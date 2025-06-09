import os
import django
import requests
from asgiref.sync import sync_to_async
from django.db.models import ObjectDoesNotExist
import asyncio
import pandas as pd
import sys
from datetime import datetime
from dotenv import load_dotenv


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


# log_file = open(f'/home/jonathanbrito48/log_youtubeAPI.log', 'w')
log_file = open(f'/log_youtubeAPI.log', 'w')


# Redirecionar stdout e stderr para o arquivo de log com timestamps
class LoggerWriter:
    def __init__(self, level):
        self.level = level
    def write(self, message):
        if message != '\n':  # Ignorar novas linhas
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.level(f"{timestamp} - {message}\n")
            log_file.flush()
    def flush(self):
        pass

sys.stdout = LoggerWriter(log_file.write)
sys.stderr = LoggerWriter(log_file.write)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.site_obpc.models import YoutubeAPI

# Passo 1: Obter o ID da playlist de uploads do canal
url_channels = 'https://www.googleapis.com/youtube/v3/channels'
params_channels = {
    'part': 'contentDetails',
    'id': os.getenv('YOUTUBE_CHANNEL_ID'),  # Use a variável de ambiente para o ID do canal
    'key': os.getenv('YOUTUBE_API_KEY')  # Use a variável de ambiente para a chave da API
}

try:
    response = requests.get(url_channels, params=params_channels)
    response.raise_for_status()
    data = response.json()
    uploads_playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print(f"ID da Playlist de Uploads: {uploads_playlist_id}")
except requests.RequestException as e:
    print(f"Erro ao fazer requisição para a API (Channels): {e}")
    uploads_playlist_id = None

# Passo 2: Se obtiver o ID da playlist, buscar os vídeos
if uploads_playlist_id:
    url_playlist_items = 'https://www.googleapis.com/youtube/v3/playlistItems'
    params_videos = {
        'part': 'snippet',
        'playlistId': uploads_playlist_id,
        'maxResults': 25,
        'key': os.getenv('YOUTUBE_API_KEY')  # Use a variável de ambiente para a chave da API
    }

    try:
        response = requests.get(url_playlist_items, params=params_videos)
        response.raise_for_status()
        video_data = response.json()
    except requests.RequestException as e:
        print(f"Erro ao fazer requisição para a API (PlaylistItems): {e}")
        video_data = {}

ids=[]
for id in video_data['items']:
    ids.append(id['snippet']['resourceId']['videoId'])
id_list = ','.join(ids)

if ids:

    url_videos = 'https://www.googleapis.com/youtube/v3/videos'
    params_videos_snippet = {
        'part': 'snippet',
        'maxResults': 25,
        'id': id_list,
        'key': 'AIzaSyBFhvKUTi7sNpKpZFzyjaI0FFMi1AfJ7Io'
    }

    try:
        response = requests.get(url_videos, params=params_videos_snippet)
        response.raise_for_status()
        video_details = response.json()
    except requests.RequestException as e:
        print(f"Erro ao fazer requisição para a API (PlaylistItems): {e}")
        video_details = {}


        
    # Criar um DataFrame para armazenar os dados dos vídeos
    df = []

    for i in video_details.get('items', []):
        df.append([
            i['id'],  # O ID do vídeo
            i['snippet']['publishedAt'],
            i['snippet']['title'],
            i['snippet']['thumbnails']['high']['url'],
            i['snippet']['liveBroadcastContent']   # Se é ao vivo, encerrado, etc.
        ])

    df = pd.DataFrame(df, columns=['videoId', 'publishedAt', 'title', 'thumbnails', 'liveBroadcastContent'])
    df = df.drop_duplicates(subset='title')
# Função para deletar os dados antigos da tabela YoutubeAPI
@sync_to_async
def deletar_dados():
    objetos_para_deletar = YoutubeAPI.objects.all()
    num_objetos_deletados, _ = objetos_para_deletar.delete()
    print(f"Objetos deletados: {num_objetos_deletados}")

# Função para inserir os novos dados da API no banco de dados
async def inserir_dados():
    if not df.empty:
        await deletar_dados()
        for video in df.values:
            novo_objeto = YoutubeAPI(
                videoId=video[0],
                publishedAt=video[1],
                title=video[2],
                thumbnails=video[3],
                liveBroadcastContent=video[4]
            )
            await sync_to_async(novo_objeto.save)()
            print(f"Dados inseridos: {novo_objeto}")

if __name__ == '__main__':
    # Execute a função assíncrona
    if uploads_playlist_id:
        asyncio.run(inserir_dados())

log_file.close()

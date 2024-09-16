import os
import django
import requests
from asgiref.sync import sync_to_async
from django.db.models import ObjectDoesNotExist
import asyncio
from datetime import datetime
import sys

log_file = open(f'/home/jonathanbrito48/log_instagram_script.log', 'w')

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

# Defina as configurações do projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

# Agora você pode importar seus modelos
from apps.site_obpc.models import Instagramapi,InstagramToken

@sync_to_async
def get_access_token():
    try:
        return InstagramToken.objects.all()[0]
    except InstagramToken.DoesNotExist:
        return None

async def fetch_instagram_data():
    # Obtém o token de acesso de forma assíncrona
    access_token = await get_access_token()
    
    if not access_token:
        return {"error": "Token de acesso não encontrado."}

    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,children&access_token={access_token.token}"  # Acessa a propriedade token corretamente
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": f"Erro ao acessar a API: {response.status_code}"}

async def processa_instagram_data():
    # Obtém os dados da API do Instagram
    dados_instagram = await fetch_instagram_data()
    
    # Verifica se há algum erro na resposta
    if "error" in dados_instagram:
        return {"error": dados_instagram["error"]}
    
    # Cria um dicionário para armazenar os dados dos posts
    dados_dict = {}
    
    # Itera sobre cada post recebido da API
    for post in dados_instagram.get('data', []):
        post_id = post['id']  # Usa o ID do post como chave
        dados_dict[post_id] = {
            "caption": post.get("caption", ""),
            "media_type": post.get("media_type", ""),
            "media_url": post.get("media_url", ""),
            "permalink": post.get("permalink", ""),
            "thumbnail_url": post.get("thumbnail_url", ""),
            "timestamp": post.get("timestamp", ""),
            "children": post.get("children", {}).get("data", [])
        }
    
    return dados_dict

# Chama a função e coleta os dados em um dicionário

async def deletar_dados():
    # Filtre os objetos que deseja deletar
    objetos_para_deletar = Instagramapi.objects.all()

    # Exclua os objetos
    num_objetos_deletados, _ = await sync_to_async(objetos_para_deletar.delete)()



async def inserir_dados():
    dados = await processa_instagram_data()
    if len(dados.keys()) > 0:
        await deletar_dados()
        for i in dados.keys():
        # Crie uma nova instância do modelo
            novo_objeto = Instagramapi(
                id_instagram=i,
                media_type= dados[i].get('media_type'),
                caption= dados[i].get('caption'),
                media_url= dados[i].get('media_url'),
                timestamp= dados[i].get('timestamp'),
                permalink=dados[i].get('permalink'),
                children= dados[i].get('children'),
                thumbnail_url= dados[i].get('thumbnail_url')
                # Adicione mais campos conforme necessário
            )
            
            # Salve o objeto no banco de dados
            await sync_to_async(novo_objeto.save)()


            print(f"Dados inseridos: {novo_objeto}")

if __name__ == '__main__':
    # Execute a função assíncrona
    asyncio.run(inserir_dados())
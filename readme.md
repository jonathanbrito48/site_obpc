# Projeto Site OBPC

Este é um projeto Django para o site da Igreja O Brasil para Cristo, com integração para exibição de vídeos do YouTube, postagens do Instagram, gerenciamento de devocionais, eventos, pastores e congregações.

## Estrutura do Projeto

- `apps/site_obpc/`: Aplicações Django customizadas (modelos, views, jobs).
- `media/`: Uploads de mídia do site.
- `static/` e `setup/static/`: Arquivos estáticos (CSS, JS, imagens).
- `templates/`: Templates HTML do Django.
- `youtube_api.py`: Script para importar vídeos do canal do YouTube para o banco de dados.
- `instagram_posts_job.py`: Script para importar posts do Instagram.
- `db_backup/`: Backups do banco de dados.
- `setup/`: Configurações do projeto Django.
- `docker-compose.yml` e `Dockerfile`: Suporte a Docker.

## Requisitos

- Python 3.10+
- Django 4.x
- Docker (opcional)
- Variáveis de ambiente em `.env` e `.env.db`

## Instalação

1. Clone o repositório.
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure o banco de dados e variáveis de ambiente conforme `.env` e `.env.db`.
5. Execute as migrações:
   ```sh
   python manage.py migrate
   ```
6. (Opcional) Carregue dados de exemplo ou backup:
   ```sh
   python manage.py loaddata db_backup/01_backupDB.sql
   ```

## Execução

Para rodar o servidor de desenvolvimento:
```sh
python manage.py runserver
```

Para importar vídeos do YouTube:
```sh
python youtube_api.py
```

Para importar posts do Instagram:
```sh
python instagram_posts_job.py
```

## Agendamento (Crontab)

Para agendar a execução automática dos scripts, adicione no crontab:
```
0 * * * * /caminho/para/.venv/bin/python /caminho/para/youtube_api.py
0 6 * * * /caminho/para/.venv/bin/python /caminho/para/instagram_posts_job.py
```

## Docker

Para rodar com Docker:
```sh
docker-compose up --build
```

## Estrutura de Pastas

- `media/`: Uploads de usuários (imagens, banners, etc)
- `static/`: Arquivos estáticos coletados
- `setup/static/`: Fontes, CSS, JS do projeto
- `templates/`: Templates HTML

## Scripts Principais

- [`youtube_api.py`](youtube_api.py): Importa vídeos do canal do YouTube para o banco de dados.
- [`instagram_posts_job.py`](instagram_posts_job.py): Importa posts do Instagram para o banco de dados.

## Licença

MIT

---

Para dúvidas, consulte os arquivos de configuração ou entre em contato com o mantenedor.
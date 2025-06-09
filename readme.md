# Projeto Site OBPC

Este é um projeto Django para o site da Igreja O Brasil para Cristo, com integração para exibição de vídeos do YouTube, postagens do Instagram, gerenciamento de devocionais, eventos, pastores e congregações.

## Estrutura do Projeto

- `apps/site_obpc/`: Aplicações Django customizadas (modelos, views, jobs).
- `media/`: Uploads de mídia do site.
- `static/` e `setup/static/`: Arquivos estáticos (CSS, JS, imagens).
- `templates/`: Templates HTML do Django.
- `youtube_api.py`: Script para importar vídeos do canal do YouTube para o banco de dados.
- `instagram_posts_job.py`: Script para importar posts do Instagram.
- `db_backup/`: Backups do banco de dados utilizados para restauração automática pelo Docker.
- `setup/`: Configurações do projeto Django.
- `docker-compose.yml` e `Dockerfile`: Suporte obrigatório a Docker.

## Requisitos

- Docker e Docker Compose (obrigatório)
- Variáveis de ambiente em `.env` e `.env.db`

> **Atenção:** O projeto depende do Docker Compose para funcionar corretamente, pois o banco de dados é restaurado automaticamente a partir do backup presente em `db_backup/`. Sem esse backup, o container do Postgres não terá dados para iniciar a aplicação.

## Instalação e Execução

1. Clone o repositório.
2. Copie os arquivos de exemplo de variáveis de ambiente:
   ```sh
   cp .env.example .env
   cp .env.db.example .env.db
   ```
3. Edite os arquivos `.env` e `.env.db` conforme necessário (veja explicação abaixo).
4. Suba a aplicação com Docker Compose:
   ```sh
   docker-compose up -d --build
   ```

## Sobre os arquivos `.env` e `.env.db`

- `.env`: Contém variáveis de ambiente do Django e da conexão do banco para o Django, além de configurações gerais da aplicação, como `SECRET_KEY`, chaves de APIs externas, etc.
- `.env.db`: Contém as configurações para criação de usuário e banco de dados Postgres, como usuário, senha, nome do banco e host.

**Exemplo de `.env.example`:**
```
DB_ENGINE=django.db.backends.postgresql
SECRET_KEY=sua_secret_key
YOUTUBE_API_KEY=sua_api_key
YOUTUBE_CHANNEL_ID=id_canal_yt
DB_NAME=siteobpc
DB_USER=seu_usuário
DB_PASSWORD=sua_senha
DB_HOST=db
DB_PORT=5432
```

**Exemplo de `.env.db.example`:**
```
POSTGRES_DB=siteobpc
POSTGRES_USER=seu_usuário
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

> **Importante:** Sempre mantenha suas chaves e senhas protegidas e nunca faça commit dos arquivos `.env` reais.

## Scripts Principais

- [`youtube_api.py`](youtube_api.py): Importa vídeos do canal do YouTube para o banco de dados.
- [`instagram_posts_job.py`](instagram_posts_job.py): Importa posts do Instagram para o banco de dados.

## Agendamento (Crontab)

Para agendar a execução automática dos scripts, adicione no crontab do container ou utilize ferramentas de agendamento conforme sua necessidade:
```
0 * * * * /caminho/para/.venv/bin/python /caminho/para/youtube_api.py
0 6 * * * /caminho/para/.venv/bin/python /caminho/para/instagram_posts_job.py
```

## Estrutura de Pastas

- `media/`: Uploads de usuários (imagens, banners, etc)
- `static/`: Arquivos estáticos coletados
- `setup/static/`: Fontes, CSS, JS do projeto
- `templates/`: Templates HTML

## Licença

MIT

---

Para dúvidas, consulte os arquivos de configuração ou entre em contato com o mantenedor.
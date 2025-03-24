#!/bin/sh

# Inicia o cron
crond

# Inicia o servidor Gunicorn para o Django
exec gunicorn setup.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 2 \
  --timeout 300 \
  --worker-class gthread \
  --threads 3 \
  --graceful-timeout 30 \
  --keepalive 5 \
  --max-requests 1000 \
  --max-requests-jitter 50 \
  --log-level debug \
  --access-logfile - \
  --error-logfile -

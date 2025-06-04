#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Inicia o cron
crond

# Inicia o servidor Gunicorn para o Django
exec gunicorn setup.wsgi:application --bind 0.0.0.0:8000


#!/bin/sh

# Inicia o cron
crond

# Inicia o servidor Gunicorn para o Django
exec gunicorn setup.wsgi:application --bind 0.0.0.0:8000

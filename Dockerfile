FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    postgresql-dev \
    build-base \
    dcron \
    python3-dev && \
    pip install -r requirements.txt

COPY crontab /etc/cron.d/django-cron
RUN chmod 0644 /etc/cron.d/django-cron
RUN crontab /etc/cron.d/django-cron

COPY . /app/

RUN chmod +x start.sh

CMD ["./start.sh"]


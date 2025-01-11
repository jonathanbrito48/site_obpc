FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    postgresql-dev \
    build-base \
    python3-dev && \
    pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn","setup.wsgi:application","--bind","0.0.0.0:8000"]


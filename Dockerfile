# Dockerfile at root

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Use the inner directory as workdir
WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --noinput

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT

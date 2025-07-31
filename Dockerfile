# Dockerfile at root

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Use the inner directory as workdir
WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend/ .

# RUN python manage.py collectstatic --noinput

# TEMP: Create superuser if not exists
RUN echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='amir').exists() or \
User.objects.create_superuser('amir', 'amir@example.com', 'Eddy@747')" \
| python manage.py shell

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT

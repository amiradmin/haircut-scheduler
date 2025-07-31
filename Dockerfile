FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy requirements.txt from backend folder
COPY backend/requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all backend code into /app
COPY backend /app/

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

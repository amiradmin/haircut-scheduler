# Use official slim Python image
FROM python:3.11-slim

# Environment variables to speed up builds and improve logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy Django project
COPY backend/ .

# Copy and make the entrypoint script executable
COPY backend/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command (can be overridden by docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

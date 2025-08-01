#!/bin/bash

# Run database migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'amir'
password = 'Eddy@747'
email = 'amirbehvandi747@gmail.com'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
EOF

# Start server (pass the CMD from Dockerfile/docker-compose)
echo "Starting server..."
exec "$@"

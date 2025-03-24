#!/bin/bash

set -e

# Wait for Postgres to be ready
echo "Waiting for PostgreSQL to start..."
while ! pg_isready -h db -p 5432 -U postgres; do
  sleep 1
done
echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if needed (optional)
# Uncomment the following if you want to create a superuser automatically
# python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword') if not User.objects.filter(username='admin').exists() else None"

# Start Django development server
echo "Starting Django server..."
# For development:
python manage.py runserver 0.0.0.0:8000

# For production, uncomment the following and comment out the development server line above
# gunicorn yourproject.wsgi:application --bind 0.0.0.0:8000

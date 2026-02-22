#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if not exists
echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser('admin', 'admin@thecitadel.com', 'admin123')
    print('Superuser created: admin / admin123')
else:
    print('Superuser already exists')
EOF

echo "Starting server..."
exec gunicorn silicon.wsgi:application --bind 0.0.0.0:$PORT

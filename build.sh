git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/yahyobek2013/LifeHub-saytim-.git
git push -u origin main#!/usr/bin/env bash
# Build script for Render deployment

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser if needed (optional)
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')" | python manage.py shell
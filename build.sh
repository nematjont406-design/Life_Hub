#!/usr/bin/env bash
# Build script for Render deployment

set -e  # Exit on any error

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

# Create admin user (only if database is ready)
python create_admin.py || echo "Admin user creation skipped (database may not be ready)"

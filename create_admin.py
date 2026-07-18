#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import User

# Admin foydalanuvchisini yaratish
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123456')
    print("Admin foydalanuvchisi yaratildi!")
    print("Login: admin")
    print("Parol: admin123456")
else:
    print("Admin foydalanuvchi allaqachon mavjud!")
    user = User.objects.get(username='admin')
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"is_staff: {user.is_staff}")
    print(f"is_superuser: {user.is_superuser}")
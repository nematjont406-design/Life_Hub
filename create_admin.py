#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import User

# Admin foydalanuvchisini yaratish yoki yangilash
username = 'admin'
password = 'admin123456'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Admin foydalanuvchisi yaratildi!")
    print(f"Login: {username}")
    print(f"Parol: {password}")
else:
    user = User.objects.get(username=username)
    # is_staff va is_superuser ni tekshirish va o'rnatish
    if not user.is_staff or not user.is_superuser:
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        print("Admin foydalanuvchi yangilandi!")
        print(f"Login: {username}")
        print(f"Parol: {password}")
    else:
        print("Admin foydalanuvchi allaqachon mavjud va to'g'ri sozlangan!")
        print(f"Username: {user.username}")
        print(f"is_staff: {user.is_staff}")
        print(f"is_superuser: {user.is_superuser}")

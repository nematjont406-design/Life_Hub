"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Add WhiteNoise for static file serving in production
BASE_DIR = Path(__file__).resolve().parent.parent
static_root = str(BASE_DIR / 'staticfiles')
application = WhiteNoise(application, root=static_root, prefix='static/')
application.add_files(str(BASE_DIR / 'media'), prefix='media/')

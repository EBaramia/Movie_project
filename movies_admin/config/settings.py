from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import optional, include

import os


load_dotenv()

include(
    "components/database.py",
    "components/apps.py",
    "components/middleware.py",
    "components/templates.py",
    "components/password_validators.py",
    "components/apps.py",
)


BASE_DIR = Path(__file__).resolve().parent.parent

LOCALE_PATHS = ['movies/locale']

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INTERNAL_IPS = [
    '127.0.0.1', 
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

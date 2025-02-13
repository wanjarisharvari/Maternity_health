import os 
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
#MEDIA_URLS ='/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Also Make aure To set allowed_hosts to '*'

ALLOWED_HOSTS = ['.vercel.app','127.0.0.1','localhost']
#/from pathlib import Path

# Use environment variable for security
SECRET_KEY = os.getenv(‘SECRET_KEY’) if “SECRET_KEY” in os.environ[“SECRET_KEY”] else config(“SECRET_KEY”)

# Debug mode (Turn off in production)
DEBUG = False  

# Allowed hosts (Update in production)
#ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # ✅ Uncommented for authentication
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'back'
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Keep or remove based on needs
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'health.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'health.wsgi.application'

# Database configuration (SQLite for development)
DATABASES = {}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

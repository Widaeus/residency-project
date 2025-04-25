import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-fallback-key')
DEBUG      = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    # Djangos egna
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_browser_reload',
    
    # Din app
    'rotations.apps.RotationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     os.getenv('POSTGRES_DB'),
        'USER':     os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST':     os.getenv('DB_HOST', 'db'),
        'PORT':     os.getenv('DB_PORT', '5432'),
    }
}


TEMPLATES[0]['DIRS'] = [ BASE_DIR / 'templates' ]

STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

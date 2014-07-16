#encoding:utf-8
"""
Django settings for recetario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u*rm4pwq#m5m@ci=g-4lfo(g#5-&egf2d1#ed3^_)(1e&icz#5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'plantillas'),
)

MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'carga')

MEDIA_URL = 'http://127.0.0.1:8000/media/'

ALLOWED_HOSTS = []

ADMINS = (

    ('Geovanny Rocha', 'georocha24@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    #'django.contrib.sites',
    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'recetario.urls'

WSGI_APPLICATION = 'recetario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
'NAME': 'prueba1', # Or path to database file if using sqlite3.
'USER': 'root', # Not used with sqlite3.
'PASSWORD': '', # Not used with sqlite3.
'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Tegucigalpa'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#configuracion para enviar mensajes usando gmail
EMAIL_USE_TLS=True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'georocha24@gmail.com'
EMAIL_HOST_PASSWORD = '240819882403'
EMAIL_PORT = 587

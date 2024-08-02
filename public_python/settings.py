"""
Django settings for public_python project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#consente l'apertura di popup nello stesso dominio, evitando il blocco per il clickjacking
SECURE_FRAME_DENY = False
SECURE_CONTENT_TYPE_DENY = False
X_FRAME_OPTIONS = 'SAMEORIGIN'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gm5q(q6s2821e*x(d=ws6+3=zuql6l2-cfd767vzjgkdj6wp*&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1','localhost']
else:
    ALLOWED_HOSTS = ['bleish.serv00.net']


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'anag_utenti.apps.AnagUtentiConfig',
    'contable.apps.ContableConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'info.apps.InfoConfig',
    'mptt',
    'django_mptt_admin',
    'organizations',
    'stdForm',
    'multigroup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'public_python.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'public_python.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            #'ENGINE': 'django.db.backends.mysql',
            #'NAME': 'm9800_agricontable',
            #'USER': 'm9800_bleish',
            #'PASSWORD': 'gioio,io@SERV00',
            #'HOST':'mysql4.serv00.com',
            #'PORT':'3306',
            #'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",}
        }
    }
else:
    DATABASES = {
        'default': {
            #'ENGINE': 'django.db.backends.sqlite3',
            #'NAME': BASE_DIR / 'db.sqlite3',
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'm9800_agricontable',
            'USER': 'm9800_bleish',
            'PASSWORD': 'gioio,io@SERV00',
            'HOST':'mysql4.serv00.com',
            'PORT':'3306',
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",}
        }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

#STATIC_URL = 'static/'
STATIC_URL = 'static/'
MEDIA_URL = 'media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

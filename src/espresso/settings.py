"""
Django settings for espresso project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i^_&k@nc9!&4vyeas#51tm4)g+6=ovs055ss63p4@3)+!m0del'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['web']


# Application definition

INSTALLED_APPS = [
    'jsignature',
    'homepage.apps.HomepageConfig',
    'parchment_intake.apps.ParchmentIntakeConfig',
    'dry_coffee.apps.DryCoffeeConfig',
    'beans_intake.apps.BeansIntakeConfig',
    'green_beans_intake.apps.GreenBeansIntakeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'crispy_forms',
    'storages',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'espresso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'espresso.wsgi.application'

AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''


AWS_STORAGE_BUCKET_NAME='obou'
AWS_S3_REGION_NAME='nyc3'
AWS_S3_ENDPOINT_URL='https://obou.nyc3.digitaloceanspaces.com'
AWS_DEFAULT_ACL = 'public-read'

# DEFAULT_FILE_STORAGE = 'beans_intake.custom_storage.MediaStorage'  Pa33w0rd
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'espresso',
        'USER': 'pgadmin',
        'PASSWORD': 'something',        
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC_URL = '/code/static/'      # current deployed
STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, "static") 

MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/'
# MEDIA_URL = '/uploads/'
# MEDIA_ROOT=os.path.join(BASE_DIR, "uploads") 

# settings.py
JSIGNATURE_WIDTH = 400
JSIGNATURE_HEIGHT = 150
JSIGNATURE_COLOR='BLACK'
JSIGNATURE_RESET_BUTTON=True
JSIGNATURE_DECOR_COLOR='GREEN'
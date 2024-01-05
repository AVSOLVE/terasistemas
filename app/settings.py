
import os
import dj_database_url
from prettyconf import config

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@1741q#tj0i+xt6@f%hp!ja&e0sxinlmyy8*#(jma3na#)@i!!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=config.boolean)
ENVIRONMENT = config("ENVIRONMENT", default="PROD")
ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.process',
    'app.core',
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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": dj_database_url.parse(config("DATABASE_URL"))}


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

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = False


STORAGES = {
    "default": {
        "BACKEND": "app.storage_backends.PublicMediaStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

if ENVIRONMENT == "PROD":
    STORAGES["staticfiles"] = {
        "BACKEND": "app.storage_backends.StaticStorage",
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



region_name = "nyc3"
endpoint_url = f"https://{region_name}.digitaloceanspaces.com"
access_key = config("SPACE_KEY")
secret_key = config("SPACE_SECRET")
bucket_name = config("SPACE_NAME")

AWS_S3_ENDPOINT_URL = endpoint_url
AWS_S3_REGION_NAME = region_name
AWS_S3_ACCESS_KEY_ID = access_key
AWS_S3_SECRET_ACCESS_KEY = secret_key

# AWS_S3_SESSION_PROFILE="s3"
AWS_STORAGE_BUCKET_NAME = bucket_name


STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "upload"),
    os.path.join(BASE_DIR, "static"),

]
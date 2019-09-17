# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from django.utils.translation import ugettext_lazy as _
from decouple import config, Csv


# ############## BASE_DIR (manage.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f'BASE_DIR: {BASE_DIR}')

# ############## Secret Key
SECRET_KEY = config('SECRET_KEY')

# ############## Debug
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = config('TEMPLATE_DEBUG', default=False, cast=bool)

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# ############## Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_filters',
    'django_celery_results',
    ##### Rest
    'rest_framework',
    # 'rest_framework.authtoken',
    ##### libs
    'taggit',
    ##### apps
    'ocp',
    'ocp.accounts',
    'ocp.core',
    'ocp.courses',
    'ocp.forum',
    'ocp.languages',
]

# ############## MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions across requests
    'django.middleware.locale.LocaleMiddleware',  # Traz as bibliotecas para realizar a internacionalização do sistema
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ############## URL's
ROOT_URLCONF = 'ocp.urls'

# ############## TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors',
                # 'django.core.context_processors',
                # 'django.core.context_processors.request',
                # 'django.core.context_processors.i18n',  # Habilita a internacionalização
                # 'django.core.context_processors.static',
            ],
        },
    },
]

# ############## WSGI
WSGI_APPLICATION = 'ocp.wsgi.application'

# ############## DATABASE

# ########################### Password validation
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

# ##########################  Password validation

# ##########################  Internationalization
LANGUAGE_CODE = 'en'  # Set the default language for your site.
TIME_ZONE = 'Europe/Madrid'   # UTC é o padrão de hora mundial
USE_I18N = True     # Provide a lists of languages which your site supports.
USE_L10N = True     # True=> Time Zone respeitará sua localização (default=>False)
USE_TZ = False   # False => não usa internacionalização / True=> Tradução respeitará sua localização
LANGUAGES = [
    ('en', _('English')),
    ('pt-br', _('Portuguese')),
    ('es', _('Spanish')), ]

BASE_LOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_PATHS = (
    os.path.join(BASE_LOC, "locale/"),
    os.path.join(BASE_LOC, "accounts/locale/"),
    os.path.join(BASE_LOC, "core/locale/"),
    os.path.join(BASE_LOC, "courses/locale/"),
    os.path.join(BASE_LOC, "forum/locale/"),
    os.path.join(BASE_LOC, "languages/locale"),
)

# ########################## AWS S3
USE_S3 = config('USE_S3', default=True, cast=bool)
if USE_S3:
    # # ############## Application definition - AWS
    INSTALLED_APPS += [
      'storages',
    ]
    # # ########################## AWS S3 - Settings Variable
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_S3_REGION_NAME = 'us-west-2'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = None

# ########################## REDIS
CELERY_BROKER_URL = config('CELERY_BROKER_URL')

# Configurando Celery para rodar em paralelo (True => para testes)
CELERY_TASK_ALWAYS_EAGER = config('CELERY_TASK_ALWAYS_EAGER_DESENV', default=False, cast=bool)

# ########################## django-celery-results
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

# ########################## REST
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# ########################## Auth
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_URL = 'accounts:logout'
AUTH_USER_MODEL = 'accounts.User'  # AUTH_USER_MODEL muda do modelUserAdmin para o configurado


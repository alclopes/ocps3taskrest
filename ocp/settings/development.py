from .common import *

# ############## BASE_DIR

# ############## Secret Key

# ############## Debug
DEBUG = config('DEBUG_DESENV', default=True, cast=bool)

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS_DESENV', cast=Csv())

# ############## Application definition

# ############## MIDDLEWARE

# ############## TEMPLATES
TEMPLATE_DEBUG = config('DEBUG_DESENV', default=True, cast=bool)

# ############## WSGI

# ############## DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ############## DATABASE
# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE_POSTGRES'),
#         'NAME': config('DB_NAME_POSTGRES'),
#         'USER': config('DB_USER_POSTGRES'),
#         'PASSWORD': config('DB_PASSWORD_POSTGRES'),
#         'HOST': config('DB_HOST_POSTGRES'),
#         'PORT': config('DB_PORT_POSTGRES'),
#     }
# }

# ########################### Password validation

# ##########################  Internationalization

# ########################## AWS S3

# # ########################## AWS S3 Private Media Upload
if USE_S3:
    # # ########################## AWS S3 - Settings Variable
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME_DESENV')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # # ########################## AWS S3 Static files (CSS, JavaScript, Images)
    STATICFILES_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    STATICFILES_STORAGE = config('AWS_STATICFILES_STORAGE')

    # # ########################## AWS S3 Private Media Upload
    MEDIAFILES_LOCATION = 'media'
    AWS_S3_PATH = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  # 20190822/0724
    MEDIA_URL = f'https://{AWS_S3_PATH}/{MEDIAFILES_LOCATION}/'
    DEFAULT_FILE_STORAGE = config('AWS_DEFAULT_FILE_STORAGE')
else:
    # ########################### Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    # # STATIC_URL=> aponta para dentro de cada app core
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    # # STATIC_ROOT=> defines the single folder you want to collect all your static files into

    # # ########################## Media
    # Media files are for user-uploaded content.
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ########################### Caches

# ########################### envolvidos (Login, Logout)

# ########################## REDIS

# ########################## Email
EMAIL_BACKEND = config('EMAIL_BACKEND_DESENV')
EMAIL_USE_TLS = config('EMAIL_USE_TLS_DESENV', default='True')
EMAIL_HOST = config('EMAIL_HOST_DESENV', default='')
EMAIL_PORT = config('EMAIL_PORT_DESENV', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER_DESENV', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD_DESENV', default='')
RECEIVE_EMAIL = config('RECEIVE_EMAIL_DESENV', default='')





from .common import *

# ############## BASE_DIR

# ############## Secret Key

# ############## Debug
DEBUG = config('DEBUG_DESENV', default=True, cast=bool)

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS_DESENV', cast=Csv())

# ############## Application definition
# INSTALLED_APPS += 
#
# ]

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
    # # Amazon S3/myBucketName/static/myimage/files
    STATICFILES_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    # STATIC_ROOT = [os.path.join(BASE_DIR, 'mypage/static'), ]  # Não usar com S3
    STATICFILES_STORAGE = config('AWS_STATICFILES_STORAGE')

    # # ########################## AWS S3 Private Media Upload
    # # Amazon S3/myBucketName/media/myimage/files
    MEDIAFILES_LOCATION = 'media'

    # https://testheroku-assets.s3.amazonaws.com/media/myimage/images/Course_6.png
    AWS_S3_PATH = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  # 20190822/0724
    MEDIA_URL = f'https://{AWS_S3_PATH}/{MEDIAFILES_LOCATION}/'

    # MEDIA_ROOT = os.path.join(BASE_DIR, 'mypage/media') # Não usar com S3
    DEFAULT_FILE_STORAGE = config('AWS_DEFAULT_FILE_STORAGE')
else:
    # # ########################## Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'  # aponta para dentro de cada app core
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Heroku pode servir desde que seja nesta pasta
    STATIC_ROOT = (
        os.path.join(BASE_DIR, 'static'),
    )

    # # ########################## Media
    # Media files are for user-uploaded content.
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ########################### Caches

# ########################### envolvidos (Login, Logout)


# ########################## REDIS

# ########################## Email
#### How to Allow Users to Reset Password in Django 2/2 (Django Tutorial) | Part 22
CONTACT_EMAIL = config('CONTACT_EMAIL_DESENV')
EMAIL_BACKEND = config('EMAIL_BACKEND_DESENV')
EMAIL_USE_TLS = config('EMAIL_USE_TLS_DESENV', default='True')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL_DESENV', default='')
EMAIL_HOST = config('EMAIL_HOST_DESENV', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER_DESENV', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD_DESENV', default='')
EMAIL_PORT = config('EMAIL_PORT_DESENV', default='')
RECEIVE_EMAIL = config('RECEIVE_EMAIL_DESENV', default='')



from .common import *

# Heroku
import dj_database_url

# ##############  Databases
DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL_PROD'))}

# # ########################## AWS S3 Private Media Upload
if USE_S3:
    # # ########################## AWS S3 - Settings Variable
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
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


# ########################## Email
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default='True')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = config('EMAIL_PORT', default='')
RECEIVE_EMAIL = config('RECEIVE_EMAIL', default='')









from .common import *

# Heroku
import dj_database_url

# ##############  DATABASES
# Heroku settings
DATABASES = {
    'default':  dj_database_url.config(),
}

# # ########################## AWS S3 Private Media Upload
if USE_S3:
    # # ########################## AWS S3 - Settings Variable
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
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














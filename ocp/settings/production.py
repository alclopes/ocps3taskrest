from .common import *

# Heroku
import dj_database_url

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# ##############  Databases
DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}

# ########################### Password validation

# ##########################  Internationalization

# # ########################## AWS S3 Private Media Upload
if not USE_S3:
    # ########################### Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    # # STATIC_URL=> aponta para dentro de cada app core
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    # # STATIC_ROOT=> defines the single folder you want to collect all your static files into

    # # ########################## Media
    # Media files are for user-uploaded content.
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')












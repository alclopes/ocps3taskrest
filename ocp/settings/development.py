from .common import *
from decouple import config, Csv
import dj_database_url

# ############## BASE_DIR

# ############## Secret Key

# ############## Debug
DEBUG = True
TEMPLATE_DEBUG = True

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS_DESENV', cast=Csv())

# ############## Application definition

# ############## MIDDLEWARE

# ############## TEMPLATES
TEMPLATE_DEBUG = config('DEBUG_DESENV', default=True, cast=bool)

# ############## WSGI

# ##############  Databases Sqlite
# DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL_DESENV'))}

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE_POSTGRES'),
        'NAME': config('DB_NAME_POSTGRES'),
        'USER': config('DB_USER_POSTGRES'),
        'PASSWORD': config('DB_PASSWORD_POSTGRES'),
        'HOST': config('DB_HOST_POSTGRES'),
        'PORT': config('DB_PORT_POSTGRES'),
    }
}

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

# ########################### Caches

# ########################### envolvidos (Login, Logout)

# ########################## Email

# ########################## REDIS

# ########################## Celery

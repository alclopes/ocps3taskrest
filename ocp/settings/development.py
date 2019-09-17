from .common import *

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

# ##############  Databases
DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL_DESENV'))}

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
EMAIL_BACKEND = config('EMAIL_BACKEND_DESENV')
EMAIL_USE_TLS = config('EMAIL_USE_TLS_DESENV', default='True')
EMAIL_HOST = config('EMAIL_HOST_DESENV', default='')
EMAIL_PORT = config('EMAIL_PORT_DESENV', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER_DESENV', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD_DESENV', default='')
RECEIVE_EMAIL = config('RECEIVE_EMAIL_DESENV', default='')

# ########################## REDIS

# ########################## Celery

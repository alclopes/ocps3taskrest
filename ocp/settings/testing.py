from .common import *

# ############## Debug
# logging.disable(logging.INFO)
DEBUG = True
TEMPLATE_DEBUG = True

# ##############  Databases
DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL_TEST'))}

# ############## TEMPLATES

# ##########################Email

# ########################## Celery
BROKER_BACKEND = 'memory'
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True


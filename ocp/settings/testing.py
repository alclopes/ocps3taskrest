#coding: utf-8
from .common import *

# ############## Debug
# logging.disable(logging.INFO)
DEBUG = True
TEMPLATE_DEBUG = True

# ############## DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ############## TEMPLATES

# ##########################Email

# ########################## Celery
BROKER_BACKEND = 'memory'
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True


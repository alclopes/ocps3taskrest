'''
Para rodar testes em ambiente de desenvolvimento:
python manage.py test --settings=ocp.settings_testing
'''
#coding: utf-8
import os
import logging
from decouple import config

from .development import *

# logging.disable(logging.INFO)
DEBUG = True
TEMPLATE_DEBUG = True

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

###########################Email

# BROKER_BACKEND = 'memory'

# SOUTH_TESTS_MIGRATE = False

# SKIP_SLOW_TESTS = True

# RUN_SLOW_TESTS = False
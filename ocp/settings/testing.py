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
CONTACT_EMAIL = config('CONTACT_EMAIL_TEST')
EMAIL_BACKEND = config('EMAIL_BACKEND_TEST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS_TEST', default='True')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL_TEST', default='')
EMAIL_HOST = config('EMAIL_HOST_TEST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER_TEST', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD_TEST', default='')
EMAIL_PORT = config('EMAIL_PORT_TEST', default='')
RECEIVE_EMAIL = config('RECEIVE_EMAIL_TEST', default='')

# BROKER_BACKEND = 'memory'

# SOUTH_TESTS_MIGRATE = False

# SKIP_SLOW_TESTS = True

# RUN_SLOW_TESTS = False
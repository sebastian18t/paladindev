from .base import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DEBUG = False

ALLOWED_HOSTS = ['paladindev.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'den0jo98ega41i',
        'USER': 'eckvshfxabsmqf',
        'PASSWORD': '2ffb20468cec7332c78b064dc7a0130b589027d06967b9ceeedeb2cbb452725d',
        'HOST': 'ec2-18-211-48-247.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

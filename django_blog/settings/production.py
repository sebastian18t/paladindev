from .base import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd541kl6t87sn0d',
        'USER': 'cblkavczzpvadw',
        'PASSWORD': 'b543a4a8c520b543f989b614509c70cc8e2608bd95cecd94c2044fb803f8b617',
        'HOST': 'ec2-54-236-169-55.compute-1.amazonaws.com',
        'PORT': 5432,
        
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
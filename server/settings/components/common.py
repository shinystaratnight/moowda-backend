from settings import config

from server import BASE_DIR

ROOT_URLCONF = 'server.urls'
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

WSGI_APPLICATION = 'server.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

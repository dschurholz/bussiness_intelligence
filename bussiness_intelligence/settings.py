"""
Django settings for bussiness_intelligence project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname, join, realpath
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.realpath(os.path.join(BASE_DIR, '..'))

STATIC_ROOT = ROOT_DIR + '/static/'

MEDIA_ROOT = ROOT_DIR + '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ec%c^uc@)xb(6rrdp55^wl&@%fz5tkw!%gfw94a!g*8!ngj9nw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'core',

    # Dependencies
    'rest_framework',
    'south',
    'debug_toolbar',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'bussiness_intelligence.urls'

WSGI_APPLICATION = 'bussiness_intelligence.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.OAuth2Authentication'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.YAMLRenderer',
        'rest_framework.renderers.XMLRenderer',
        'rest_framework_msgpack.renderers.MessagePackRenderer'
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.YAMLParser',
        'rest_framework.parsers.XMLParser',
        'rest_framework_msgpack.parsers.MessagePackParser'
    )

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

try:
    from .local_settings import *
except ImportError, exp:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured("local_settings.py is not defined. "
                               "Did you forget to symlink one?")

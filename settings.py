# -*- coding: utf-8 -*-
import os, sys
from settings_local import *

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

MEDIA_ROOT         = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT        = os.path.join(PROJECT_ROOT, 'sitestatic')
STATICFILES_DIRS   = (os.path.join(PROJECT_ROOT, 'static'),)

THUMBS_URL         = MEDIA_URL + 'thumbs'

ADMIN_MEDIA_PREFIX = '/admin/media/'

# Это общее для всех
SITE_ID            = 1
SECRET_KEY         = ''

USE_I18N           = False
USE_L10N           = False
TIME_ZONE          = 'Europe/Moscow'
LANGUAGE_CODE      = 'ru-ru'

ROOT_URLCONF       = 'urls'

LOGIN_URL          = '/login'
LOGIN_REDIRECT_URL = '/'

MANAGERS = ADMINS = ()

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.request',
	'django.core.context_processors.debug',
	'django.core.context_processors.static',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',
)

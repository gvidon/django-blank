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
SECRET_KEY         = 'hot1!ntbc$on@ypotwo5r#e9=^)jqbmc$5s-ud8$!wk^l@p&y3'

USE_I18N           = False
USE_L10N           = False
TIME_ZONE          = 'Europe/Moscow'
LANGUAGE_CODE      = 'ru-ru'

ROOT_URLCONF       = 'urls'

LOGIN_URL          = '/login'
LOGIN_REDIRECT_URL = '/'

MAX_SHOW_PAGES     = 20
PAGINATE_BY        = 10

INTERNAL_IPS       = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG  = {
	'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

MANAGERS = ADMINS = (
	#('Elena Kantemirova', 'elena.kantemirova@gmail.com'),
	('Gvidon Malyarov'  , 'nenegoro@gmail.com'),
)

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
	#'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	#'django.middleware.cache.FetchFromCacheMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',
	
	'debug_toolbar',
	
	# Изъебнулся. Весь project и есть одно приложение
	PROJECT_ROOT.split('/')[-1]
)

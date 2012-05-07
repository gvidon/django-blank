# -*- coding: utf-8 -*-
import os

DEBUG_SQL      = True
DEBUG          = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT   = '/home/nide/code/dailytags'
MEDIA_URL      = '/media/'
STATIC_URL     = '/static/'

MONGODB_NAME   = 'dailytags'

DATABASES = {
	'default': {
		'ENGINE'  : 'django.db.backends.mysql',
		'USER'    : 'root',
		'PASSWORD': '123097',
		'NAME'    : 'dailytags',
	}
}

CACHES = {
	'default': {
		'BACKEND' : 'redis_cache.RedisCache',
		'LOCATION': 'localhost:6379',
		
		'OPTIONS': {
			'DB'          : 1,
			'PASSWORD'    : '',
			'PARSER_CLASS': 'redis.connection.HiredisParser'
		},
	},
}


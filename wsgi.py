import os, sys
from gevent import monkey, wsgi

WSGI_HOST = '127.0.0.1'
WSGI_PORT = 8888

monkey.patch_socket()

sys.path.insert(0, os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.handlers.wsgi import WSGIHandler

wsgi.WSGIServer((WSGI_HOST, WSGI_PORT), WSGIHandler()).serve_forever()

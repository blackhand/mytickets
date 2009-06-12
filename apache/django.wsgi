import os, sys
from os.path import join, dirname
PROJECT_DIR = join(dirname(__file__), '..')
BASE_DIR = join(PROJECT_DIR, '..')
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mytickets.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


import os
import sys

# Your actual username and path
path = '/home/poly/vcyou'
project_home = path

# Add the project directory and its parent to the Python path
if path not in sys.path:
    sys.path.insert(0, project_home)
    sys.path.insert(0, os.path.dirname(project_home))

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'vcyou.settings'

# Initialize Django WSGI application
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

application = get_wsgi_application()
application = WhiteNoise(application) 
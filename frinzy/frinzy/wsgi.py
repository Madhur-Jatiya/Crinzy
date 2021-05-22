"""
WSGI config for frinzy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

path = "/home/Crinzy/.virtualenvs/frinzy/frinzy"
if path not in sys.path:
    sys.path.append(path)


os.environ["DJANGO_SETTINGS_MODULE"] = 'frinzy.settings'

from django.core.wsgi import get_wsgi_application



application = get_wsgi_application()


from dotenv import load_dotenv
project_folder = os.path.expanduser('home/Crinzy/.virtualenvs/frinzy/frinzy')
load_dotenv(os.path.join(project_folder, '.env'))
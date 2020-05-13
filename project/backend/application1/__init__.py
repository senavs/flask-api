import os

from flask import Blueprint

from ...configuration import BASE_DIR

# import your views route here

app_application1 = Blueprint('application1', __name__,
                             url_prefix='/',
                             static_folder='static',
                             static_url_path=os.path.join(BASE_DIR, 'project', 'frontend', 'static'),
                             template_folder=os.path.join(BASE_DIR, 'project', 'frontend', 'templates'))

# add your views route here

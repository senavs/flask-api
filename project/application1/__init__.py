import os

from flask import Blueprint

# import your views route here

app_application1 = Blueprint('application1', __name__,
                             url_prefix='/',
                             static_folder='static',
                             static_url_path=os.path.join(os.path.dirname(__file__), 'static'),
                             template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

# add your views route here

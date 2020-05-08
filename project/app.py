import os

from project import create_app

app = create_app(os.environ.get('FLASK_CONFIG', 'develop'))

import os

from flask import Blueprint

from .views import APIDocumentation
from ...settings import project_env

app = Blueprint('docs', 'docs', url_prefix='/',
                template_folder=os.path.join(project_env.PROJECT_DIR, 'resources', 'docs', 'templates'),
                static_folder=os.path.join(project_env.PROJECT_DIR, 'resources', 'docs', 'static'),
                static_url_path='/static/docs',
                )
app.add_url_rule('/docs', view_func=APIDocumentation.as_view('docs'))

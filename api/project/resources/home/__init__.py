from flask import Blueprint

from .views import HomePage

app = Blueprint('home', 'home', url_prefix='/')
app.add_url_rule('/', view_func=HomePage.as_view('home'))

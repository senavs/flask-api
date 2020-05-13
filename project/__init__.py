from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .configuration import config
from .backend.application1 import app_application1

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str = 'develop'):
    # configurations
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # init app
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    app.register_blueprint(app_application1)

    return app

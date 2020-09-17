from flask import Flask

from .modules.default.error_handler import ErrorHandler
from .modules.default.signals import APPSignals
from .resources import docs, home

error = ErrorHandler()
signals = APPSignals()


def create_app():
    app = Flask(__name__, static_folder=None)

    # init app
    error.init_app(app)
    signals.init_app(app)

    # blueprints
    app.register_blueprint(docs.app)
    app.register_blueprint(home.app)

    return app

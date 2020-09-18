from flask import Flask
from flask_cors import CORS

from .modules.default.database import Database
from .modules.default.error_handler import ErrorHandler
from .modules.default.metrics import PrometheusMetricsEndpoint
from .modules.default.signals import APPSignals
from .resources import docs, home

cors = CORS()
db = Database()
error = ErrorHandler()
metrics = PrometheusMetricsEndpoint(multiprocessing=False)
signals = APPSignals()


def create_app():
    app = Flask(__name__, static_folder=None)

    # init app
    cors.init_app(app)
    db.init_app(app)
    error.init_app(app)
    metrics.init_app(app)
    signals.init_app(app)

    # blueprints
    app.register_blueprint(docs.app)
    app.register_blueprint(home.app)

    return app

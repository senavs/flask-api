from flask import Flask

from .modules.default.database import Database
from .modules.default.error_handler import ErrorHandler
from .modules.default.metrics import PrometheusMetricsEndpoint
from .modules.default.signals import APPSignals
from .resources import docs, home

db = Database()
error = ErrorHandler()
metrics = PrometheusMetricsEndpoint(multiprocessing=False)
signals = APPSignals()


def create_app():
    app = Flask(__name__, static_folder=None)

    # init app
    db.init_app(app)
    error.init_app(app)
    metrics.init_app(app)
    signals.init_app(app)

    # blueprints
    app.register_blueprint(docs.app)
    app.register_blueprint(home.app)

    return app

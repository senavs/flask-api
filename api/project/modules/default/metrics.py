import os
from typing import Optional, Union

from flask import Blueprint, Flask

from .bases import FlaskBaseExtension
from ...utils.default.metrics import metrics_multiprocessing, metrics_monoprocessing


class PrometheusMetricsEndpoint(FlaskBaseExtension):

    def __init__(self, app: Optional[Union[Flask, Blueprint]] = None, *, multiprocessing: Optional[bool] = False):
        super().__init__(app)

        if multiprocessing and not os.environ.get('prometheus_multiproc_dir'):
            raise ValueError(f"to use multiprocessing metrics, please define 'prometheus_multiproc_dir' to environments variables")

        self._is_multiprocessing = bool(multiprocessing)

    def init_app(self, app: Union[Flask, Blueprint]):
        super().init_app(app)

        self._register_metrics_endpoint()

    def _register_metrics_endpoint(self):
        if self._is_multiprocessing:
            self.app.add_url_rule('/metrics', view_func=metrics_multiprocessing)
        else:
            self.app.add_url_rule('/metrics', view_func=metrics_monoprocessing)

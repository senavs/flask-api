from typing import Callable, Type, Union

from flask import Blueprint, Flask
from werkzeug.exceptions import HTTPException

from .bases import FlaskBaseExtension
from ...utils.default.error_handler import handler_exception, handler_http_exception, handler_validation
from ...exceptions.default import ValidationException


class ErrorHandler(FlaskBaseExtension):
    _view_funcs = {
        Exception: handler_exception,
        HTTPException: handler_http_exception,
        ValidationException: handler_validation
    }

    def init_app(self, app: Union[Flask, Blueprint]):
        super().init_app(app)

        self._register_errors_handlers()

    @classmethod
    def add_error_handler(cls, code_exception: Union[Type[Exception], int], view_func: Callable):
        cls._view_funcs[code_exception] = view_func

    def _register_errors_handlers(self):
        for code_exception, view_func in self._view_funcs.items():
            self.app.register_error_handler(code_exception, view_func)

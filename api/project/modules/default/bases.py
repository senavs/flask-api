from typing import Optional, Union

from flask import Flask, Blueprint


class FlaskBaseExtension:
    _app: Union[Flask, Blueprint]

    def __init__(self, app: Optional[Union[Flask, Blueprint]] = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Union[Flask, Blueprint]):
        self._app = app

    @property
    def app(self) -> Union[Flask, Blueprint, None]:
        return self._app

    def __repr__(self):
        return f'{type(self).__qualname__}(app={self.app})'

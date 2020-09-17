from collections import defaultdict
from typing import Callable, Union

from flask import Blueprint, Flask

from .bases import FlaskBaseExtension


class APPSignals(FlaskBaseExtension):
    _view_funcs = {
        'before_first_request': [],
        'before_request': defaultdict(list),
        'after_request': defaultdict(list),
        'teardown_request': defaultdict(list)
    }

    def init_app(self, app: Union[Flask, Blueprint]):
        super().init_app(app)

        self._register_signals()

    @classmethod
    def add_signals(cls, location: str, blueprint: Union[None, str], func: Callable):
        if location not in cls._view_funcs.keys():
            raise ValueError(f'location must be in ({", ".join(cls._view_funcs.keys())})')

        if location == 'before_first_request':
            cls._view_funcs['before_first_request'].append(func)
        else:
            cls._view_funcs[location][blueprint].append(func)

    def _register_signals(self):
        for name, signal in self._view_funcs.items():
            self.app.__dict__[f'{name}_funcs'] = signal

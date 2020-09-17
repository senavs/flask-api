from functools import wraps
from typing import Callable, Type

from flask import request
from pydantic import BaseModel, ValidationError

from ...exceptions.default import RequestValidationError


class Parser:
    REQUEST_DATA_LOCATION = ('args', 'form', 'files', 'values', 'json')

    def __init__(self, location: str):
        if location not in self.REQUEST_DATA_LOCATION:
            raise ValueError(f'location must be in {",".join(self.REQUEST_DATA_LOCATION)}')
        self._location = str(location)

    def __call__(self, model: Type[BaseModel]) -> Callable:
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if self._location == 'json':
                    req = request.json or {}
                else:
                    req = getattr(request, self._location)

                try:
                    valid_req = model(**req)
                except ValidationError as err:
                    raise RequestValidationError(str(err))
                else:
                    return func(request_=valid_req.dict(), *args, **kwargs)

            return wrapper

        return decorator


parse_args = Parser('args')
parse_files = Parser('files')
parse_form = Parser('form')
parse_json = Parser('json')
parse_values = Parser('values')

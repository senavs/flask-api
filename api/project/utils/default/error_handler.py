from werkzeug.exceptions import HTTPException


def handler_http_exception(error: HTTPException):
    return {'message': type(error).__qualname__.lower(), 'detail': str(error)}, error.code, {'Content-Type': 'application/json'}


def handler_exception(error: Exception):
    return {'message': type(error).__qualname__.lower(), 'detail': str(error)}, 500, {'Content-Type': 'application/json'}


def handler_validation(error: Exception):
    return {'message': type(error).__qualname__.lower(), 'detail': str(error)}, 400, {'Content-Type': 'application/json'}

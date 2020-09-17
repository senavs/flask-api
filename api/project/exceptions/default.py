class ValidationException(Exception):
    pass


class RequestValidationError(ValidationException):
    pass


class ResponseValidationError(ValidationException):
    pass

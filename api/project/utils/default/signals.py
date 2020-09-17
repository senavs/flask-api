from flask import Response


def json_response(response: Response) -> Response:
    if 'Content-Type' not in response.headers:
        response.headers['Content-Type'] = 'application/json'
    return response

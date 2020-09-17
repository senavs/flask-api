from flask.views import MethodView

from .models import HomeRequest
from ...modules.default.parser import parse_json


class HomePage(MethodView):

    @parse_json(HomeRequest)
    def post(self, request_):
        return request_

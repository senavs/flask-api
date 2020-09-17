import json
import unittest

from project import create_app


class TestErrorHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        self.app_client = self.app.test_client()

        response = self.app_client.get('/page_not_found')
        self.response = json.loads(response.data.decode('utf-8'))

    def test_application_json(self):
        self.assertIsInstance(self.response, dict)

    def test_notfound(self):
        for key in self.response:
            self.assertIn(key, ('message', 'detail'))


if __name__ == '__main__':
    unittest.main()

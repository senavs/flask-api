import unittest

from project import create_app


class TestApplicationStartup(unittest.TestCase):
    APP_URLS = ('/', '/docs', '/static/docs/<path:filename>')

    def setUp(self) -> None:
        self.app = create_app()
        self.app_client = self.app.test_client()

    def test_urls(self):
        for url in self.app.url_map.iter_rules():
            self.assertIn(str(url), self.APP_URLS)


if __name__ == '__main__':
    unittest.main()

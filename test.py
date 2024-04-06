import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Sentiment Analysis</title>', response.data)

    def test_result_route(self):
        response = self.app.get('/result')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Analyzed Results</title>', response.data)

if __name__ == '__main__':
    unittest.main()

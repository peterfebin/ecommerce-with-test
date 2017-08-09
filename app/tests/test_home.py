import unittest
from app import app

class Home(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def testHomePage(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        pass

# runs the unit tests in the module
if __name__ == '__main__':
      unittest.main()

import unittest
from app import app

class Login(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def testLoginPage(self):
        result = self.app.get('/login')
        self.assertEqual(result.status_code, 200)

 #   def testLoginSubmit(self)
   
    def tearDown(self):
        pass

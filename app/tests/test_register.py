import unittest
from app import app
from flask import session

class Register(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_METHODS'] = []
        self.app = app.test_client()

    def testRegisterPage(self):
        result = self.app.get('/register')
        self.assertEqual(result.status_code, 200)

    def register(self, username, email, password, confirm):
        return self.app.post(
                '/register',
                data=dict(username=username, email=email, password=password, confirm=confirm),
                follow_redirects=True
                )


    def testRegisterSubmit(self):
        response = self.register('test12312313', 'test12312312', 'test', 'test')
        self.assertEqual(response.status_code, 200)
#        self.assertIn(b'You are now registered', response.data)

    def tearDown(self):
        pass

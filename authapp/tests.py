from django.test import TestCase, Client
from django.contrib.auth.models import User

class AuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass1234')

    def test_login(self):
        response = self.client.post('/auth/login/', {'username': 'testuser', 'password': 'pass1234'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        response = self.client.post('/auth/login/', {'username': 'wrong', 'password': 'wrong'}, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_logout(self):
        self.client.login(username='testuser', password='pass1234')
        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 200)

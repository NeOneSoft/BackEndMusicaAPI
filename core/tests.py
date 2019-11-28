from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TokenTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')

    def test_authenticate(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})

        assert 'access' in result.data

    def test_valid_token(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})
        token = result.data['access']

        canciones_result = self.client.get('/api/v1/canciones/', HTTP_AUTHORIZATION='Bearer ' + token)
        artistas_result = self.client.get('/api/v1/artistas/', HTTP_AUTHORIZATION='Bearer ' + token)
        albumes_result = self.client.get('/api/v1/albumes/', HTTP_AUTHORIZATION='Bearer ' + token)

        assert canciones_result.status_code, artistas_result == 200
        assert albumes_result.status_code == 200

    def test_valid_token(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})
        token = result.data['access']

        canciones_result = self.client.get('/api/v1/canciones/', HTTP_AUTHORIZATION='Bearer ' + token)
        artistas_result = self.client.get('/api/v1/artistas/', HTTP_AUTHORIZATION='Bearer ' + token)
        albumes_result = self.client.get('/api/v1/albumes/', HTTP_AUTHORIZATION='Bearer ' + token)

        assert canciones_result, artistas_result.status_code == 200
        assert albumes_result.status_code == 200






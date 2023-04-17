from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('user_test',password='test123')

    def test_user_auth(self):
        """verifiy user auth"""
        user = authenticate(username='user_test',password='test123')
        self.assertTrue(user is not None) and user.is_authenticated

    def test_request_unautorized(self):
        """unautorized auth"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_GET_user_auth(self):
        """test"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


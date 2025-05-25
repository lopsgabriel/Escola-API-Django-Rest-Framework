from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.reverse import reverse

class AuthenticationTestCase(APITestCase):
  def setUp(self):
    self.user = User.objects.create_superuser(username='testuser', password='testpass')
    self.url = reverse('Estudantes-list')

  def test_authentication(self):
    """Teste que verifica a autenticação de um usuário"""
    user = authenticate(username = 'testuser', password = 'testpass')
    self.assertTrue((user is not None) and user.is_authenticated)
  
  def test_wrong_password_authentication(self):
    """Teste que verifica a autenticação de um usuário com a senha incorreta"""
    user = authenticate(username = 'testuser', password = 'wrongpass')
    self.assertFalse((user is not None) and user.is_authenticated)
  
  def test_wrong_username_authentication(self):
    """Teste que verifica a autenticação de um usuário com o username incorreto"""
    user = authenticate(username = 'wronguser', password = 'testpass')
    self.assertFalse((user is not None) and user.is_authenticated)

  def test_request_get_authentication(self):
    """Teste que verifica a requisição GET autorizada"""
    self.client.force_authenticate(self.user)
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_request_get_no_authentication(self):
    """Teste que verifica uma requisição GET não autorizada"""
    response = self.client.get(self.url)
    self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
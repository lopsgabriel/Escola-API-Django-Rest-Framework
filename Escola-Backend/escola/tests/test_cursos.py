from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursosSerializer

class CursosTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='biells')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.get(pk=1)
        self.curso_02 = Curso.objects.get(pk=2)

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_um_curso(self):
        """Teste para verificar a requisição GET para listar um curso"""
        #/cursos/1/
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursosSerializer(instance=dados_curso).data
        #print(dados_estudante_serializados)
        self.assertEqual(response.data,dados_curso_serializados)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        dados = {
            'codigo':'CTT3',
            'descricao':'Curso teste 3',
            'nivel':'A'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE para deletar um curso"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        dados = {
            'codigo':'CTT1',
            'descricao':'Curso teste 1 atualizado',
            'nivel':'I'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from rest_framework import status
# from rest_framework.reverse import reverse
# from escola.models import Curso
# from escola.serializers import CursosSerializer
# class CursosTestCase(APITestCase):
#   fixtures = ['prototipo_banco.json']
#   def setUp(self):
#     self.user = User.objects.get(username='biells')
#     self.url = reverse('Cursos-list')
#     self.client.force_authenticate(user=self.user)
#     self.curso_01 = Curso.objects.get(pk=1)
#     self.curso_02 = Curso.objects.get(pk=2)

#   def test_request_get_cursos(self):
#     response = self.client.get(self.url)
#     self.assertEqual(response.status_code, status.HTTP_200_OK)

#   def test_request_get_one_curso(self):
#     response = self.client.get(self.url+'1/')
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     dados_curso = Curso.objects.get(pk=1)
#     dados_curso_serializer = CursosSerializer(instance=dados_curso).data
#     self.assertEqual(response.data, dados_curso_serializer)
  
#   def test_request_post_curso(self):
#     dados = {
#       'codigo':'PYTHON', 
#       'descricao':'Curso de Python', 
#       'nivel':'B'
#     }
#     response = self.client.post(self.url, dados)
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
#   def test_request_delete_um_curso(self):
#     response = self.client.delete(f'{self.url}1/')
#     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
  
#   def test_request_put_um_curso(self):
#     dados = {
#       'codigo':'PYTHON', 
#       'descricao':'Curso de Python', 
#       'nivel':'B'
#     }
#     response = self.client.put(f'{self.url}1/', dados)
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
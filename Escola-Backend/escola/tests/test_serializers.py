from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursosSerializer, MatriculaSerializer

class EstudanteSerializerTestCase(TestCase):
  def setUp(self):
    self.estudante = Estudante(
      nome='teste modelo',
      cpf='70838025056', 
      email='kKQ0f@example.com', 
      data_de_nascimento='2000-01-01', 
      celular='11 00000-0000'
    )
    self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

  def test_estudante_serializer(self):
    """Teste que verifica os atributos do modelo de estudante"""
    dados = self.serializer_estudante.data
    self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_de_nascimento', 'celular']))
  
  def test_estudante_serializer_data(self):
    """Teste que verifica os atributos do modelo de estudante"""
    dados = self.serializer_estudante.data
    self.assertEqual(dados['nome'], self.estudante.nome)
    self.assertEqual(dados['email'], self.estudante.email)
    self.assertEqual(dados['cpf'], self.estudante.cpf)
    self.assertEqual(dados['data_de_nascimento'], self.estudante.data_de_nascimento)
    self.assertEqual(dados['celular'], self.estudante.celular)

class CursosSerializerTestCase(TestCase):
  def setUp(self):
    self.curso = Curso(
      codigo='PYTHON',
      descricao='Curso de Python',
      nivel='B'
    )
    self.serializer_curso = CursosSerializer(instance=self.curso)

  def test_curso_serializer(self):
    """Teste que verifica os atributos do modelo de curso"""
    dados = self.serializer_curso.data
    self.assertEqual(set(dados.keys()), set(['id', 'codigo', 'descricao', 'nivel']))
  
  def test_curso_serializer_data(self):
    """Teste que verifica os atributos do modelo de curso"""
    dados = self.serializer_curso.data
    self.assertEqual(dados['codigo'], self.curso.codigo)
    self.assertEqual(dados['descricao'], self.curso.descricao)
    self.assertEqual(dados['nivel'], self.curso.nivel)

class MatriculaSerializerTestCase(TestCase):
  def setUp(self):
    self.estudante_matricula = Estudante.objects.create(
      nome='teste modelo',
      cpf='70838025056', 
      email='kKQ0f@example.com', 
      data_de_nascimento='2000-01-01', 
      celular='11 00000-0000'
    ) 
    self.curso_matricula = Curso.objects.create(codigo='PYTHON', descricao='Curso de Python', nivel='B')
    self.matricula = Matricula.objects.create(estudante=self.estudante_matricula, curso=self.curso_matricula, periodo='M')
    self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

  def test_matricula_serializer(self):
    """Teste que verifica os atributos do modelo de matricula"""
    dados = self.serializer_matricula.data
    self.assertEqual(set(dados.keys()), set(['id', 'estudante', 'curso', 'periodo']))
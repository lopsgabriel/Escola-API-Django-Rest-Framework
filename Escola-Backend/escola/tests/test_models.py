from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
  def setUp(self):
    self.estudante = Estudante.objects.create(
      nome='teste modelo',
      cpf='70838025056', 
      email='kKQ0f@example.com', 
      data_de_nascimento='2000-01-01', 
      celular='11 00000-0000'
    )
  
  def test_estudante_model(self):
    """Teste que verifica os atributos do modelo de estudante"""
    self.assertEqual(self.estudante.cpf, '70838025056')
    self.assertEqual(self.estudante.email, 'kKQ0f@example.com')
    self.assertEqual(self.estudante.data_de_nascimento, '2000-01-01')
    self.assertEqual(self.estudante.celular, '11 00000-0000')
    self.assertEqual(self.estudante.nome, 'teste modelo')
  
class ModelCursoTestCase(TestCase):
  def setUp(self):
    self.curso = Curso.objects.create(codigo='PYTHON', descricao='Curso de Python', nivel='B')

  
  def test_curso_model(self):
    """Teste que verifica os atributos do modelo de curso"""
    self.assertEqual(self.curso.codigo, 'PYTHON')
    self.assertEqual(self.curso.descricao, 'Curso de Python')
    self.assertEqual(self.curso.nivel, 'B')
  
class ModelMatriculaTestCase(TestCase):
  def setUp(self):
    self.estudande_matricula = Estudante.objects.create(
      nome='teste modelo',
      cpf='70838025056', 
      email='kKQ0f@example.com', 
      data_de_nascimento='2000-01-01', 
      celular='11 00000-0000'
    ) 
    self.curso_matricula = Curso.objects.create(codigo='PYTHON', descricao='Curso de Python', nivel='B')
    self.matricula = Matricula.objects.create(estudante=self.estudande_matricula, curso=self.curso_matricula)

  
  def test_matricula_model(self):
    """Teste que verifica os atributos do modelo de matricula"""
    self.assertEqual(self.matricula.estudante, self.estudande_matricula)
    self.assertEqual(self.matricula.curso, self.curso_matricula)
    self.assertEqual(self.matricula.periodo, 'M')
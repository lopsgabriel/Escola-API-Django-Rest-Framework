from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_de_nascimento = models.DateField(blank=False)
    celular = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.TextField(max_length=100, blank=False)
    nivel = models.CharField(max_length=100, choices=NIVEL, blank=False, null=False, default = 'B')

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=100, choices=PERIODO, blank=False, null=False, default = 'M')
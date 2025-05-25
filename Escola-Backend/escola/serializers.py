from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_de_nascimento', 'celular']
    def validate(self, data):
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF invalido'})
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome':'Nome invalido'})
        if celular_invalido(data['celular']):
            raise serializers.ValidationError({'celular':'Celular invalido'})
        return data

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.ReadOnlyField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursosSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Curso
        fields = ['estudante_nome']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()    

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']
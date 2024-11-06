from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursosSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer,ListaMatriculasEstudanteSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    # serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer

class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        query_set = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        query_set = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasCursoSerializer


from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSrializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
        """Exibindo todos os cursos"""
        queryset = Curso.objects.all()
        serializer_class = CursoSrializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


# Create your views here.

from django.shortcuts import render
from .models import Curso, Professor, Aluno

def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escolaOnline/cursos.html', {'cursos': cursos})

def curso_view(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'escolaOnline/curso.html', {'curso': curso})

def professores_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escolaOnline/professores.html', {'professores': professores})

def alunos_view(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escolaOnline/alunos.html', {'alunos': alunos})
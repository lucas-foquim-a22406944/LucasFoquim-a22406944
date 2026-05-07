from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tecnologia, Competencia, Formacao, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def is_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()

def index_view(request):
    return render(request, 'portfolio/index.html')

# PROJETOS
def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

@login_required(login_url='/accounts/login/')
def projeto_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})

@login_required(login_url='/accounts/login/')
def projeto_editar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})

@login_required(login_url='/accounts/login/')
def projeto_apagar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': projeto, 'tipo': 'Projeto'})

# TECNOLOGIAS
def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

@login_required(login_url='/accounts/login/')
def tecnologia_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

@login_required(login_url='/accounts/login/')
def tecnologia_editar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

@login_required(login_url='/accounts/login/')
def tecnologia_apagar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': tecnologia, 'tipo': 'Tecnologia'})

# COMPETENCIAS 
def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

@login_required(login_url='/accounts/login/')
def competencia_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Nova Competência'})

@login_required(login_url='/accounts/login/')
def competencia_editar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Editar Competência'})

@login_required(login_url='/accounts/login/')
def competencia_apagar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': competencia, 'tipo': 'Competência'})

# FORMACOES 
def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related('competencias').all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

@login_required(login_url='/accounts/login/')
def formacao_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Nova Formação'})

@login_required(login_url='/accounts/login/')
def formacao_editar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Editar Formação'})

@login_required(login_url='/accounts/login/')
def formacao_apagar(request, id):
    if not is_gestor(request.user):
        raise PermissionDenied
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': formacao, 'tipo': 'Formação'})

# SOBRE 
def sobre_view(request):
    tecnologias = Tecnologia.objects.all()
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/sobre.html', {
        'tecnologias': tecnologias,
        'makingof': makingof,
    })
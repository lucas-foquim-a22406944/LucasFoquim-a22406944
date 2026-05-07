from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def is_autor(user):
    return user.groups.filter(name='autores').exists()

# ── LISTAGEM ──
def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('comentarios', 'likes').all()
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

# ── DETALHE ──
def artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.all()
    form_comentario = ComentarioForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        if 'comentario' in request.POST:
            form_comentario = ComentarioForm(request.POST)
            if form_comentario.is_valid():
                comentario = form_comentario.save(commit=False)
                comentario.artigo = artigo
                comentario.autor = request.user
                comentario.save()
                return redirect('artigo', id=id)
        if 'like' in request.POST:
            if request.user in artigo.likes.all():
                artigo.likes.remove(request.user)
            else:
                artigo.likes.add(request.user)
            return redirect('artigo', id=id)

    return render(request, 'artigos/artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    })

# ── CRIAR ──
@login_required(login_url='/accounts/login/')
def artigo_criar(request):
    if not is_autor(request.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Novo Artigo'})

# ── EDITAR ──
@login_required(login_url='/accounts/login/')
def artigo_editar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if not is_autor(request.user) or artigo.autor != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Editar Artigo'})

# ── APAGAR ──
@login_required(login_url='/accounts/login/')
def artigo_apagar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if not is_autor(request.user) or artigo.autor != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos')
    return render(request, 'artigos/confirmar_apagar.html', {'objeto': artigo})
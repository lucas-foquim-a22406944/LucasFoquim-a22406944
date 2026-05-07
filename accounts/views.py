from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegistoForm
from .models import Perfil
import secrets
from django.contrib.auth.models import User, Group

# ── helper para enviar o magic link ──
def envia_magic_link(user, email, request):
    token = secrets.token_urlsafe(32)
    perfil, _ = Perfil.objects.get_or_create(user=user)
    perfil.token = token
    perfil.save()
    link = request.build_absolute_uri(f'/accounts/magic-link/?token={token}')
    send_mail(
        subject='Portfolio: Autenticação',
        message=f'Olá {user.username}, clica no link para entrar: {link}',
        from_email='noreply@portfolio.pt',
        recipient_list=[email],
    )

# ── login normal ──
def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projetos')
        else:
            erro = 'Username ou password incorretos.'
    return render(request, 'accounts/login.html', {'erro': erro})

# ── logout ──
def logout_view(request):
    logout(request)
    return redirect('login')

# ── registo ──
def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        grupo_autores, _ = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo_autores)
        return redirect('login')
    return render(request, 'accounts/registo.html', {'form': form})

# ── magic link: pedir link ──
def magic_link_request(request):
    mensagem = None
    if request.method == 'GET' and 'email' in request.GET:
        email = request.GET.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            envia_magic_link(user, email, request)
            mensagem = 'Link enviado! Verifica o teu email.'
        else:
            mensagem = 'Email não encontrado.'
    return render(request, 'accounts/magic_link_request.html', {'mensagem': mensagem})

# ── magic link: verificar token ──
def magic_link_verify(request):
    token = request.GET.get('token')
    try:
        perfil = Perfil.objects.get(token=token)
        perfil.token = ''  # invalida o token após uso
        perfil.save()
        login(request, perfil.user)
        return redirect('projetos')
    except Perfil.DoesNotExist:
        return render(request, 'accounts/magic_link_invalido.html')
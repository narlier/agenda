from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import redirect, render

from .models import Evento


# Create your views here.
def login_user(request):
    return render(request, 'core/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Evento.objects.all()
    context = {'eventos': evento, 'usuario': user}
    return render(request, 'core/agenda.html', context)

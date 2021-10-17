from django.http import response
from django.shortcuts import render

from .models import Evento


# Create your views here.
def lista_eventos(request):
    evento = Evento.objects.all()
    context = {'eventos': evento}
    return render(request, 'core/agenda.html', context)

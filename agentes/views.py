from django.shortcuts import render
from .models import Agente


# Create your views here.

def lista_agente(request):
    lista_agente = Agente.objects.all()
    template = 'agentes/agentes.html'
    context = {
        'lista_agente': lista_agente
    }

    return render(request, template, context)

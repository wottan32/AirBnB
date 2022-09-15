from django.shortcuts import render
from propiedad.models import Propiedad, Categoria
from agentes.models import Agente
from django.db.models import Count


# Create your views here.


def inmueble(request):
    lista_categoria = Categoria.objects.annotate(property_count=Count('propiedad')).values('nombre_categoria',
                                                                                           'property_count',
                                                                                           'imagen')
    print(lista_categoria)
    lista_propiedad = Propiedad.objects.all()
    lista_agente = Agente.objects.all()
    template = 'inmueble/inmueble.html'
    context = {
        'lista_categoria_home': lista_categoria,
        'lista_propiedad_home': lista_propiedad,
        'lista_agente_home': lista_agente
    }

    return render(request, template, context)

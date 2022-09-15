from django.shortcuts import render

# Create your views here.
from .models import Propiedad, Categoria
from .forms import ReservaForm
from django.db.models import Q


def lista_propiedad(request):
    lista_propiedad = Propiedad.objects.all()
    template = 'propiedad/lista.html'

    address_query = request.GET.get('q')
    tipo_propiedad = request.GET.getlist('tipo_propiedad', None)
    if address_query and tipo_propiedad:
        print(address_query)
        print(tipo_propiedad)
        lista_propiedad = lista_propiedad.filter(
            Q(name__icontains=address_query) &
            Q(tipo_propiedad__icontains=tipo_propiedad[0])
        ).distinct()

    print(lista_propiedad)

    context = {
        'lista_propiedad': lista_propiedad
    }

    return render(request, template, context)


def detalles_propiedad(request):
    # propiedad = Propiedad.objects.get(id=id)
    detalles_propiedad = Propiedad.objects.get(id=id)

    template = 'propiedad/detalle.html'

    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_form.save()
    else:
        reserva_form = ReservaForm()

    context = {
        'detalles_propiedad': detalles_propiedad,
        'reserva_form': reserva_form
    }

    return render(request, template, context)

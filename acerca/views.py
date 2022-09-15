from django.shortcuts import render

# Create your views here.
from .models import Acerca


def acerca(request):
    acerca = Acerca.objects.last()
    template = 'acerca/acerca.html'
    context = {
        'acerca': acerca
    }

    return render(request, template, context)

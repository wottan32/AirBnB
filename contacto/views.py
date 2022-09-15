from django.shortcuts import render, redirect
from .forms import ContactoForm
# Create your views here.
from .models import ContactoDetalles
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse, HttpResponseRedirect


def send_mail(request):
    contactodetalles = ContactoDetalles.objects.last()
    template = 'contacto/contacto.html'

    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            subject = contacto_form.cleaned_data['asunto']
            from_email = contacto_form.cleaned_data['mail_remitente']
            message = contacto_form.cleaned_data['mensaje']

            try:
                sm(subject, message, from_email, ['mariotorreslagos@gmail.com'])

            except BadHeaderError:
                return HttpResponse('invalid header')

            return redirect('contacto:success')

    else:
        contacto_form = ContactoForm()

    context = {
        'contactodetalles': contactodetalles,
        'contacto_form': contacto_form
    }

    return render(request, template, context)


def success(request):
    return HttpResponse('Message Sent Successfully')

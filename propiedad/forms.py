from django import forms
from .models import Reserva, Propiedad


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

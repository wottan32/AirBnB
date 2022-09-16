from django import forms


class ContactoForm(forms.Form):
    asunto = forms.CharField()
    mail_remitente = forms.EmailField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)

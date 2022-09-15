from django.db import models


# Create your models here.

class ContactoDetalles(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    numero_contacto = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)

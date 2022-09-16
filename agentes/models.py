from django.db import models


# Create your models here.


class Agente(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='agente/')

    def __str__(self):
        return self.nombre

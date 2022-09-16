from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.gis.db import models

# Create your models here.

tipo_propiedad = (
    ('venta', "venta"),
    ('arriendo', "arriendo")
)


class Propiedad(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_propiedad = models.CharField(choices=tipo_propiedad, max_length=10)
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey('Categoria', null=True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2, max_digits=8)
    numero_camas = models.PositiveIntegerField()
    numero_banos = models.PositiveIntegerField()
    numero_estacionamiento = models.PositiveIntegerField()
    # servicios_choices = (("", "---------"), ("PISCINA", "piscina"), ("GIMNASIO", "gimnasio"), ("SPA", "spa"),
    #                     ("JACUZZI", "jacuzzi"), ("INTERNET", "internet"),
    #                     ("CABLE", "cable"), ("SECURITY", "security"), ("LAVANDERIA", "lavanderia"),
    #                     ("PARKING", "parking"), ("BODEGA", "bodega"),
    #                     ("OFICINA", "oficina"), ("RESTAURANTE", "restaurante"),
    #                     ("CENTRO DE EVENTOS", "centro de eventos"))
    # servicios = models.CharField(max_length=100, choices=servicios_choices, null=True, blank=True, default=None)
    imagen = models.ImageField(upload_to='propiedad/', null=True)
    imagen1 = models.ImageField(upload_to='propiedad/', null=True)
    imagen2 = models.ImageField(upload_to='propiedad/', null=True)
    imagen3 = models.ImageField(upload_to='propiedad/', null=True)
    imagen4 = models.ImageField(upload_to='propiedad/', null=True)
    imagen5 = models.ImageField(upload_to='propiedad/', null=True)
    locacion = models.PointField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='categoria/', null=True)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    notas = models.TextField()
    modalidad_choices = (("", "---------"), ("ARRIENDO", "Arriendo"), ("Venta", "Venta"))
    modalidad = models.CharField(max_length=100, choices=modalidad_choices, null=False, blank=False, default=None)

    def __str__(self):
        return self.nombre

from django.db import models


# Create your models here.


class Acerca(models.Model):
    vision = models.TextField()
    mision = models.TextField()
    imagen = models.ImageField(upload_to='acerca/')

    def __str__(self):
        return str(self.id)

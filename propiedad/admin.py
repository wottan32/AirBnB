from django.contrib import admin

# Register your models here.
from .models import Propiedad, Categoria, Reserva


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_propiedad', 'categoria', 'area', 'numero_camas', 'numero_banos',
                    'numero_estacionamiento']
    search_fields = ['nombre', 'tipo_propiedad']
    list_filter = ['categoria', 'tipo_propiedad']


admin.site.register(Propiedad, PropertyAdmin)
admin.site.register(Categoria)
admin.site.register(Reserva)

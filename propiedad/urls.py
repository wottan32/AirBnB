from django.urls import path
from . import views


app_name = 'propiedad'


urlpatterns = [
    path('', views.lista_propiedad, name='lista_propiedad'),
    path('<int:id>', views.detalles_propiedad, name='detalles_propiedad'),

]

from django.urls import path
from . import views

app_name = 'agentes'

urlpatterns = [
    path('', views.lista_agente, name='lista_agente'),

]

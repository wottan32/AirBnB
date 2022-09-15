from django.urls import path
from . import views

app_name = 'inmueble'

urlpatterns = [
    path('', views.inmueble, name='inmueble'),

]

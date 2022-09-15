from django.urls import path
from . import views

app_name = 'acerca'

urlpatterns = [
    path('', views.acerca, name='acerca'),

]

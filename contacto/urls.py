from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('', views.send_mail, name='send_mail'),
    path('success/', views.success, name='success'),
    # path(r'^$', views.index, name='index'),
]

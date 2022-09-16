"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.inmueble, name='inmueble')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='inmueble')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inmueble.urls', namespace='inmueble')),
    path('propiedad/', include('propiedad.urls', namespace='propiedad')),
    path('agentes/', include('agentes.urls', namespace='agentes')),
    path('acerca/', include('acerca.urls', namespace='acerca')),
    path('contacto/', include('contacto.urls', namespace='contacto'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "RESERVA KASA SYS ADMIN"
admin.site.site_title = "PROPIEDAD RESERVA ADMIN"
admin.site.site_index_title = "Bienvenido al portal de administración de RESERVA KASA"

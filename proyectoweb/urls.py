"""proyectoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index
from core.views import inicio
from core.views import nosotros
from core.views import contacto
from core.views import donaciones
from core.views import tienda
from core.views import tienda_bandanas
from core.views import tienda_correas
from core.views import tienda_identificadores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('inicio', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('contacto', contacto, name="contacto"),
    path('donaciones', donaciones, name="donaciones"),
    path('tienda', tienda, name="tienda"),
    path('tienda_bandanas', tienda_bandanas, name="tienda_bandanas"),
    path('tienda_correas', tienda_correas, name="tienda_correas"),
    path('tienda_identificadores', tienda_identificadores, name="tienda_identificadores"),
]

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
from msilib.schema import LockPermissions
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from core.views import index
from core.views import inicio
from core.views import nosotros
from core.views import contacto
from core.views import donaciones
from core.views import tienda
from core.views import administracion_productos
from core.views import form_agregar_producto
from core.views import form_modificar_producto
from core.views import form_eliminar_producto
from core.views import administracion_fundaciones
from core.views import form_agregar_fundacion
from core.views import form_modificar_fundacion
from core.views import form_eliminar_fundacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('inicio', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('contacto', contacto, name="contacto"),
    path('donaciones', donaciones, name="donaciones"),
    path('tienda/<int:categoria>/', tienda, name="tienda"),
    path('administracion', administracion_productos, name="administracion_productos"),
    path('administracion_productos', administracion_productos, name="administracion_productos"),
    path('form_agregar_producto', form_agregar_producto, name="form_agregar_producto"),
    path('form_modificar_producto/<idProducto>/', form_modificar_producto, name="form_modificar_producto"),
    path('form_eliminar_producto/<idProducto>', form_eliminar_producto, name="form_eliminar_producto"),
    path('administracion_fundaciones', administracion_fundaciones, name="administracion_fundaciones"),
    path('form_agregar_fundacion', form_agregar_fundacion, name="form_agregar_fundacion"),
    path('form_modificar_fundacion/<idFundacion>/', form_modificar_fundacion, name="form_modificar_fundacion"),
    path('form_eliminar_fundacion/<idFundacion>', form_eliminar_fundacion, name="form_eliminar_fundacion"),
]
#Se enlaza las variables MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



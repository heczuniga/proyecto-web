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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static 
from core.views import index
from core.views import login
from core.views import inicio
from core.views import nosotros
from core.views import contacto
from core.views import donaciones
from core.views import tienda
from core.views import administracion_productos
from core.views import form_agregar_producto
from core.views import form_modificar_producto
from core.views import form_eliminar_producto
from core.views import administracion_categorias
from core.views import form_agregar_categoria
from core.views import form_modificar_categoria
from core.views import form_eliminar_categoria
from core.views import administracion_pymes
from core.views import form_agregar_pyme
from core.views import form_modificar_pyme
from core.views import form_eliminar_pyme
from core.views import administracion_contactos
from core.views import form_eliminar_contacto
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('inicio/', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('donaciones/', donaciones, name="donaciones"),
    path('tienda/<int:codCategoria>/', tienda, name="tienda"),
    path('administracion_categorias/', administracion_categorias, name="administracion_categorias"),
    path('form_agregar_categoria/', form_agregar_categoria, name="form_agregar_categoria"),
    path('form_modificar_categoria/<int:codCategoria>/', form_modificar_categoria, name="form_modificar_categoria"),
    path('form_eliminar_categoria/<int:codCategoria>/', form_eliminar_categoria, name="form_eliminar_categoria"),
    path('administracion/', administracion_productos, name="administracion_productos"),
    path('administracion_productos/', administracion_productos, name="administracion_productos"),
    path('form_agregar_producto/', form_agregar_producto, name="form_agregar_producto"),
    path('form_modificar_producto/<int:idProducto>/', form_modificar_producto, name="form_modificar_producto"),
    path('form_eliminar_producto/<int:idProducto>', form_eliminar_producto, name="form_eliminar_producto"),
    path('administracion_pymes/', administracion_pymes, name="administracion_pymes"),
    path('form_agregar_pyme/', form_agregar_pyme, name="form_agregar_pyme"),
    path('form_modificar_pyme/<int:idPyme>/', form_modificar_pyme, name="form_modificar_pyme"),
    path('form_eliminar_pyme/<int:idPyme>/', form_eliminar_pyme, name="form_eliminar_pyme"),
    path('administracion_contactos/', administracion_contactos, name="administracion_contactos"),
    path('form_eliminar_contacto/<int:idContacto>/', form_eliminar_contacto, name="form_eliminar_contacto"),
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon.ico')),
    path('api/', include('api_rest.urls')),
]
#Se enlaza las variables MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



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
from core.views import administracion_productos
from core.views import form_agregar_producto
from core.views import form_modificar_producto
from core.views import form_eliminar_producto
from core.views import administracion_parametros
from core.views import form_agregar_parametro
from core.views import form_modificar_parametro
from core.views import form_eliminar_parametro
from core.views import administracion_pymes
from core.views import form_agregar_pyme
from core.views import form_modificar_pyme
from core.views import form_eliminar_pyme
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', administracion_productos, name="administracion_productos"),
    path('administracion_parametros/', administracion_parametros, name="administracion_parametros"),
    path('form_agregar_parametro/', form_agregar_parametro, name="form_agregar_parametro"),
    path('form_modificar_parametro/<int:codParametro>/', form_modificar_parametro, name="form_modificar_parametro"),
    path('form_eliminar_parametro/<int:codParametro>/', form_eliminar_parametro, name="form_eliminar_parametro"),
    path('administracion/', administracion_productos, name="administracion_productos"),
    path('administracion_productos/', administracion_productos, name="administracion_productos"),
    path('form_agregar_producto/', form_agregar_producto, name="form_agregar_producto"),
    path('form_modificar_producto/<int:idProducto>/', form_modificar_producto, name="form_modificar_producto"),
    path('form_eliminar_producto/<int:idProducto>', form_eliminar_producto, name="form_eliminar_producto"),
    path('administracion_pymes/', administracion_pymes, name="administracion_pymes"),
    path('form_agregar_pyme/', form_agregar_pyme, name="form_agregar_pyme"),
    path('form_modificar_pyme/<int:idPyme>/', form_modificar_pyme, name="form_modificar_pyme"),
    path('form_eliminar_pyme/<int:idPyme>/', form_eliminar_pyme, name="form_eliminar_pyme"),
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon.ico')),
    path('api/', include('api_rest.urls')),
]
#Se enlaza las variables MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



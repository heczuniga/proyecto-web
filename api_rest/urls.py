
from django.urls import path

from api_rest.views import ListaProductos
from api_rest.views import ListaProductosCategoria
from api_rest.views import CrearProducto
from api_rest.views import Productos
from api_rest.views import ListaContactos
from api_rest.views import CrearContacto
from api_rest.views import Contactos
from api_rest.views import ListaFundaciones
from api_rest.views import CrearFundacion
from api_rest.views import Fundaciones
from api_rest.views import ListaCategorias
from api_rest.views import CrearCategoria
from api_rest.views import Categorias
from rest_framework.authtoken import views

urlpatterns = [
    path('productos/lista/', ListaProductos.as_view()),
    path('productos/categoria/<int:codCategoria>/', ListaProductosCategoria.as_view()),
    path('productos/', CrearProducto.as_view()),
    path('productos/<int:idProducto>/', Productos.as_view()),
    path('contactos/lista/', ListaContactos.as_view()),
    path('contactos/', CrearContacto.as_view()),
    path('contactos/<int:idContacto>/', Contactos.as_view()),
    path('fundaciones/lista/', ListaFundaciones.as_view()),
    path('fundaciones/', CrearFundacion.as_view()),
    path('fundaciones/<int:idFundacion>/', Fundaciones.as_view()),
    path('categorias/lista/', ListaCategorias.as_view()),
    path('categorias/', CrearCategoria.as_view()),
    path('categorias/<int:codCategoria>/', Categorias.as_view()),
    path('generar_token/', views.obtain_auth_token),
]

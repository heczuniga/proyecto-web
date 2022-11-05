
from django.urls import path

from .views import ListaProductos
from .views import ListaProductosCategoria
from .views import CrearProducto
from .views import Productos
from .views import ListaContactos
from .views import CrearContacto
from .views import Contactos
from .views import ListaFundaciones
from .views import CrearFundacion
from .views import Fundaciones
from .views import ListaCategorias
from .views import CrearCategoria
from .views import Categorias

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
]

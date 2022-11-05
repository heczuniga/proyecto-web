
from django.urls import path

from .views import ListaProductos
from .views import CrearProducto
from .views import Productos
from .views import ListaPymes
from .views import CrearPyme
from .views import Pymes
from .views import ListaParametros
from .views import CrearParametro
from .views import Parametros

urlpatterns = [
    path('productos/lista/', ListaProductos.as_view()),
    path('productos/', CrearProducto.as_view()),
    path('productos/<int:idProducto>/', Productos.as_view()),
    path('pymes/lista/', ListaPymes.as_view()),
    path('pymes/', CrearPyme.as_view()),
    path('pymes/<int:idPyme>/', Pymes.as_view()),
    path('parametros/lista/', ListaParametros.as_view()),
    path('parametros/', CrearParametro.as_view()),
    path('parametros/<int:codParametro>/', Parametros.as_view()),
]

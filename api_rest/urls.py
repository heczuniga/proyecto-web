
from django.urls import path

from .views import ListaProductos
from .views import CrearProducto
from .views import Productos
from .views import ListaFundaciones
from .views import CrearFundacion
from .views import Fundaciones
from .views import ListaParametros
from .views import CrearParametro
from .views import Parametros

urlpatterns = [
    path('productos/lista/', ListaProductos.as_view()),
    path('productos/', CrearProducto.as_view()),
    path('productos/<int:idProducto>/', Productos.as_view()),
    path('fundaciones/lista/', ListaFundaciones.as_view()),
    path('fundaciones/', CrearFundacion.as_view()),
    path('fundaciones/<int:idFundacion>/', Fundaciones.as_view()),
    path('parametros/lista/', ListaParametros.as_view()),
    path('parametros/', CrearParametro.as_view()),
    path('parametros/<int:codParametro>/', Parametros.as_view()),
]

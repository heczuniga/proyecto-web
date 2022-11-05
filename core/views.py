
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth import logout

from rest_framework import status
import requests

# Vista de página base
def index(request):

    return render(request, 'core/index.html')

# Vista de página base
def login(request):

    return render(request, 'core/login.html')


# Vista de página de inicio
def inicio(request):
    
    return render(request, 'core/inicio.html')


# Vista de página de nosotros
def nosotros(request):
    
    return render(request, 'core/nosotros.html')


# Vista de página de contacto
def contacto(request):

    url_api = 'http://127.0.0.1:8000/api/contactos/'
    datos = {}

    if request.method == 'POST':

        response = requests.post(url_api, data=request.POST)

        if response.status_code == status.HTTP_201_CREATED:
            datos['mensaje'] = "Los datos del formulario se han recibido correctamente! Pronto nos comunicaremos contigo."
        else:
            datos['error'] = "Se ha producido un error al almacenar el formulario. Verifica tus datos y reintenta."

        return render(request, "core/contacto.html", datos)
    
    return render(request, "core/contacto.html")


# Vista de página de donaciones
def donaciones(request):

    url_api = 'http://127.0.0.1:8000/api/fundaciones/lista/'

    response = requests.get(url_api).json()

    datos = {
         'fundaciones': response

    }
    return render(request,'core/donaciones.html', datos)


# Vista de página de tienda
def tienda(request, codCategoria):

    url_api_categorias = 'http://127.0.0.1:8000/api/categorias/lista/'
    url_api_productos = f'http://127.0.0.1:8000/api/productos/categoria/{codCategoria}/'

    # Recuperamos las categorías
    response_categorias = requests.get(url_api_categorias).json()

    # Recuperamos los productos de dicha categoría
    response_productos = requests.get(url_api_productos).json()
    datos = {'categorias': response_categorias,
             'productos': response_productos,
             'categoria': codCategoria}

    return render(request, 'core/tienda.html', datos)


# Vista de página para administración de productos
def administracion_productos(request):

    url_api = "http://127.0.0.1:8000/api/productos/lista/"

    # Recuperamos los productos
    response = requests.get(url_api).json()
    datos = {'productos': response}

    return render(request, 'core/administracion-productos.html', datos)


# Vista de formulario para agregar productos
def form_agregar_producto(request):

    url_api_lista_pymes = 'http://127.0.0.1:8000/api/pymes/lista/'
    url_api_productos = 'http://127.0.0.1:8000/api/productos/'

    # Recuperamos los PYMEs
    response_pymes = requests.get(url_api_lista_pymes).json()

    datos = {'pymes' : response_pymes}

    if request.method == 'POST':

        response_productos = requests.post(url_api_productos, data=request.POST, files=request.FILES)

        if response_productos.status_code == status.HTTP_201_CREATED:
            datos['mensaje'] = "El producto fue agregado correctamente.."
        else:
            datos['error'] = "Se ha producido un error al agregar el producto. Verifica tus datos y reintenta."

        return render(request, "core/form-agregar-producto.html", datos)
    
    return render(request, "core/form-agregar-producto.html", datos)


# Vista de formulario para modificar productos
def form_modificar_producto(request, idProducto):

    url_api_lista_pymes = 'http://127.0.0.1:8000/api/pymes/lista/'
    url_api_productos = f'http://127.0.0.1:8000/api/productos/{idProducto}/'

    # Recuperamos los PYMEs
    response_pymes = requests.get(url_api_lista_pymes).json()
    response_producto = requests.get(url_api_productos).json()
    datos = {
        'pymes' : response_pymes,
        'producto' : response_producto,
        }

    if request.method == 'POST':

        if request.FILES:
            response_productos = requests.put(url_api_productos, data=request.POST, files=request.FILES)
        else:
            response_productos = requests.put(url_api_productos, data=request.POST)
       
        if response_productos.status_code == status.HTTP_202_ACCEPTED:

            # Si actualizó bien los datos, se recargan los atributos para que se vean modificados en la página
            response_producto = requests.get(url_api_productos).json()
            datos = {
                'pymes' : response_pymes,
                'producto' : response_producto,
                }

            datos['mensaje'] = "El producto fue modificado correctamente."
        else:
            datos['error'] = "Se ha producido un error al modificar el producto. Verifica tus datos y reintenta."

        return render(request, "core/form-modificar-producto.html", datos)

    return render(request, "core/form-modificar-producto.html", datos)


# Vista para eliminar productos
def form_eliminar_producto(request, idProducto):

    url_api = f'http://127.0.0.1:8000/api/productos/{idProducto}/'

    response = requests.delete(url_api)
    return redirect(to="/administracion_productos/")


# Vista de página para administración de categorías
def administracion_parametros(request):

    url_api = "http://127.0.0.1:8000/api/parametros/lista/"

    # Recuperamos los productos
    response = requests.get(url_api).json()
    datos = {'parametros': response}

    return render(request, 'core/administracion-parametros.html', datos)


# Vista de formulario para agregar categorías
def form_agregar_parametro(request):

    url_api = 'http://127.0.0.1:8000/api/parametros/'

    datos = {}

    if request.method == 'POST':

        response = requests.post(url_api, data=request.POST, files=request.FILES)

        if response.status_code == status.HTTP_201_CREATED:
            datos['mensaje'] = "El parámetro fue agregado correctamente.."
        else:
            datos['error'] = "Se ha producido un error al agregar el parámetro. Verifica tus datos y reintenta."

        return render(request, "core/form-agregar-parametro.html", datos)
    
    return render(request, "core/form-agregar-parametro.html", datos)


# Vista de formulario para modificar categorías
def form_modificar_parametro(request, codParametro):

    url_api = f'http://127.0.0.1:8000/api/parametros/{codParametro}/'

    response_parametro = requests.get(url_api).json()
    datos = {
        'parametro' : response_parametro,
        }

    if request.method == 'POST':

        response_parametros = requests.put(url_api, data=request.POST)
       
        if response_parametros.status_code == status.HTTP_202_ACCEPTED:

            # Si actualizó bien los datos, se recargan los atributos para que se vean modificados en la página
            response_parametro = requests.get(url_api).json()
            datos = {
                'parametro' : response_parametro,
                }

            datos['mensaje'] = "El parámetro fue modificado correctamente."
        else:
            datos['error'] = "Se ha producido un error al modificar el parámetro. Verifica tus datos y reintenta."

        return render(request, "core/form-modificar-parametro.html", datos)

    return render(request, "core/form-modificar-parametro.html", datos)


# Vista para eliminar categorías
def form_eliminar_parametro(request, codParametro):

    url_api = f'http://127.0.0.1:8000/api/parametros/{codParametro}/'
    response = requests.delete(url_api)

    datos = {}
    
    if response.status_code != status.HTTP_204_NO_CONTENT:
        datos['error'] = "Se ha producido un error al eliminar el parámetro."
    
    return redirect(to="/administracion_parametros/")


# Vista de página para administración de fundaciones
def administracion_pymes(request):

    url_api = 'http://127.0.0.1:8000/api/pymes/lista/'
    
    # Recuperamos los PYMEs
    response = requests.get(url_api).json()
    
    datos = {'pymes' : response}

    return render(request, 'core/administracion-pymes.html', datos)


# Vista de formulario para agregar PYMEs
def form_agregar_pyme(request):

    url_api = 'http://127.0.0.1:8000/api/pymes/'

    datos = {}

    if request.method == 'POST':

        response = requests.post(url_api, data=request.POST, files=request.FILES)

        if response.status_code == status.HTTP_201_CREATED:
            datos['mensaje'] = "La PYME fue agregada correctamente.."
        else:
            datos['error'] = "Se ha producido un error al agregar la PYME. Verifica tus datos y reintenta."

        return render(request, "core/form-agregar-pyme.html", datos)
    
    return render(request, "core/form-agregar-pyme.html", datos)


# Vista de formulario para modificar PYMEs
def form_modificar_pyme(request, idPyme):

    url_api = f'http://127.0.0.1:8000/api/pymes/{idPyme}/'

    response_pyme = requests.get(url_api).json()
    datos = {
        'pyme' : response_pyme,
        }

    if request.method == 'POST':

        if request.FILES:
            response_pymes = requests.put(url_api, data=request.POST, files=request.FILES)
        else:
            response_pymes = requests.put(url_api, data=request.POST)
       
        if response_pymes.status_code == status.HTTP_202_ACCEPTED:

            # Si actualizó bien los datos, se recargan los atributos para que se vean modificados en la página
            response_pyme = requests.get(url_api).json()
            datos = {
                'pyme' : response_pyme
                }

            datos['mensaje'] = "La PYME fue modificada correctamente."
        else:
            datos['error'] = "Se ha producido un error al modificar la PYME. Verifica tus datos y reintenta."

        return render(request, "core/form-modificar-pyme.html", datos)

    return render(request, "core/form-modificar-pyme.html", datos)


# Vista para eliminar PYMEs
def form_eliminar_pyme(request, idPyme):

    url_api = f'http://127.0.0.1:8000/api/pymes/{idPyme}/'

    response = requests.delete(url_api)
    return redirect(to="/administracion_pymes/")


# Vista de página para administración de contactos ingresados
def administracion_contactos(request):

    url_api = "http://127.0.0.1:8000/api/contactos/lista/"

    # Recuperamos los contactos
    response = requests.get(url_api).json()
    datos = {'contactos': response}

    return render(request, 'core/administracion-contactos.html', datos)


# Vista para eliminar contactos
def form_eliminar_contacto(request, idContacto):

    url_api = f'http://127.0.0.1:8000/api/contactos/{idContacto}/'

    response = requests.delete(url_api)
    return redirect(to="/administracion_contactos/")

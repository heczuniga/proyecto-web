
from django.shortcuts import render, redirect
from numpy import delete
from .models import Categoria
from .models import Producto
from .models import Fundacion
from .forms import ContactoForm
from .forms import ProductoForm
from .forms import FundacionForm

# Create your views here.

# Vista de página base
def index(request):

    return render(request, 'core/index.html')

# Vista de página de inicio
def inicio(request):
    
    return render(request, 'core/inicio.html')

# Vista de página de nosotros
def nosotros(request):
    
    return render(request, 'core/nosotros.html')

# Vista de página de contacto
def contacto(request):
    
    contactoForm = ContactoForm()

    datos = {
        'form': contactoForm
    }

    if request.method == 'POST':
        
        formulario = ContactoForm(request.POST)

        if formulario.is_valid:
            
            formulario.save()

            datos['mensaje'] = "Los datos del formulario se han recibido correctamente! Pronto nos comunicaremos contigo."
        
            return render(request, "core/contacto.html", datos)

    return render(request, "core/contacto.html", datos)

# Vista de página de donaciones
def donaciones(request):

    fundaciones = Fundacion.objects.all()
    datos = {
        'fundaciones': fundaciones

    }
    return render(request,'core/donaciones.html', datos)

# Vista de página de tienda
def tienda(request, categoria):

    # Recuperamos las categorías de un tipo específico agregando una columna que ayuda a manejar el active en el menú de categorías de productos
    categorias = Categoria.objects.extra(select={"active":"case codCategoria = " + str(categoria) + " when 1 then 'active' else '' end "}).all()

    # Recuperamos los productos de dicha categoría
    productos = Producto.objects.filter(categoria_id = categoria)
    datos = {'categorias': categorias,
             'productos': productos}

    return render(request, 'core/tienda.html', datos)

# Vista de página de tienda de bandanas
def tienda_bandanas(request):
    
    return render(request, 'core/tienda-bandanas.html')

# Vista de página de tienda de correas
def tienda_correas(request):
    
    return render(request, 'core/tienda-correas.html')

# Vista de página de tienda de intentificadores
def tienda_identificadores(request):
    
    return render(request, 'core/tienda-identificadores.html')

# Modulo administración productos
def administracion_productos(request):

    # Recuperamos los productos
    productos = Producto.objects.all().order_by('categoria').order_by('idProducto')
    datos = {'productos': productos}

    return render(request, 'core/administracion-productos.html', datos)

# Modulo administración fundaciones
def administracion_fundaciones(request):

    fundaciones = Fundacion.objects.all().order_by('idFundacion')
    datos = {'fundaciones' : fundaciones}

    return render(request, 'core/administracion-fundaciones.html', datos)

# Vista para eliminar productos
def form_eliminar_producto(request, idProducto):

    producto = Producto.objects.get(idProducto = idProducto)
    producto.delete()
    return redirect(to="administracion_productos")

# Vista para eliminar fundaciones
def form_eliminar_fundacion(request, idFundacion):

    fundacion = Fundacion.objects.get(idFundacion = idFundacion)
    fundacion.delete()
    return redirect(to="administracion_fundaciones")

def form_agregar_producto(request):

    productoForm = ProductoForm()

    datos = {
        'form': productoForm
    }

    if request.method == 'POST':
        
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid:
            
            formulario.save()

            datos['mensaje'] = "El producto ha sido agregado correctamente!"
        
            return render(request, "core/form-agregar-producto.html", datos)

    return render(request, "core/form-agregar-producto.html", datos)


def form_modificar_producto(request, idProducto):

    producto = Producto.objects.get(idProducto=idProducto)

    datos = {
        'form': ProductoForm(instance=producto),
        'idProducto': idProducto
    }

    if request.method == 'POST':

        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        
        if formulario.is_valid:
            
            formulario.save()

            datos['mensaje'] = "El producto ha sido modificado correctamente!"
        
            return render(request, "core/form-modificar-producto.html", datos)

    return render(request, "core/form-modificar-producto.html", datos)

def form_agregar_fundacion(request):

    fundacionForm = FundacionForm()

    datos = {
        'form': fundacionForm
    }

    if request.method == 'POST':
        
        formulario = FundacionForm(request.POST, request.FILES)

        if formulario.is_valid:
            
            formulario.save()

            datos['mensaje'] = "La fundación ha sido agregada correctamente!"
        
            return render(request, "core/form-agregar-fundacion.html", datos)

    return render(request, "core/form-agregar-fundacion.html", datos)


def form_modificar_fundacion(request, idFundacion):

    fundacion = Fundacion.objects.get(idFundacion=idFundacion)

    datos = {
        'form': FundacionForm(instance=fundacion),
        'idFundacion': idFundacion
    }

    if request.method == 'POST':

        formulario = FundacionForm(request.POST, request.FILES, instance=fundacion)
        
        if formulario.is_valid:
            
            formulario.save()

            datos['mensaje'] = "La fundación ha sido modificada correctamente!"
        
            return render(request, "core/form-modificar-fundacion.html", datos)

    return render(request, "core/form-modificar-fundacion.html", datos)

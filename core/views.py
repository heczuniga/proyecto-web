
from django.shortcuts import render, redirect
from numpy import delete
from .models import Categoria
from .models import Producto
from .forms import ContactoForm
from .models import Fundacion

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
    productos = Producto.objects.all()
    datos = {'productos': productos}

    return render(request, 'core/administracion-productos.html', datos)

# Modulo administración fundaciones
def administracion_fundaciones(request):

    fundaciones = Fundacion.objects.all()
    datos = {'fundaciones' : fundaciones}

    return render(request, 'core/administracion-fundaciones.html', datos)

# Vista para eliminar productos
def form_eliminar_producto(request, idProducto):

    producto = Producto.objects.get(idProducto = idProducto)
    producto.delete()
    return redirect(to="administracion_productos")



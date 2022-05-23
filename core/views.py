from django.shortcuts import render

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
    
    return render(request, 'core/contacto.html')

# Vista de página de donaciones
def donaciones(request):
    
    return render(request, 'core/donaciones.html')

# Vista de página de tienda
def tienda(request):
    
    return render(request, 'core/tienda.html')

# Vista de página de tienda de bandanas
def tienda_bandanas(request):
    
    return render(request, 'core/tienda-bandanas.html')

# Vista de página de tienda de correas
def tienda_correas(request):
    
    return render(request, 'core/tienda-correas.html')

# Vista de página de tienda de intentificadores
def tienda_identificadores(request):
    
    return render(request, 'core/tienda-identificadores.html')

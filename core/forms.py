
from django import forms
from django.forms import ModelForm
from .models import Contacto
from .models import Producto
from .models import Fundacion

# Creamos la clase para el formulario desde el modelo respectivo
class ContactoForm(ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombres", "apellidos", "celular", "correo", "direccion", "codRegion", "codComuna"]

# Creamos la clase para el formulario de productos
class ProductoForm(ModelForm):

    # La imagen de un producto es opcional
    imagen = forms.ImageField(required=False)
    
    class Meta:
        model = Producto
        fields = ["idProducto", "nombreCorto", "nombreLargo", "descripcion", "precio", "imagen", "categoria"]

# Creamos la clase para el formulario de fundaciones
class FundacionForm(ModelForm):

    # La imagen de un producto es opcional
    imagen = forms.ImageField(required=False)
    
    class Meta:
        model = Fundacion
        fields = ["idFundacion", "nombreCorto", "nombreLargo", "descripcion", "sitioWeb", "imagen"]

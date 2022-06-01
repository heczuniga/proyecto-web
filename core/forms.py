
from django import forms
from django.forms import ModelForm
from .models import Contacto

# Creamos la clase para el formulario desde el modelo respectivo
class ContactoForm(ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombres", "apellidos", "celular", "correo", "direccion", "codRegion", "codComuna"]


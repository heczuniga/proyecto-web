
from rest_framework import serializers
from api_rest.models import Producto
from api_rest.models import Contacto
from api_rest.models import Fundacion
from api_rest.models import Categoria
from django.forms import ValidationError
import requests

# Serializer de productos
class ProductoSerializer(serializers.ModelSerializer):

    categoria_desc = serializers.CharField(source='categoria.nombreCategoria', read_only=True)
    
    class Meta:
        model = Producto
        fields = "__all__"


# Serializer de contactos
class ContactoSerializer(serializers.ModelSerializer):

    nombreComuna = serializers.CharField(source='codComuna.nomComuna', read_only=True)
    nombreRegion = serializers.CharField(source='codRegion.nomRegion', read_only=True)

    class Meta:
        model = Contacto
        fields = "__all__"


# Serializer de fundaciones
class FundacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fundacion
        fields = "__all__"


# Serializer de categorias
class CategoriaSerializer(serializers.ModelSerializer):

    total_productos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Categoria
        fields = "__all__"

    # Recuperamos el total de productos de cada categoría que es un dato importante para armar algunas vistas
    def get_total_productos(self, data):
        
        url_api = f'http://127.0.0.1:8000/api/productos/categoria/{data.codCategoria}/'
        response = requests.get(url_api).json()

        total_productos = len(response)
        datos = {
            'total_productos' : total_productos,
        }

        return datos['total_productos']

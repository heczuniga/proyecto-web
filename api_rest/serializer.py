
from rest_framework import serializers
from api_rest.models import Producto
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


# Serializer de fundaciones
class FundacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fundacion
        fields = "__all__"


# Serializer de categorias
class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = "__all__"

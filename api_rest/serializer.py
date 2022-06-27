
from rest_framework import serializers
from core.models import Producto
from core.models import Contacto
from core.models import Fundacion
from core.models import Categoria
from django.forms import ValidationError


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

    class Meta:
        model = Categoria
        fields = "__all__"



from rest_framework import serializers
from api_rest.models import Producto
from api_rest.models import Pyme
from api_rest.models import Parametro
from django.forms import ValidationError
import requests

# Serializer de productos
class ProductoSerializer(serializers.ModelSerializer):

    nombrePyme = serializers.CharField(source='pyme.nombreCorto', read_only=True)
    
    class Meta:
        model = Producto
        fields = "__all__"


# Serializer de PYMEs
class PymeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pyme
        fields = "__all__"


# Serializer de categorias
class ParametroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parametro
        fields = "__all__"

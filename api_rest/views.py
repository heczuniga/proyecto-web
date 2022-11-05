from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from api_rest.models import Producto
from api_rest.models import Fundacion
from api_rest.models import Parametro
from api_rest.serializer import ProductoSerializer
from api_rest.serializer import FundacionSerializer
from api_rest.serializer import ParametroSerializer
from rest_framework import status
from rest_framework import serializers

# API's relacionadas con productos
class ListaProductos(APIView):
    
    # # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
        
    def get(self, request):
        order_by = ['nombreCorto']
        productos = Producto.objects.all().order_by(*order_by)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class CrearProducto(APIView):

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Productos(APIView):
    
    def get_producto_by_id(self, idProducto):
        try:
            return Producto.objects.get(idProducto=idProducto)
        except:
            producto = Producto()
            producto.nombreCorto = "Producto no existente"
            return producto
    
    def get(self, request, idProducto):
        producto = self.get_producto_by_id(idProducto)
        
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self, request, idProducto):
        producto = self.get_producto_by_id(idProducto)
        serializer = ProductoSerializer(producto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idProducto):
        producto = self.get_producto_by_id(idProducto)
        
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API's relacionadas con fundaciones
class ListaFundaciones(APIView):
    
    def get(self, request):
        order_by = ['nombreCorto']
        fundaciones = Fundacion.objects.all().order_by(*order_by)
        serializer = FundacionSerializer(fundaciones, many=True)
        return Response(serializer.data)


class CrearFundacion(APIView):

    def post(self, request):
        serializer = FundacionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Fundaciones(APIView):
    
    def get_fundacion_by_id(self, idFundacion):
        try:
            return Fundacion.objects.get(idFundacion=idFundacion)
        except:
            fundacion = Fundacion()
            fundacion.nombreCorto = "Fundación no existente"
            return fundacion
    
    def get(self, request, idFundacion):
        fundacion = self.get_fundacion_by_id(idFundacion)
        
        serializer = FundacionSerializer(fundacion)
        return Response(serializer.data)
    
    def put(self, request, idFundacion):
        fundacion = self.get_fundacion_by_id(idFundacion)
        serializer = FundacionSerializer(fundacion, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idFundacion):
        fundacion = self.get_fundacion_by_id(idFundacion)
        
        fundacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API's relacionadas con los parámetros del sistema
class ListaParametros(APIView):

    def get(self, request):
        # Recuperamos los parámetros
        order_by = ['codParametro']
        parametros = Parametro.objects.all()

        serializer = ParametroSerializer(parametros, many=True)

        return Response(serializer.data)


class CrearParametro(APIView):

    def post(self, request):
        serializer = ParametroSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Parametros(APIView):
    
    def get_parametro_by_id(self, codParametro):
        try:
            return Parametro.objects.get(codParametro=codParametro)
        except:
            parametro = Parametro()
            parametro.nombreParametro = "Parámetro no existente"
            return parametro
    
    def get(self, request, codParametro):
        parametro = self.get_parametro_by_id(codParametro)
        
        serializer = ParametroSerializer(parametro)
        return Response(serializer.data)
    
    def put(self, request, codParametro):
        parametro = self.get_parametro_by_id(codParametro)
        serializer = ParametroSerializer(parametro, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, codParametro):
        parametro = self.get_parametro_by_id(codParametro)
        
        parametro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

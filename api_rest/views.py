from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Producto
from core.models import Contacto
from core.models import Fundacion
from core.models import Categoria
from api_rest.serializer import ProductoSerializer
from api_rest.serializer import ContactoSerializer
from api_rest.serializer import FundacionSerializer
from api_rest.serializer import CategoriaSerializer
from rest_framework import status
from rest_framework import serializers

# API's relacionadas con productos
class ListaProductos(APIView):
    
    def get(self, request):
        order_by = ['categoria','nombreCorto']
        productos = Producto.objects.all().order_by(*order_by)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class ListaProductosCategoria(APIView):
    
    def get(self, request, codCategoria):
        order_by = ['nombreCorto']
        productos = Producto.objects.filter(categoria_id = codCategoria).order_by(*order_by)
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

# API's relacionadas con contactos
class ListaContactos(APIView):
    
    def get(self, request):
        order_by = ['idContacto']
        contactos = Contacto.objects.all().order_by(*order_by)
        serializer = ContactoSerializer(contactos, many=True)
        return Response(serializer.data)

class CrearContacto(APIView):

    def post(self, request):
        serializer = ContactoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Contactos(APIView):
    
    def get_contacto_by_id(self, idContacto):
        try:
            return Contacto.objects.get(idContacto=idContacto)
        except:
            contacto = Contacto()
            contacto.nombres = "Contacto no existente"
            return contacto
    
    def get(self, request, idContacto):
        contacto = self.get_contacto_by_id(idContacto)
        
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)
    
    def put(self, request, idContacto):
        contacto = self.get_contacto_by_id(idContacto)
        serializer = ContactoSerializer(contacto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idContacto):
        contacto = self.get_contacto_by_id(idContacto)
        
        contacto.delete()
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


# API's relacionadas con categorías de productos
class ListaCategorias(APIView):

    def get(self, request):
        # Recuperamos las categorías
        order_by = ['codCategoria']
        categorias = Categoria.objects.all().extra(select={'total_productos': '(select count(idProducto) from core_producto where categoria_id = codCategoria)'})

        print(categorias)

        serializer = CategoriaSerializer(categorias, many=True)

        print(serializer)

        return Response(serializer.data)


class CrearCategoria(APIView):

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Categorias(APIView):
    
    def get_categoria_by_id(self, codCategoria):
        try:
            return Categoria.objects.get(codCategoria=codCategoria)
        except:
            categoria = Categoria()
            categoria.nombreCategoria = "Categoría no existente"
            return categoria
    
    def get(self, request, codCategoria):
        categoria = self.get_categoria_by_id(codCategoria)
        
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def put(self, request, codCategoria):
        categoria = self.get_categoria_by_id(codCategoria)
        serializer = CategoriaSerializer(categoria, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, codCategoria):
        categoria = self.get_categoria_by_id(codCategoria)
        
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

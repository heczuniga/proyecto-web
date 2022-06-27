
from django.db import models

# Modelos del sistema
class Region(models.Model):
    codRegion = models.CharField(primary_key=True, max_length=2, verbose_name="Código de la región")
    nomRegion = models.CharField(max_length=100, verbose_name="Nombre de la región")
    
    def __str__(self) -> str:
        return self.nomRegion
    
class Comuna(models.Model):
    codComuna = models.CharField(primary_key=True, max_length=5, verbose_name="Código de la comuna")
    nomComuna = models.CharField(max_length=100, verbose_name="Nombre de la comuna")
    codRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nomComuna
    
class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True, verbose_name="Identificador del contacto")
    nombres = models.CharField(max_length=100, verbose_name="Nombres (*)")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos (*)")
    celular = models.PositiveIntegerField(verbose_name="Celular (*)")
    correo = models.CharField(max_length=100, verbose_name="Correo electrónico (*)")
    direccion = models.CharField(max_length=250, verbose_name="Dirección (*)")
    codRegion = models.ForeignKey(Region, on_delete=models.RESTRICT, verbose_name="Región (*)")
    codComuna = models.ForeignKey(Comuna, on_delete=models.RESTRICT, verbose_name="Comuna (*)")
    
    def __str__(self) -> str:
        return self.idContacto

class Categoria(models.Model):
    codCategoria = models.IntegerField(primary_key=True, verbose_name="Código de la categoría")
    nombreCategoria = models.CharField(max_length=50, null=False, verbose_name="Nombre de la categoría")

    def __str__(self) -> str:
        return self.nombreCategoria
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Identificador del producto (*)")
    nombreCorto = models.CharField(max_length=100, null=False, verbose_name="Nombre corto del producto (*)")
    nombreLargo = models.CharField(max_length=200, null=False, verbose_name="Nombre largo del producto (*)")
    descripcion = models.TextField(max_length=1000, null=False, verbose_name="Descripción del producto (*)")
    precio = models.IntegerField(null=False, verbose_name="Precio del producto (*)")
    imagen = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen del producto (*)")
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, verbose_name="Categoria del producto (*)")
    
    def __str__(self) -> str:
        return self.nombreCorto

class Fundacion(models.Model):
    idFundacion = models.AutoField(primary_key=True, verbose_name="Identificador de la fundación")
    nombreCorto = models.CharField(max_length=100, null=False, verbose_name="Nombre corto de la fundación")
    nombreLargo = models.CharField(max_length=200, null=False, verbose_name="Nombre largo de la fundación")
    descripcion = models.TextField(max_length=1000, null=False, verbose_name="Descripción de la fundación")
    sitioWeb = models.CharField(max_length=200, null=True, verbose_name="Sitio web de la fundación")
    imagen = models.ImageField(upload_to="fundaciones", null=True, blank=True, verbose_name="Imagen de la fundación")

    def __str__(self) -> str:
        return self.nombreCorto


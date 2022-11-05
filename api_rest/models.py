from django.db import models

# Modelos del sistema
class Parametro(models.Model):
    codParametro = models.IntegerField(primary_key=True, verbose_name="Código del parámetro")
    nombreParametro = models.CharField(max_length=50, null=False, verbose_name="Nombre del parámetro")
    valor = models.CharField(max_length=10, null=False, verbose_name="Valor del parámetro")

    def __str__(self) -> str:
        return self.nombreParametro

class Pyme(models.Model):
    idPyme = models.AutoField(primary_key=True, verbose_name="Identificador de la PYME")
    nombreCorto = models.CharField(max_length=100, null=False, verbose_name="Nombre corto de la PYME")
    nombreLargo = models.CharField(max_length=200, null=False, verbose_name="Nombre largo de la PYME")
    descripcion = models.TextField(max_length=1000, null=False, verbose_name="Descripción de la PYME")
    sitioWeb = models.CharField(max_length=200, null=True, verbose_name="Sitio web de la PYME")
    imagen = models.ImageField(upload_to="pymes", null=True, blank=True, verbose_name="Imagen de la PYME")

    def __str__(self) -> str:
        return self.nombreCorto
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Identificador del producto (*)")
    nombreCorto = models.CharField(max_length=100, null=False, verbose_name="Nombre corto del producto (*)")
    nombreLargo = models.CharField(max_length=200, null=False, verbose_name="Nombre largo del producto (*)")
    descripcion = models.TextField(max_length=1000, null=False, verbose_name="Descripción del producto (*)")
    precio = models.IntegerField(null=False, verbose_name="Precio del producto (*)")
    imagen = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen del producto (*)")
    pyme = models.ForeignKey(Pyme, on_delete=models.RESTRICT, verbose_name="PYME que vende el producto (*)")
    
    def __str__(self) -> str:
        return self.nombreCorto


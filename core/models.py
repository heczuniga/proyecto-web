
from pydoc import visiblename
from django.db import models

# Create your models here.

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
    idContacto = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres (*)")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos (*)")
    celular = models.IntegerField(verbose_name="Celular (*)")
    correo = models.CharField(max_length=100, verbose_name="Correo electrónico (*)")
    direccion = models.CharField(max_length=250, verbose_name="Dirección (*)")
    codRegion = models.ForeignKey(Region, on_delete=models.RESTRICT, verbose_name="Región (*)")
    codComuna = models.ForeignKey(Comuna, on_delete=models.RESTRICT, verbose_name="Comuna (*)")
    
    def __str__(self) -> str:
        return self.idContacto

from django.contrib import admin
from api_rest.models import Parametro
from api_rest.models import Producto
from api_rest.models import Fundacion

# Register your models here.
admin.site.register(Parametro)
admin.site.register(Producto)
admin.site.register(Fundacion)

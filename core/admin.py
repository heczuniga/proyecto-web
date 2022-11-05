from django.contrib import admin
from api_rest.models import Region
from api_rest.models import Comuna
from api_rest.models import Contacto
from api_rest.models import Categoria
from api_rest.models import Producto
from api_rest.models import Fundacion

# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Contacto)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Fundacion)

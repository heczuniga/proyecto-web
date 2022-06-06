from django.contrib import admin
from .models import Region
from .models import Comuna
from .models import Contacto
from .models import Categoria
from .models import Producto

# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Contacto)
admin.site.register(Categoria)
admin.site.register(Producto)

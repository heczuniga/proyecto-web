from django.contrib import admin
from .models import Region
from .models import Comuna
from .models import Contacto


# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Contacto)

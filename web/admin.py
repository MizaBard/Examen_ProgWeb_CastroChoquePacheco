from django.contrib import admin
from .models import Producto, Boleta, detalle_boleta, Contacto

# Register your models here.

admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)
admin.site.register(Contacto)

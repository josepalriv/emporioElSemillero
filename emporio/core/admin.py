from django.contrib import admin
from .models import Categoria, Presentacion, Producto
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Presentacion)
admin.site.register(Producto)
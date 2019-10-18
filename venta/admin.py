from django.contrib import admin

# Register your models here.
from . models import Producto, Tipo

admin.site.register(Producto)
admin.site.register(Tipo)
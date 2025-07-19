from django.contrib import admin
from .models import Pedido, Plato

# Register your models here.
admin.site.register(Plato)
admin.site.register(Pedido)
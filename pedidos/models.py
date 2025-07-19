from django.db import models

# Create your models here.
class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    platos = models.ManyToManyField(Plato)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.fecha_pedido.strftime('%Y-%m-%d %H:%M:%S')}"

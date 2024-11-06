from django.db import models
from productos.models import Producto

# Create your models here.
class Oferta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje_descuento =models.DecimalField(max_digits=6, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f" oferta en: {self.producto} --- Descuento: {self.porcentaje_descuento} %"

    @property
    def precio_descuento(self):
        return self.producto.precio - (self.producto.precio * self.porcentaje_descuento / 100)
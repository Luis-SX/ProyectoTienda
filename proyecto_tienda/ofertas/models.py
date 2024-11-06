from django.db import models
from django.forms import ValidationError
from productos.models import Producto

# Create your models here.
class Oferta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje_descuento =models.DecimalField(max_digits=6, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def clean(self):   #metodo especial para validaciones personalizadas
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError('La fecha de inicio debe ser menor que la fecha de fin')
        if self.porcentaje_descuento < 0 or self.porcentaje_descuento > 100:
            raise ValidationError('El porcentaje de descuento debe estar entre 0 y 100')

    def save(self, *args, **kwargs):    #invoca a Clean antes de guardar los datos
        self.clean()
        super(Oferta, self).save(*args, **kwargs)

    def __str__(self):
        return f" oferta en: {self.producto} --- Descuento: {self.porcentaje_descuento} %"

    @property
    def precio_descuento(self):
        return self.producto.precio - (self.producto.precio * self.porcentaje_descuento / 100)
from django.db import models
from Coche.models import Coche  
from Vendedor.models import Vendedor  

class VentaCoche(models.Model):
    coche_vendido = models.ForeignKey(Coche, on_delete=models.CASCADE)  
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)  
    fecha_venta = models.DateField()  
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"Venta de Coche {self.id}: Coche {self.coche_vendido}, Vendedor {self.vendedor}, Fecha {self.fecha_venta}, Precio {self.precio_venta}"

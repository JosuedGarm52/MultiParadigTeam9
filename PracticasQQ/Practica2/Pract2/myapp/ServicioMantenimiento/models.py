from django.db import models
from Coche.models import Coche

# Create your models here.
class ServicioMantenimiento(models.Model):
    TIPOS_DE_SERVICIO = (
        ('cambio_aceite', 'Cambio de Aceite'),
        ('revision_frenos', 'Revisión de Frenos'),
        ('otros', 'Otros'),
    )

    tipo_servicio = models.CharField(max_length=50, choices=TIPOS_DE_SERVICIO)  
    fecha_servicio = models.DateField()  
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2)  
    descripcion_servicio = models.TextField() 
    vehiculo = models.ForeignKey(Coche, on_delete=models.CASCADE)  

    def __str__(self):
        return f"Servicio de Mantenimiento {self.id}: Tipo - {self.get_tipo_servicio_display()}, Fecha - {self.fecha_servicio}, Costo - {self.costo_servicio}, Vehículo - {self.vehiculo}"
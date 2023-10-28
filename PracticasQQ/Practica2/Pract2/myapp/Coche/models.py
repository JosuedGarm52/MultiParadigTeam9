from django.db import models
from Conductor.models import Conductor
from MarcaCoche.models import MarcaCoche

# Create your models here.
class Coche(models.Model):
    marca = models.ForeignKey(MarcaCoche, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100) 
    year_fabricacion = models.PositiveIntegerField()  
    numeroplaca = models.CharField(max_length=20)  
    color = models.CharField(max_length=50)  
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Coche {self.id}: {self.marca} {self.modelo}, Año {self.year_fabricacion}, Placa {self.numeroplaca} dueño: {self.conductor.nombre}"
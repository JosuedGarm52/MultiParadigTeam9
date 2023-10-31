from django.db import models

# Create your models here.
class MarcaCoche(models.Model):
    nombre = models.CharField(max_length=100)
    paisorigen = models.CharField(max_length=100)  
    year_fundacion = models.PositiveIntegerField() 

    def __str__(self):
        return f"Marca de Coche: {self.nombre}, País de Origen: {self.paisorigen}, Año de Fundación: {self.year_fundacion}"

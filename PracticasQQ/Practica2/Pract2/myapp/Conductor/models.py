from django.db import models

# Create your models here.
class Conductor(models.Model):
    nombre = models.CharField(max_length=100)  
    clave_licencia = models.CharField(max_length=20)  
    edad = models.PositiveIntegerField()  
    direccion = models.CharField(max_length=200)  

    def __str__(self):
        return f"Conductor {self.id}: Nombre {self.nombre}, Clave de la licencia {self.clave_licencia}, Edad {self.edad}, Dirección {self.direccion}"
        
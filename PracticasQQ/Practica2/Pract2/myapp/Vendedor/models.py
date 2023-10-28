from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)  
    correo = models.EmailField(max_length=255)  
    telefono = models.CharField(max_length=20)  
    direccion = models.CharField(max_length=200)  

    def __str__(self):
        return f"Vendedor {self.id}: Nombre - {self.nombre}, Correo - {self.correo}, Teléfono - {self.telefono}, Dirección - {self.direccion}"
from django.db import models

# Create your models here.


class Estacion(models.Model):
    puesto = models.CharField(max_length=25)
    pais = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"puesto: {self.puesto}, pais: {self.pais}, ciudad: {self.ciudad}"
    
class Equipo(models.Model):
    turno = models.CharField(max_length=25)
    nombre = models.CharField(max_length=255)
    #  = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"turno: {self.turno}, nombre: {self.nombre}"


class Bombero(models.Model):
    nombre = models.CharField(max_length=255)
    no_empleado = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"nombre: {self.nombre}, no_empleado: {self.no_empleado}"

class Camion(models.Model):
    nombre = models.CharField(max_length=255)
    niv = models.IntegerField()
    estacion = models.ForeignKey(Estacion, on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"nombre: {self.nombre}, niv: {self.niv}"


class PerroBombero(models.Model):
    nombre = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    edad = models.IntegerField()
    estacion = models.ForeignKey(Estacion, on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"nombre: {self.nombre}, raza: {self.raza}, edad: {self.edad}"



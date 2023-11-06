from logger_base import log 
from datetime import date

class Animal: 
    def __init__(self,id=None,raza=None,fecha_ingreso = None,fecha_salida = None) -> None:
        #python si uno tiene un valor por defecto, todos deben tener ese valor por defecto
        self._id = id
        self._raza = raza
        self._fecha_ingreso = fecha_ingreso
        self._fecha_salida = fecha_salida

    def __str__(self) -> str:
        return f"""
            ID ANIMAL {self._id}, Raza: {self._raza},
            Fecha de ingreso: {self._fecha_ingreso}, Fecha de salida: {self._fecha_salida}
        """
    
    @property
    def idAnimal(self):
        return self._id
    @idAnimal.setter
    def idAnimal(self, id):
        self._id = id
    
    @property
    def Raza(self):
        return self._raza
    @Raza.setter
    def Raza(self, raza):
        self._raza = raza
    
    @property
    def FechaIngreso(self):
        return self._fecha_ingreso
    @FechaIngreso.setter
    def FechaIngreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    @property
    def FechaSalida(self):
        return self._fecha_salida
    @FechaSalida.setter
    def FechaSalida(self, fecha_salida):
        self._fecha_salida = fecha_salida

if __name__ == "__main__":
    objeto1 = Animal(1,"Boxer",date(2023, 11, 6),date(2023, 11, 7))
    print(objeto1)
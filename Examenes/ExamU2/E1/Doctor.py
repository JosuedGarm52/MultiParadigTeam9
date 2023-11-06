from logger_base import log 

class Doctor: 
    def __init__(self,id=None,nombre=None,num_telef = None) -> None:
        #python si uno tiene un valor por defecto, todos deben tener ese valor por defecto
        self._id = id
        self._nombre = nombre
        self._num_telef = num_telef

    def __str__(self) -> str:
        return f"""
            ID DOCTOR {self._id}, 
            Nombre: {self._nombre},
            Numero de telefono: {self._num_telef}
        """
    
    @property
    def idDoctor(self):
        return self._id
    @idDoctor.setter
    def idDoctor(self, id):
        self._id = id
    
    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def NumTelef(self):
        return self._num_telef
    @NumTelef.setter
    def NumTelef(self, num__num_telef):
        self._num_telef = num__num_telef


if __name__ == "__main__":
    objeto1 = Doctor(1,"Juan","7171578")
    print(objeto1)
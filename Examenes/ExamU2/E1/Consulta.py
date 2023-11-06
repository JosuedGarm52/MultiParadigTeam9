from logger_base import log 

class Consulta: 
    def __init__(self,id_animal=None,id_doctor =None,servicio = None,costo = None) -> None:
        #python si uno tiene un valor por defecto, todos deben tener ese valor por defecto
        self._id_animal = id_animal
        self._id_doctor = id_doctor
        self._servicio = servicio
        self._costo = costo

    def __str__(self) -> str:
        return f"""
            ID ANIMAL {self._id_animal}, 
            ID DOCTOR {self._id_doctor}, 
            Servicio: {self._servicio}, Costo: {self._costo}
        """
    
    @property
    def idAnimal(self):
        return self._id_animal
    @idAnimal.setter
    def idAnimal(self, id):
        self._id_animal = id

    @property
    def idDoctor(self):
        return self._id_doctor
    @idDoctor.setter
    def idDoctor(self, id):
        self._id_doctor = id
    
    @property
    def Servicio(self):
        return self._servicio
    @Servicio.setter
    def Servicio(self, servicio):
        self._servicio = servicio

    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo(self, costo):
        self._costo = costo

if __name__ == "__main__":
    objeto1 = Consulta(1,1,"Diagnostico cancer",220.00)
    print(objeto1)
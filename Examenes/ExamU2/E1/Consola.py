from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log
from Animal import Animal
from Doctor import Doctor
from Consulta import Consulta
from AnimalDAO import AnimalDAO
from DoctorDao import DoctorDAO
from ConsultaDao import ConsultaDAO

class Consola:
    _Query1 = ""
    _Query2 = "INSERT INTO consulta (id_animal, id_doctor, servicio, costo) VALUES(%s,%s,%s,%s)"
    _Query3 = ""
    _Query4 = ""
    _Query5 = ""
    _Query6 = ""

    @classmethod
    def Query2(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.idAnimal, consulta.idDoctor, consulta.Servicio, consulta.Costo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

if __name__ == "__main__":
    objeto1 = Consulta(id_animal=1,id_doctor=1,servicio='consulta resfriado', costo= 530.69)

    personas = ConsultaDao().seleccionar()
    for p in personas:
        log.debug(p)
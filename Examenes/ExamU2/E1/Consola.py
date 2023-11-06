from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log
from Animal import Animal
from Doctor import Doctor
from Consulta import Consulta
from datetime import date

class Consola:
    _Query1 = "SELECT COUNT(*) FROM consulta JOIN animal ON consulta.id_animal = animal.id WHERE consulta.id_doctor = %s AND animal.fecha_ingreso = %s GROUP BY consulta.id_doctor, animal.fecha_ingreso HAVING COUNT(*) < 2 "
    _Query2 = "INSERT INTO consulta (id_animal, id_doctor, servicio, costo) VALUES(%s,%s,%s,%s)"
    _Query3 = "SELECT SUM(consulta.costo) FROM consulta JOIN animal ON consulta.id_animal = animal.id WHERE animal.fecha_ingreso = (SELECT fecha_ingreso FROM animal WHERE id = consulta.id_animal) - INTERVAL '1 day' "
    _Query4 = ""
    _Query5 = ""
    _Query6 = ""

    @classmethod
    def Query1(cls,consulta,animal):
        with CursorDelPool() as cursor:
            valores = (consulta.idDoctor, animal.FechaIngreso)
            cursor.execute(cls._Query2, valores)
            return cursor.rowcount

    @classmethod
    def Query2(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.idAnimal, consulta.idDoctor, consulta.Servicio, consulta.Costo)
            cursor.execute(cls._Query2, valores)
            return cursor.rowcount
        
    @classmethod
    def query3(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            consulta = []
            for r in registros:
                consulta.append(Consulta(r[0]))
            return consulta

if __name__ == "__main__":
    animal1 = Animal(fecha_ingreso= date(2023,11,7))
    consulta1 = Consulta(id_doctor=1)
    query1 = Consola.Query2(consulta1,animal1)
    log.debug(f"Personas agregadas: {query1}")
    objeto2 = Consulta(id_animal=1,id_doctor=1,servicio='consulta resfriado', costo= 530.69)
    query2 = Consola.Query2(objeto2)
    log.debug(f"Personas agregadas: {query2}")
    query3 = Consola().seleccionar()
    for p in query3:
        log.debug(p)
    
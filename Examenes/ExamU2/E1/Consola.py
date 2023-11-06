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
    _Query4 = "SELECT doctor.id, doctor.nombre FROM doctor LEFT JOIN consulta ON doctor.id = consulta.id_doctor WHERE consulta.id_doctor IS NULL "
    _Query6 = """
    SELECT 
    animal.id AS animal_id,
    animal.raza AS animal_raza,
    animal.fecha_ingreso AS animal_fecha_ingreso,
    animal.fecha_salida AS animal_fecha_salida,
    doctor.id AS doctor_id,
    doctor.nombre AS doctor_nombre,
    doctor.num_telef AS doctor_telefono,
    consulta.servicio,
    consulta.costo
    FROM 
        consulta
    JOIN animal ON consulta.id_animal = animal.id
    JOIN doctor ON consulta.id_doctor = doctor.id
    WHERE animal.id = %s
    """
    _Query5 = """
    SELECT 
    animal.id AS animal_id,
    animal.raza AS animal_raza,
    animal.fecha_ingreso AS animal_fecha_ingreso,
    animal.fecha_salida AS animal_fecha_salida,
    doctor.id AS doctor_id,
    doctor.nombre AS doctor_nombre,
    doctor.num_telef AS doctor_telefono,
    consulta.servicio,
    consulta.costo
    FROM 
    consulta
    JOIN animal ON consulta.id_animal = animal.id
    JOIN doctor ON consulta.id_doctor = doctor.id;
    """

    @classmethod
    def Query1(cls,consulta,animal):
        with CursorDelPool() as cursor:
            valores = (consulta.idDoctor, animal.FechaIngreso)
            cursor.execute(cls._Query1, valores)
            return cursor.rowcount

    @classmethod
    def Query2(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.idAnimal, consulta.idDoctor, consulta.Servicio, consulta.Costo)
            cursor.execute(cls._Query2, valores)
            return cursor.rowcount
        
    @classmethod
    def Query3(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Query3)
            registros=cursor.fetchall()
            consulta = []
            for r in registros:
                consulta.append(Consulta(r[0]))
            return consulta
        
    @classmethod
    def Query4(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Query4)
            registros=cursor.fetchall()
            consulta = []
            for r in registros:
                consulta.append(Consulta(r[0]),r[1])
            return consulta
    @classmethod
    def Query5(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Query5)
            registros=cursor.fetchall()
            consulta = []
            for r in registros:
                consulta.append(Consulta(r[0]),r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8])
            return consulta
    @classmethod
    def Query6(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.id,)
            cursor.execute(cls._Query6, valores)
            return cursor.rowcount

if __name__ == "__main__":
    animal1 = Animal(fecha_ingreso= date(2023,11,7))
    consulta1 = Consulta(id_doctor=1)
    query1 = Consola.Query1(consulta1,animal1)
    log.debug(f"Personas agregadas: {query1}")
    objeto2 = Consulta(id_animal=1,id_doctor=1,servicio='consulta resfriado', costo= 530.69)
    query2 = Consola.Query2(objeto2)
    log.debug(f"Personas agregadas: {query2}")
    query3 = Consola().Query3()
    for p in query3:
        log.debug(p)
    query4 = Consola().Query4()
    for p in query4:
        log.debug(p)

    query5 = Consola().Query6()
    for p in query5:
        log.debug(p)

    animal2 = Animal(id=1)
    query6 = Consola.Query6(animal1)
    log.debug(f"Personas agregadas: {query6}")
from Doctor import Doctor
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class DoctorDao:
    _SELECCIONAR = "SELECT id, nombre, num_telef FROM doctor ORDER BY id"
    _INSERTAR = "INSERT INTO doctor (nombre, num_telef) VALUES(%s,%s)"
    _ACTUALIZAR = "UPDATE doctor SET nombre = %s,num_telef=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM doctor WHERE id = %s" 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            doctor = []
            for r in registros:
                doctor.append(Doctor(r[0],r[1],r[2]))
            return doctor
    @classmethod
    def insertar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.NumTelef)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.NumTelef,doctor.idDoctor)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.idDoctor,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    objeto1 = Doctor(nombre="Juan",num_telef="787492")
    insercion = DoctorDao.insertar(objeto1)
    log.debug(f"Personas agregadas: {insercion}")
    objeto1.idDoctor = 2
    objeto1.NumTelef = "717-187-4492"
    actualizacion = DoctorDao.actualizar(objeto1)
    log.debug(f"Personas Actualizadas: {actualizacion}")
    eliminacion = DoctorDao.eliminar(objeto1)
    objeto1.idDoctor = 3
    log.debug(f"Personas Eliminadas: {eliminacion}")
    personas = DoctorDao().seleccionar()
    for p in personas:
        log.debug(p)

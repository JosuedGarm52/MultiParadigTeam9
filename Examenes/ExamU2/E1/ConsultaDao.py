from Consulta import Consulta
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class ConsultaDao:
    _SELECCIONAR = "select id_animal, id_doctor, servicio, costo from consulta ORDER BY id_animal, id_doctor"
    _INSERTAR = "INSERT INTO consulta (id_animal, id_doctor, servicio, costo) VALUES(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE consulta SET servicio = %s, costo=%s WHERE id_animal = %s AND id_doctor = %s"
    _ELIMINAR = "DELETE FROM consulta WHERE id_animal = %s AND id_doctor = %s" 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            consulta = []
            for r in registros:
                consulta.append(Consulta(r[0],r[1],r[2],r[3]))
            return consulta
    @classmethod
    def insertar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.idAnimal, consulta.idDoctor, consulta.Servicio, consulta.Costo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.Servicio, consulta.Costo, consulta.idAnimal, consulta.idDoctor)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.idAnimal, consulta.idDoctor,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    objeto1 = Consulta(id_animal=1,id_doctor=1,servicio='consulta contra cancer de mama', costo= 530.69)
    insercion = ConsultaDao.insertar(objeto1)
    log.debug(f"Personas agregadas: {insercion}")
    objeto2 = Consulta(id_animal=2,id_doctor=1,servicio='consulta contra cancer de mama', costo= 530.69)
    insercion = ConsultaDao.insertar(objeto2)
    log.debug(f"Personas agregadas: {insercion}")
    objeto2.idAnimal = 1
    actualizacion = ConsultaDao.actualizar(objeto1)
    log.debug(f"Personas Actualizadas: {actualizacion}")
    objeto2.idAnimal = 2
    eliminacion = ConsultaDao.eliminar(objeto2)
    log.debug(f"Personas Eliminadas: {eliminacion}")
    personas = ConsultaDao().seleccionar()
    for p in personas:
        log.debug(p)

from Plantilla import Plantilla
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class PlantillaDao:
    _SELECCIONAR = "SELECT id_persona, nombre, apellido, email, telefono FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona (nombre, apellido, email, telefono) VALUES(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s,apellido=%s, email = %s, telefono = %s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona = %s" 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            plantilla = []
            for r in registros:
                plantilla.append(Plantilla(r[0],r[1],r[2],r[3],r[4]))
            return plantilla
    @classmethod
    def insertar(cls,plantilla):
        with CursorDelPool() as cursor:
            valores = (plantilla.Nombre, plantilla.Apellido, plantilla.Email, plantilla.Telefono)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,plantilla):
        with CursorDelPool() as cursor:
            valores = (plantilla.Nombre, plantilla.Apellido,plantilla.Email,plantilla.Telefono,plantilla.idPersona)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,plantilla):
        with CursorDelPool() as cursor:
            valores = (plantilla.idPersona,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    objeto1 = Plantilla(nombre="Juan",apellido="Perez",email="dg@gmail.com",telefono="787492")
    insercion = PlantillaDao.insertar(objeto1)
    log.debug(f"Personas agregadas: {insercion}")
    objeto1.idPersona = 2
    actualizacion = PlantillaDao.actualizar(objeto1)
    log.debug(f"Personas Actualizadas: {actualizacion}")
    eliminacion = PlantillaDao.eliminar(objeto1)
    log.debug(f"Personas Eliminadas: {eliminacion}")
    personas = PlantillaDao().seleccionar()
    for p in personas:
        log.debug(p)

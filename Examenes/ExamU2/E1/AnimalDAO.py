from Animal import Animal
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 
from datetime import date

class AnimalDao:
    _SELECCIONAR = "select id, raza, fecha_ingreso, fecha_salida from animal order by id"
    _INSERTAR = "INSERT INTO animal (raza, fecha_ingreso, fecha_salida) VALUES(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE animal SET raza = %s, fecha_ingreso=%s, fecha_salida = %s WHERE id=%s"
    _ELIMINAR = "DELETE FROM animal WHERE id = %s" 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            animal = []
            for r in registros:
                animal.append(Animal(r[0],r[1],r[2],r[3]))
            return animal
    @classmethod
    def insertar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Raza, animal.FechaIngreso, animal.FechaSalida)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Raza, animal.FechaIngreso, animal.FechaSalida, animal.idAnimal)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.idAnimal,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    objeto1 = Animal(raza="Boxer",fecha_ingreso=date(2023, 11, 6),fecha_salida=date(2023, 11, 6))
    insercion = AnimalDao.insertar(objeto1)
    log.debug(f"Personas agregadas: {insercion}")
    objeto1.idAnimal = 1
    objeto1.FechaSalida = date(2023, 11, 8)
    actualizacion = AnimalDao.actualizar(objeto1)
    log.debug(f"Personas Actualizadas: {actualizacion}")
    objeto1.idAnimal = 2
    eliminacion = AnimalDao.eliminar(objeto1)
    log.debug(f"Personas Eliminadas: {eliminacion}")
    personas = AnimalDao().seleccionar()
    for p in personas:
        log.debug(p)

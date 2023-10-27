from Persona import Persona
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class PersonaDao:
    _SELECCIONAR = "SELECT id_persona, nombre, apellido, email, telefono FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona (nombre, apellido, email, telefono) VALUES(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s,apellido=%s, email = %s, telefono = %s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona = %s" 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            personas = []
            for r in registros:
                personas.append(Persona(r[0],r[1],r[2],r[3],r[4]))
            return personas
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Apellido, persona.Email, persona.Telefono)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Apellido,persona.Email,persona.Telefono,persona.idPersona)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    persona1 = Persona(nombre="Juan",apellido="Perez",email="dg@gmail.com",telefono="787492")
    insercion = PersonaDao.insertar(persona1)
    log.debug(f"Personas agregadas: {insercion}")
    persona1.idPersona = 2
    actualizacion = PersonaDao.actualizar(persona1)
    log.debug(f"Personas Actualizadas: {actualizacion}")
    eliminacion = PersonaDao.eliminar(persona1)
    log.debug(f"Personas Eliminadas: {eliminacion}")
    personas = PersonaDao().seleccionar()
    for p in personas:
        log.debug(p)

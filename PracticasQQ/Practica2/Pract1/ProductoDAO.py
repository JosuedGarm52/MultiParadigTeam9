from Producto import Producto
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class ProductoDao:
    _SELECCIONAR = "select id_producto, nombre, valor, descripcion from producto order by id_producto"
    _INSERTAR = "INSERT INTO producto (nombre, valor, descripcion) VALUES(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE producto SET nombre = %s,valor=%s, descripcion = %s WHERE id_producto=%s"
    _ELIMINAR = "DELETE FROM producto WHERE id_producto = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            producto = []
            for r in registros:
                producto.append(Producto(r[0],r[1],r[2],r[3]))
            return producto
    @classmethod
    def insertar(cls,producto):
        with CursorDelPool() as cursor:
            valores = (producto.Nombre, producto.Valor, producto.Descripcion)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,producto):
        with CursorDelPool() as cursor:
            valores = (producto.Nombre, producto.Valor, producto.Descripcion, producto.idProducto)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,producto):
        with CursorDelPool() as cursor:
            valores = (producto.idProducto,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    producto1 = Producto(nombre="Leche",valor="12",descripcion="Producto lacteo")
    insercion = ProductoDao.insertar(producto1)
    log.debug(f"Productos agregadas: {insercion}")
    producto1.idProducto = 3
    actualizacion = ProductoDao.actualizar(producto1)
    log.debug(f"Productos Actualizadas: {actualizacion}")
    eliminacion = ProductoDao.eliminar(producto1)
    log.debug(f"Productos Eliminadas: {eliminacion}")
    personas = ProductoDao().seleccionar()
    for p in personas:
        log.debug(p)

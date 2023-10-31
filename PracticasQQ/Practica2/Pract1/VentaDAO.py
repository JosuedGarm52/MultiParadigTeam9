from Venta import Venta
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class ProductoDao:
    _SELECCIONAR = "select id_venta, id_persona, id_producto, cantidad from venta order by id_venta"
    _INSERTAR = "INSERT INTO venta (id_persona, id_producto, cantidad) VALUES(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE venta SET id_persona = %s,id_producto=%s, cantidad = %s WHERE id_venta=%s"
    _ELIMINAR = "DELETE FROM venta WHERE id_venta = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            producto = []
            for r in registros:
                producto.append(Venta(r[0],r[1],r[2],r[3]))
            return producto
    @classmethod
    def insertar(cls,venta):
        with CursorDelPool() as cursor:
            valores = (venta.idPersona, venta.idProducto, venta.Cantidad)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,venta):
        with CursorDelPool() as cursor:
            valores = (venta.idPersona, venta.idProducto, venta.Cantidad, venta.idVenta)
            cursor.execute(cls._ACTUALIZAR,valores)
        return cursor.rowcount
    @classmethod
    def eliminar(cls,venta):
        with CursorDelPool() as cursor:
            valores = (venta.idVenta,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    venta1 = Venta(id_persona=1,id_producto=1,cantidad=1)
    insercion = ProductoDao.insertar(venta1)
    log.debug(f"Productos agregadas: {insercion}")
    venta1.idVenta = 3
    actualizacion = ProductoDao.actualizar(venta1)
    log.debug(f"Productos Actualizadas: {actualizacion}")
    eliminacion = ProductoDao.eliminar(venta1)
    log.debug(f"Productos Eliminadas: {eliminacion}")
    personas = ProductoDao().seleccionar()
    for p in personas:
        log.debug(p)

from logger_base import log 

class Venta: 
    def __init__(self,id_venta=None,id_persona=None,id_producto = None,cantidad = None) -> None:
        self._id_venta = id_venta
        self._id_persona = id_persona
        self._id_producto = id_producto
        self._cantidad = cantidad

    def __str__(self) -> str:
        return f"""
            ID VENTA {self._id_venta}, ID Persona: {self._id_persona},
            ID producto: {self._id_producto}, Cantidad: {self._cantidad}
        """
    
    @property
    def idVenta(self):
        return self._id_venta
    @idVenta.setter
    def idVenta(self, id):
        self._id_venta = id

    @property
    def idPersona(self):
        return self._id_persona
    @idPersona.setter
    def idPersona(self, id):
        self._id_persona = id
    
    @property
    def idProducto(self):
        return self._id_producto
    @idProducto.setter
    def idProducto(self, id):
        self._id_producto = id
    
    @property
    def Cantidad(self):
        return self._cantidad
    @Cantidad.setter
    def Cantidad(self, cantidad):
        self._cantidad = cantidad

if __name__ == "__main__":
    persona1 = Venta(1,1,1,1)
    print(persona1)
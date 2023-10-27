from logger_base import log 

class Producto: 
    def __init__(self,id_producto=None,nombre=None,valor = None,descripcion = None) -> None:
        self._id_producto = id_producto
        self._nombre = nombre
        self._valor = valor
        self._descripcion = descripcion

    def __str__(self) -> str:
        return f"""
            ID PRODUCTO {self._id_producto}, Nombre: {self._nombre},
            Valor: {self._valor}, Descripcion: {self._descripcion}
        """
    
    @property
    def idProducto(self):
        return self._id_producto
    @idProducto.setter
    def idProducto(self, id):
        self._id_producto = id
    
    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def Valor(self):
        return self._valor
    @Valor.setter
    def Apellido(self, valor):
        self._valor = valor

    @property
    def Descripcion(self):
        return self._descripcion
    @Descripcion.setter
    def Descripcion(self, descripcion):
        self._descripcion = descripcion

if __name__ == "__main__":
    persona1 = Producto(1,"Leche","12","Producto lacteo")
    print(persona1)
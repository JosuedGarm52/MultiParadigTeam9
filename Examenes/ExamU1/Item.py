from Locacion import Locacion

class Item(Locacion):
    def __init__(self,nombreItem,cantidadItems,precioItem) -> None:
        self._nombreItem = nombreItem #Nombre del item
        self._cantidadItems = cantidadItems #Cantidad entera
        self._precioItem = precioItem

    def CalcularPrecioItem(self):
        self._precioItem = self._precioItem + (self._precioItem * self._porcentajeIVA)
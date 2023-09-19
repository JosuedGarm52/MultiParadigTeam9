import Item as item
import Locacion as loc

j = 1
while j == 1:
    nombreLocacion = input("Ingrese el nombre de la locación: ")
    porcentajeIVA = float(input("Ingrese el porcentaje de IVA de dicha locación: "))
    cantItems = int(input("Ingrese la cantidad de items a ingresar: "))
    listaItems = [None] * cantItems #Lista vacía de un tamaño específico
    sumatoriaCapital = 0
    
    miLocacion = loc.Locacion(nombreLocacion,porcentajeIVA)
    
    i = 0
    while i < cantItems:
        nombreItem = input(f"Ingrese el nombre del item #{i+1} para la lista: ")
        listaItems[i] = nombreItem
        cantidadItem = int(input("Ingrese la cantidad entera de unidades disponibles de este item: "))
        precioItem = float(input("Ingrese el precio de dicho item: "))
        sumatoriaCapital = sumatoriaCapital + precioItem
        miItem = item.Item(nombreItem,cantidadItem,precioItem)
        i+=1
    
    j = int(input("¿Desea ingresar otra locación? 1 - Si, 2 - No"))
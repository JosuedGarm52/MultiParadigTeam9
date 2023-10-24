
#comentario extra
def producto(*arg):
    producto_total = 1  # Inicializamos el producto en 1
    suma_total = 0      # Inicializamos la suma en 0
    
    for numero in arg:
        producto_total *= numero
        suma_total += numero
    
    return producto_total, suma_total
try:
    prod, suma = producto(1,2,3,4,5)
except Exception as err:
    print(err)
# Mostrar los resultados
print(f"El producto total es: {prod}")
print(f"La suma total es: {suma}")

# print(producto(1,2,3,4,5))


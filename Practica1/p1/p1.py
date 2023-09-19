# Definir la función que calcula el producto y la suma total
def calcular_producto_y_suma(*args):
    producto_total = 1  # Inicializamos el producto en 1
    suma_total = 0      # Inicializamos la suma en 0
    
    for numero in args:
        producto_total *= numero
        suma_total += numero
    
    return producto_total, suma_total

# Solicitar al usuario la entrada de números separados por comas
while True:
    try:
        # Convertir la entrada en una lista de números
        entrada = input("Ingresa números separados por comas: ")
        numeros = [float(numero) for numero in entrada.split(',')]
    except TypeError:
        print("Introdujiste un numero distinto a un numero")
        continue
    except ValueError:
        print("Introdujiste un numero distinto a un numero")
        continue
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        break
    else:
        # Llamar a la función con los números proporcionados

        producto, suma = calcular_producto_y_suma(*numeros)

        # Mostrar los resultados
        print(f"El producto total es: {producto}")
        print(f"La suma total es: {suma}")
        break

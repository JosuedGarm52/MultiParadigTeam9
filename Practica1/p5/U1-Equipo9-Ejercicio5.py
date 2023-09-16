# #5 – Manejo de información
# INSTRUCCIONES: Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{valor}”: “{llave}”.

# Alejandro Díaz Medrano                19100168
# Josué Daniel García Maldonado         19100182
# Rogelio Zamarripa Treviño             18100248

def funcionImprimirValoresLlaves(n):
    llaves = {}
    i = 1

    while i <= n:
        llave = input(f"Ingrese la llave {i}: ")
        valor = int(input(f"Ingrese el valor numerico de la llave {i}: "))

        llaves[llave] = valor
        i+=1
    
    for llave, valorLlave in llaves.items():
        print(f"{valorLlave} : {llave}")

n = int(input("Ingrese la cantidad de datos que desea registar: "))
funcionImprimirValoresLlaves(n)

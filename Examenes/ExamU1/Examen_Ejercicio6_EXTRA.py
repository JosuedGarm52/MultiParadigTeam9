#EXTRA - EJERCICIO 6: Crear una función que reciba como parámetro una palabra, dicha función leerá un archivo .txt el cual
# debe tener un texto a elegir de su preferencia (poner la referencia) de al menos 200 palabras o más, la
# función debe devolver la cantidad de veces que se repite la palabra y sus posiciones tomando en cuenta
# el primer caracter.


# palabraIngresada = input("Ingrese una palabra: ")
# print(funcionDevolverCantPalabraRepetidaPosiciones(palabraIngresada))

import os

filename = os.path.dirname(os.path.abspath(__file__))

def DevolverRuta(name):
    return os.path.join(filename, name)

def funcionDevolverCantPalabraRepetidaPosiciones(palabra):
    ocurrencias = {}
    
    try:
        with open(DevolverRuta("textoEjemplo.txt")) as f:
            nombre = f.readline()

            while nombre:
                nombre = nombre.strip()
                if nombre in ocurrencias and nombre == palabra:
                    ocurrencias[nombre] += 1
                else:
                    if nombre == palabra:
                        ocurrencias[nombre] = 1
                
                nombre = f.readline()
        
        return ocurrencias

    except FileNotFoundError:
        msg = "ERROR: El archivo " + filename + " no pudo ser encontrado o no existe."
        print(msg)

palabraIngresada = input("Ingrese una palabra: ")
print(funcionDevolverCantPalabraRepetidaPosiciones(palabraIngresada))
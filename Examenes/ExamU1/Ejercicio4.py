
import csv
import os
directorio_actual = os.path.dirname(os.path.abspath(__file__))
def DevolverRuta(name):
        return os.path.join(directorio_actual, name)
def Crear_Archivo(data):
    if not data:
        return  # Salir si la lista está vacía
    lista= []
     

    lista.append(data)

    encabezado = list(lista[0].keys())  # Tomar las llaves del primer diccionario
    
    with open(DevolverRuta('NuevoArchiv.csv'), mode='w', newline='', encoding='latin1') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=encabezado)
        writer.writeheader()

        for fila in lista:
            writer.writerow({clave: fila[clave] for clave in encabezado})

try:
    nombre = input('Introduce el nombre del archivo: \n')
    with open(DevolverRuta(nombre),mode='r', encoding='latin1', errors='replace') as file:
        csv_reader = csv.DictReader(file)
        data = []

        for row in csv_reader:
            data.append(row)
    #print(data)
    Crear_Archivo(data)

except Exception as err:
    print(err)
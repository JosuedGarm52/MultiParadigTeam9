
b = True
lista = []
lista_ordenada =[]
try:
    while b:
        cadena = input('Introduce una cadena: ')
        cadenaA = cadena.strip().split(' ')
        lista.extend(cadenaA)
        cadenax = input('Quieres introducir otra cadena?, introduce cualquier letra, si no, deja un espacio en blanco:\n')
        if cadenax.strip() == "" or cadenax == "$" or cadenax.strip() == " ":
            b = False
            break
except Exception as e:
    print(e)

lista_ordenada = sorted(lista, key=str.lower)
def es_numero(cadena):
    return cadena.replace(".", "", 1).isdigit()
numeros = [elemento for elemento in lista_ordenada if es_numero(elemento)]

# Separar las cadenas en una nueva lista
cadenas = [elemento for elemento in lista_ordenada if not es_numero(elemento)]

for elemento in cadenas:
    print(elemento, end=' ')
for elemento in numeros:
    print(elemento, end=' ')
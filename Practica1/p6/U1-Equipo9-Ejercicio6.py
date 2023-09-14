# #6 - Razonamiento y prueba de código
# INSTRUCCIONES: Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar condicionales.
# Máximo 5 líneas de código.

# Alejandro Díaz Medrano                19100168
# Josué Daniel García Maldonado         19100182
# Rogelio Zamarripa Treviño             18100248

# Importar las dependencias necesarias
from num2words import num2words

valido = False
while not valido:
    n = int(input('Ingrese un número entre 0 y 20: '))
    valido = n in range(21)
print(num2words(n, lang = 'es', ordinal = False))

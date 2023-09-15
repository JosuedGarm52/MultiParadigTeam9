# #7 – Formateo y conversiones
# INSTRUCCIONES: Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la
# fecha del día de hoy en el formato seleccionado.

# Alejandro Díaz Medrano                19100168
# Josué Daniel García Maldonado         19100182
# Rogelio Zamarripa Treviño             18100248

# Importar las dependencias necesarias
from datetime import datetime

opcionMenuFecha = int(input("---Menú de Formateo y Conversiones (Programación Multiparadigma)---\nSeleccione el formato con el que desea imprimir la fecha del día de hoy: \n1.- Imprimir YYYY/MM/DD \n2.- Imprimir MM/DD/YYYY\n"))
if(opcionMenuFecha == 1):
    print(datetime.today().strftime('%Y/%m/%d'))
else: 
    if(opcionMenuFecha == 2):
        print(datetime.today().strftime('%m/%d/%Y'))
    else:
        print("ERROR DE CAPTURA: La opción de formato que ud. proporcionó no se encuentra dentro de nuestro menú (1.- Imprimir YYYY/MM/DD, 2.- Imprimir MM/DD/YYYY).")

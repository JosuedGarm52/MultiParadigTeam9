nombre_completo = input("Por favor, introduce tu nombre completo: ")

nombre_formateado = ""

for i, letra in enumerate(nombre_completo):
    if i % 2 == 0:
        nombre_formateado += letra.upper()
    else:
        nombre_formateado += letra.lower()

print("Tu nombre con letras intercaladas es:", nombre_formateado)
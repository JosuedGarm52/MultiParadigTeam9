# Josue Temporal
nombre_completo = input("Introduce tu nombre: ")

nombre_inverso = ""
mayuscula = True

for letra in nombre_completo:
    if mayuscula:
        nombre_inverso += letra.upper()
    else:
        nombre_inverso += letra.lower()
    mayuscula = not mayuscula

print("Su nombre de manera inversa letra por letra intercalando"+
     + "una letra minuscula a una mayuscula es: ", nombre_inverso)
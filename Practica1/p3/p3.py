# Josue Temporal
nombre_completo = input("Introduce tu nombre: ")

nombre_inverso = ""
mayuscula = True

for letra in nombre_completo[::-1].lower():
    if letra.isalpha():
        if mayuscula:
            nombre_inverso += (letra.lower()+' ')
        else:
            nombre_inverso += (letra.upper()+ ' ')
        mayuscula = not mayuscula
    else:
        nombre_inverso += letra

print("Su nombre de manera inversa letra por letra intercalando "
     + f"una letra minuscula a una mayuscula es: {nombre_completo} : {nombre_inverso[::-1].strip()}")
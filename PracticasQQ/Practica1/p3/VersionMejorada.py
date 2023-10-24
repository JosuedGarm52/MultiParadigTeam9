nombre_completo = input("Introduce tu nombre: ")

nombre_inverso = ''.join(
    (letra.lower() if i % 2 == 0 else letra.upper()) + ' '
    if letra.isalpha()
    else letra
    for i, letra in enumerate(reversed(nombre_completo))
)

print(f"Su nombre de manera inversa letra por letra intercalando una letra minuscula a una mayuscula es: {nombre_completo} : {nombre_inverso[::-1].strip()}")

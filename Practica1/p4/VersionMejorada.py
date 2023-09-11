diccionario = {}
total_credito = 0

for _ in range(8):  # Limitar el bucle a 8 iteraciones máximas
    print("------")
    entrada = input("Introduce el semestre (inferior a 8vo), el nombre de la materia y créditos de su semestre, con este formato\n[semestre - materia - crédito], si deseas terminar deja un espacio en blanco o el caracter °:\n")

    if not entrada.strip() or entrada == "°":
        break

    arreglo = entrada.split(" - ")
    if len(arreglo) != 3:
        print("Formato incorrecto. Debe ser [semestre - materia - crédito]")
        continue

    semestre, materia, creditos = arreglo
    
    try:
        semestre = int(semestre)
        creditos = int(creditos)
    except ValueError:
        print("El valor entero no es válido.")
        continue

    if semestre < 8 and materia not in diccionario:
        diccionario[materia] = creditos
        total_credito += creditos
    elif semestre >= 8:
        print("XxX Solo puedes registrar materias inferiores al 8°vo semestre XxX")
    elif materia in diccionario:
        print("XxX Esa materia ya fue incluida XxX")
    else:
        print("Error inesperado :(")

print("------------")
print(diccionario)

if diccionario:
    for asignatura, creditos in diccionario.items():
        print(f'“{asignatura}” tiene “{creditos}” créditos')

    print(f"Total de créditos del semestre: {total_credito}")
    print(list(diccionario.keys()))
else:
    print("La lista de materias está vacía :(")

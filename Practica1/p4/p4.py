# Josue Temporal
diccionario = {}
numSemestre = 0
cond = True
cont = 0
while cond:
    print("------")
    entrada = input("Introduce el semestre (inferior a 8vo), el nombre de la materia y creditos de su semestre, con este formato\n[semestre - materia - credito], si deseas terminar deja un espacio en blanco o el caracter °:\n")
    if len(entrada) == 0:
        cond = False
        break
    elif entrada == " " or entrada == "°":
        cond = False
        break
    try:
        arreglo = entrada.split(" - ")
        semestre = int(arreglo[0])
        materia  = arreglo[1]
        creditos = int(arreglo[2])
    except ValueError:
        print("El valor entero no es valido.")
        semestre = 12
        materia = "prueba"
        creditos = 0
        
    if semestre < 8 and numSemestre == 0 and cont<8:
        numSemestre = semestre
        diccionario[materia] = creditos
    elif semestre < 8 and numSemestre == semestre and materia not in diccionario and cont <8:
        diccionario[materia] = creditos
    elif cont ==8:
        print("XxX Parece que sobrepasaste el numero de materias por semestre")
        break
    elif semestre >= 8:
        print("XxX Solo puedes registrar materias inferiores al 8°vo semestre XxX")
    elif semestre != numSemestre:
        print("XxX Debes elegir el mismo semestre de los demas XxX")
    elif materia in diccionario:
        print("XxX Esa materia ya fue incluida XxX")
    else:
        print("Error inesperado :(")
print("------------")
total_credito = 0
print(diccionario)
if diccionario :
    for asignatura in diccionario:
        creditos = int(diccionario[asignatura])
        total_credito += creditos
        print(f'“{asignatura}” tiene “{creditos}” créditos')
    print(f"Total de creditos del semestre: {total_credito}")
    print(list(diccionario.keys()))
else:
    print("La lista de materias esta vacia :(")

# Resultados:
# 5 - graficacion - 4
# 5 - fund en telecom - 4
# 5 - sistem prog - 4   
# 5 - taller bd - 4 
# 5 - software - 4 
# 5 - desarrollo sustentable - 5
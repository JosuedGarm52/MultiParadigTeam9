def LLenarAuto(n):
    if(n >= 2 and n<=10):
        matrizA1 = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        
        #print(matrizA1)
        return matrizA1
    else:
        print("El numero debe estar entre 2 y 10")

def LlenarCararol(listaA,listaB):
    n = len(listaA)
    m = len(listaA[0])

    # Inicializar variables para las direcciones del recorrido en espiral
    arriba, abajo, izquierda, derecha = 0, n - 1, 0, m - 1

    valor = 1  # Valor inicial
    while valor <= n * m:
        # Llenar la fila superior
        for j in range(izquierda, derecha + 1):
            listaB[arriba][j] = valor
            valor += 1
        arriba += 1

        # Llenar la columna derecha
        for i in range(arriba, abajo + 1):
            listaB[i][derecha] = valor
            valor += 1
        derecha -= 1

        # Llenar la fila inferior
        for j in range(derecha, izquierda - 1, -1):
            listaB[abajo][j] = valor
            valor += 1
        abajo -= 1

        # Llenar la columna izquierda
        for i in range(abajo, arriba - 1, -1):
            listaB[i][izquierda] = valor
            valor += 1
        izquierda += 1
    return listaB
try:
    numero = int(input('Introduce un numero entre 2~10: '))
    a = LLenarAuto(numero)
    matrizB1 = [[0 for _ in range(numero)] for _ in range(numero)]
    b = LlenarCararol(a,matrizB1 )
    for i in b:
        print(i)
except Exception as e:
    print(e)
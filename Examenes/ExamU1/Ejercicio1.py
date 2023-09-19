def LLenarAuto(n):
    if(n >= 2 and n<=10):
        matrizA1 = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        
        #print(matrizA1)
        return matrizA1
    else:
        print("El numero debe estar entre 2 y 10")

def LlenarCararol(listaA,listaB):
    for i in range(len(listaA[0])):
        listaB[0][i] = listaA[0][i]
    for i in range(len(listaA)-1):
        for j in range(len(listaA[1])):
            if i == len(listaA):
                listaB[i][-1] = listaA[1][j]
    

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
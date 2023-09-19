

#se requiere hacer un programa que indique cual es mayor de 2 numeros
# ocn 3 digitos cada 1 pero hay un problema con la interfaz y esya tomando los
#numeros al reves


#ejemplo entradas: n1=734 n2=893 n3=437 salidas: 437 cambiarlo antes de hacer la comparacion



while True:
    try:
        n1 = int(input('ingresa el valor de n1: '))
        if n1>=0 and n1<1000:
            n2 = int(input('ingresa el valor de n2: '))
            if n1>=0 and n1<1000:
                num1 = str(f"{(n1):03.0f}")
                num2 = str(f"{(n2):03.0f}")
                # num2 = str(n2)
                res1 = num1[::-1]
                # print('////')
                res2 = num2[::-1]
                rest1 = int(res1)
                # print(rest1,'$$$$$$$$$$$$$$$')
                rest2 = int(res2)
                if rest1 > rest2:
                    # print(f"{format((rest1): 08.2f)}")
                    print(f"{(rest1):03.0f} ///")
                    break
                else:
                    print(f"{(rest2):03.0f} ///")
                    break
            else:
                continue
        else: 
            continue
    except Exception as err:
        print(err)






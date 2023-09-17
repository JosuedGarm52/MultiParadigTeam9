from num2words import num2words

n = int(input('Ingrese un número entre 0 y 20: '))
while not 0 <= n <= 20: n = int(input('Ingrese un número entre 0 y 20: '))
print(num2words(n, lang='es', ordinal=False))

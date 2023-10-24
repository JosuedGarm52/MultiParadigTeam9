# Josue Temporal
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
resultado = []
for i, letra in enumerate(abecedario):
    if (i+1) % 2 != 0:
        resultado.append(letra)
print(resultado)
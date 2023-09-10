import string

abecedario = list(string.ascii_lowercase)
resultado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 2 != 0]
print(resultado)

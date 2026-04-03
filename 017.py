from math import hypot

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
resultado = hypot(oposto , adjacente)
print(f'O cumprimento da hipotenusa é {resultado:.2f}')
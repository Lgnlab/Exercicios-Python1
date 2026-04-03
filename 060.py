'''from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}')'''  # Utilizando módulo para resolver

numero = int(input('Digite um número para ver seu fatorial: '))
c = numero
f = 1
print(f'Calculando {numero}!')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
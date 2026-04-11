import random
numeros = []
def sorteio():
    print(f'Números sorteados:')
    for s in range(0, 5):
        sorteados = random.randint(1, 10)
        numeros.append(sorteados)
    print(numeros)

def somapar():
    soma = 0
    print('PARES:')
    for c in numeros:
        if c % 2 == 0:
            print(c, end=' ')
            soma += c
    print()
    print(f'A soma dos PARES: {soma}')


sorteio()
somapar()
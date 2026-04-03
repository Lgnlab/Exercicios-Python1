lista = list()
pares = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    sair = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if sair == 'N':
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impar.append(c)

print(f'Lista geral: {lista}')
print(f'Lista números PARES: {pares}')
print(f'Lista números ÍMPARES: {impar}')

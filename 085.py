dados = [[], []]
numero = 0
for n in range(1, 8):
    numero = int(input(f'{n} número: '))
    if numero % 2 == 0:
        dados[0].append(numero)
    else:
        dados[1].append(numero)
dados[0].sort()
dados[1].sort()
print(f'Valores PARES: {dados[0]}')
print(f'Valores ÍMPARES: {dados[1]}')

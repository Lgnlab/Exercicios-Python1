matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_tc = maior_sl = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('=' * 30)
print(f'A soma dos valores PARES: {soma_pares}')
for l in range(0, 3):
    soma_tc += matriz[l][2]
print(f'A soma dos valores da terceira coluna: {soma_tc}')
for c in range(0, 3):
    if c == 0:
        maior_sl = matriz[1][c]
    elif matriz[1][c] > maior_sl:
        maior_sl = matriz[1][c]
print(f'O maior valor da segunda linha: {maior_sl}')
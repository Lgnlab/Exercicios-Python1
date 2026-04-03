print(f'{'TABUADA' :=^30}')
numero = int(input('Escolha um número inteiro para ver a tabuada: '))

for c in range(1, 10+1):
    print(f'{numero} x {c} = {numero * c}')
print('\033[0;31mFIM\033[m') 
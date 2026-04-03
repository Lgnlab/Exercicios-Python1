print(f'{'NÚMEROS PRIMOS' :=^30}')
total = 0
numero = int(input('Digite um número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}',end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes')
if total == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')

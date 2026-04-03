print('Calculando uma PA...')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro 
contador = 1
while contador <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    contador += 1
print('\033[32mFIM\033[m')

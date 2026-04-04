lista1 = []
lista2 = []
lista3 = []
for l1 in range(1, 4):
    numero1 = int(input('Informe os valores da primeira linha: '))
    lista1.append(numero1)
print('=' * 40)
for l2 in range(1, 4):
    numero2 = int(input('Informe os valores da segunda linha: '))
    lista2.append(numero2)
print('=' * 40)
for l3 in range(1, 4):
    numero3 = int(input('Informe os valores da terceira linha: '))
    lista3.append(numero3)
print('=' * 40)
print(f'[{lista1[0]}] [{lista1[1]}] [{lista1[2]}]')
print(f'[{lista2[0]}] [{lista2[1]}] [{lista2[2]}]')
print(f'[{lista3[0]}] [{lista3[1]}] [{lista3[2]}]')

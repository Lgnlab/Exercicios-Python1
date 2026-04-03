dados = list()
princ = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso(kg): ')))
    if len(princ) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    princ.append(dados[:])
    dados.clear()
    sair = str(input('Quer continuar(S/N): ')).strip().upper()[0]
    if sair == 'N':
        break
print(f'Os dados foram {princ}')
print(f'Foram cadastrados {len(princ)} pessoas.')
print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor:.1f}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()

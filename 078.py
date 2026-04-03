valores = []
maior = menor = 0

for p in range(0,6):
    valores.append(int(input(f'Digite um valor na posição {p}: ')))
    if p == 0:
        maior = menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]
print(f'Você digitou os valores \033[32m{valores}\033[m')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print()

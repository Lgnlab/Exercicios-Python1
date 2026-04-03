maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa(Kg): '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\033[31mO maior peso lido foi de {maior}Kg\033[m')
print(f'\033[32mO menor peso lido foi de {menor}kg\033[m')
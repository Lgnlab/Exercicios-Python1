soma = 0
cont = 0
for c in range(1, 6+1):
    numero = int(input(f'Digite o {c} valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'\033[0;32mVocê informou {cont} pares e a soma foi: {soma}\033[m')
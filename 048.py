s = 0
cont = 0
for c in range(1, 500+1):
    if c % 2 != 0 and c % 3 == 0:
        s = s + c       #ALTERNATIVA RESUMIDA: s+= c
        cont += 1
print(f'\033[0;32mA soma total dos {cont} números ímpares que são múltiplos de três é: {s}\033[m')
print('\033[0;31mFIM\033[m')

valor1 = int(input('Primeiro número: '))
valor2 = int(input('Segundo número: '))

if valor1 > valor2:
    print(f'\033[0;32mO primeiro valor é maior: {valor1}\033[m')
    print(f'\033[0;31mO segundo valor é menor: {valor2}\033[m')
elif valor2 > valor1:
    print(f'\033[0;32mO segundo valor é maior: {valor2}\033[m')
    print(f'\033[0;31mO primeiro valor é menor: {valor1}\033[m')
elif valor1 == valor2:
    print('\033[7;35;45mNÃO EXISTE VALOR MAIOR;OS DOIS SÃO IGUAIS\033[m')
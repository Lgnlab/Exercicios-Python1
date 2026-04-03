numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{numero} convertido em BINÁRIO é igual {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para OCTAL é igual {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual {hex(numero)[2:]}')   #O [2:] TIRA A STRING DA FRENTE DO NÚMERO 
else:
    print('\033[0;31mOPÇÃO INVÁLIDA!TENTE NOVAMENTE\033[0m')
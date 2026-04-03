from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')    #EQUIVALENTE A UMA LISTA 
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

escolha = int(input('Qual é sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print(f'O computador escolheu {itens[computador]}')   #SUBSTITUI O NÚMERO PELO NOME EM ITENS 
print(f'O jogador jogou {itens[escolha]}')            #SUBSTITUI O NÚMERO PELO NOME EM ITENS 
print('-=' * 15)

if computador == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('JOGADOR GANHOU')
    elif escolha == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('\033[0;31mJOGADA INVÁLIDA\033[m')
elif computador == 1:
    if escolha == 1:
        print('EMPATE')
    elif escolha == 0:
        print('COMPUTADOR GANHOU')
    elif escolha == 2:
        print('JOGADOR GANHOU')
    else:
         print('\033[0;31mJOGADA INVÁLIDA\033[m')
elif computador == 2:
    if escolha == 2:
        print('EMPATE')
    elif escolha == 0:
        print('JOGADOR GANHOU')
    elif escolha == 1:
        print('COMPUTADOR GANHOU')
    else:
         print('\033[0;31mJOGADA INVÁLIDA\033[m')
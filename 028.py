from random import randint
from time import sleep
computador = randint(0, 5) #FAZ O COMPUTADOR PENSAR
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) #JOGADOR TENTA ADVINHAR
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Pensei no {computador}')
    print('Tente novamente!')
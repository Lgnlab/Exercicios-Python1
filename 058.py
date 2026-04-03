from random import randint

print('''\033[33mSou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi ?\033[m''')

computador = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Em que número pensei: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        else:
            print('Menos...Tente mais uma vez.')
print(f'\033[32mPARABÉNS! você conseguiu me vencer com {tentativas} tentativas!\033[m')

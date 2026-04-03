from random import randint

print('-=-' * 8)
print('\033[34mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('-=-' * 8)

vitoria = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else: 
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break 
    print('Vamos jogar novamente...')
print(f'\033[31mGAME OVER!\033[m você venceu {vitoria} vezes.')

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite outro número: '))
print('''\033[32m
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa\033[m''')
escolha = 0
escolha = int(input('Qual sua escolha: '))

while escolha != 5:
    if escolha == 1:
        soma = primeiro_numero + segundo_numero
        print(f'{primeiro_numero} + {segundo_numero} = {soma}')
        escolha = int(input('Qual sua escolha: '))
    elif escolha == 2:
        multiplica = primeiro_numero * segundo_numero
        print(f'{primeiro_numero} * {segundo_numero} = {multiplica}')
        escolha = int(input('Qual sua escolha: '))
    elif escolha == 3:
        if primeiro_numero > segundo_numero:
            print(f'O número {primeiro_numero} > {segundo_numero}')
        elif primeiro_numero < segundo_numero:
            print(f'O número {segundo_numero} > {primeiro_numero}')
        elif primeiro_numero == segundo_numero:
            print(f'O número {primeiro_numero} = {segundo_numero}')
        escolha = int(input('Qual sua escolha: '))
    elif escolha == 4:
        primeiro_numero = int(input('Digite um número: '))
        segundo_numero = int(input('Digite outro número: '))
        escolha = int(input('Qual sua escolha: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('\033[31mOpção Inválida. Tente Novamente!\033[m')
        break
print('FIM DO PROGRAMA! VOLTE SEMPRE.')
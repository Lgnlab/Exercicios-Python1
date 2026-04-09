def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for cont in range(1, 10 + 1, 1):
        print(f'{cont}', end=' ')
    print('FIM!', end='')
    print()
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for cont in range(10, 0, -2):
        print(cont, end=' ')
    print('0 FIM!', end='')
    print()
    print('-=' * 20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))


contador()

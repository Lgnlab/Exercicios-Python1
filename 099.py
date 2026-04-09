def maior(*numeros):
    print('Analisando os valores passsados...')
    maior_num = 0
    for c in numeros:
        print(c, end=' ')
        if c > maior_num:
            maior_num = c
    print(f'Foram informados {len(numeros)} valores ao todo.', end='')
    print()
    print(f'Maior número: {maior_num}')

maior(1, 3, 5, 25, 7, 8, 10)
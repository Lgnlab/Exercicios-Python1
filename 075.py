n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))

elementos = (n1, n2, n3, n4)
print(f'Você digitou os números {elementos}')
print(f'O número 9 foi digitado {elementos.count(9)} vezes')
if 3 in elementos:
    print(f'O número 3 foi digitado na posição {elementos.index(3)+1}ª')
else:
    print('O número 3 não foi digitado nenhuma vez!')
print('Os números pares digitados foram: ', end='')
for c in elementos:
    if c % 2 == 0:
        print(c, end=' , ')

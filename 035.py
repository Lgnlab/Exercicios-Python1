a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
print(10 * '-=-')
print('ANALISANDO TRIÂNGULOS')
print(10 * '-=-')


if a + b > c and a + c > b and b + c > a:
    print('PODEM FORMAR UM TRIÂNGULO!')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO!')
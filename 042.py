a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('\033[0;32mPODEM FORMAR UM TRIÂNGULO\033[m', end=' ')
    if a == b == c:
        print('\033[0;35mEQUILÁTERO\033[m')
    elif a != b != c != a:
        print('\033[0;35mESCALENO\033[m')
    else:
        print('\033[0;35mISÓSCELES\033[m')
else:
    print('\033[0;31mNÃO PODEM FORMAR UM TRIÂNGULO!\033[m')

while True:
    numero = int(input('Digite um número para ver sua tabuada: ')) 
    print('-=-' * 15) 
    if numero < 0:
        print('\033[31mPROGRAMA DE TABUADA ENCERRADO\033[m. \033[32mVOLTE SEMPRE!\033[m')
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('-=-' * 15)
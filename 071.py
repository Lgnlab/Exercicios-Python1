print('=' * 30)
print(f'{'BANCO LGN':^30}')
print('=' * 30)
print('CÉDULAS DISPONÍVEIS: R$50 / R$20 / R$10 / R$1')

saque = int(input('Qual valor você quer sacar? R$'))
total = saque
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break 
print('=' * 30)
print('\033[32mVOLTE SEMPRE!\033[m')
print('=' * 30)

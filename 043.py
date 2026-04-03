peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2) 
print(f'SEU IMC:{imc:.1f}')

if imc < 18.5:
    print('\033[0;31mABAIXO DO PESO\033[m')
elif imc <= 25:
    print('\033[0;32mPESO IDEAL\033[m')
elif imc <= 30:
    print('\033[0;31mSOBREPESO\033[m')
elif imc <= 40:
    print('\033[0;31mOBESSIDADE\033[m')
else:
    print('\033[0;31mOBESSIDADE MÓRBIDA\033[m') 
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('\033[0;36mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('\033[0;34mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('\033[0;32mJUNIOR\033[m')
elif idade > 19 and idade <= 25:
    print('\033[0;31mSENIOR\033[m')
elif idade > 25:
    print('\033[0;33mMASTER\033[m')

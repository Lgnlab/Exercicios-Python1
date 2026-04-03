sexo = str(input('Informe seu sexo (F/M): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31mDados inválidos\033[m. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'\033[32mSexo {sexo} resgistrado com sucesso!\033[m')
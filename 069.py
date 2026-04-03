
cont_idade = homem = mulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resposta = ' '
    while resposta not in 'SN':
        respota = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('\033[32mFim do cadastro!\033[m')
print(f'\033[33m{cont_idade} pessoa(s) tem 18 ou mais!\033[m')
print(f'\033[34mForam cadastrado(s) {homem} homem/homens!\033[m')
print(f'\033[35mTemos {mulher} mulheres abaixo de 20 anos!\033[m')
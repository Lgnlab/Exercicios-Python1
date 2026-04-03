from datetime import date
maior = 0
menor = 0

for data in range(1, 7+1):
    ano_nasc = int(input(f'Digite a {data} de nascimento: '))
    idade = date.today().year - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('-=-' * 9)
print(f'\033[32mMaior de idade: {maior} pessoas\033[m')
print(f'\033[31mMenor de idade: {menor} pessoas\033[m')
print('-=-' * 9)
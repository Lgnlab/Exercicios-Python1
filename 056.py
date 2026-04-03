soma_idade = 0
media_idade = 0
idade_velho = 0
nome_velho = ''
contador = 0

for n in range(1, 5):
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().lower()
    soma_idade += idade
    media_idade = soma_idade / 4
    if n == 1 and sexo == 'm':
        idade_velho = idade
        nome_velho = nome
    if sexo == 'm' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo == 'f' and idade < 20:
            contador += 1

print(f'{contador} mulher(es) tem menos de 20 anos')
print(f'O homem mais velho se chama {nome_velho} e ele tem {idade_velho}')
print(f'A média de idade das 4 pessoas é {media_idade:.2f}')


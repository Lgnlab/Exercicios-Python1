dados = dict()
lista_dados = []
lista_mulher = []
lista_idade = []
soma = 0
while True:
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    if sexo == 'F':
        lista_mulher.append([nome,sexo,idade])
    soma += idade
    lista_dados.append([nome,sexo,idade])
    sair = input('Quer cadastrar mais alguém [S/N]? ').strip().upper()[0]
    if sair == 'N':
        break
dados['cadastros'] = lista_dados
media = soma / len(lista_dados)
for idade in lista_dados:
    if idade[2] > media:
        lista_idade.append(nome)
        lista_idade.append(idade[2])
print('=>' * 35)
print(dados)
print('=>' * 35)
print(f'Foram cadastradas {len(lista_dados)} pessoas.')
print(f'Média de idade do grupo: {media:.1f}')
print(f'Lista de mulheres: {lista_mulher}')
print(f'Pessoas com idade acima da média: {lista_idade}')

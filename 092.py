from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano_nascimento
carteira_trabalho = int(input('Carteira de Trabalho (0 não tem): '))
if carteira_trabalho == 0:
    print(f'Nome tem o valor {dados['nome']}')
    print(f'Idade tem o valor {dados['idade']}')
    print(f'ctps tem o valor {carteira_trabalho}')
else:
    dados['carteira_trabalho'] = carteira_trabalho
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['Ano de contratação'] + 35
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')

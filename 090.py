dados = dict()
dados['nome'] = str(input('Nome: ')).strip()
dados['media'] = float(input('Média: '))
if dados['media'] >= 7:
    dados['resultado'] = 'Aprovado'
else:
    dados['resultado'] = 'Reprovado'
print(dados)
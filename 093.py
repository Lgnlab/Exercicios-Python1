dados = dict()
lista_gols = []
soma = 0
dados['Nome'] = str(input('Nome do jogador: ')).strip()
dados['Partidas'] = int(input('Partidas jogadas: '))
for perg in range(1, dados['Partidas'] + 1):
    gols = int(input('Gols por partidas: '))
    lista_gols.append(gols)
    soma += gols
dados['Gols marcados'] = lista_gols
dados['Total de gols'] = soma
print('=' * 45)
print(dados)
print('=' * 45)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 45)
print(f'O jogador {dados['Nome']} jogou {dados['Partidas']} partidas.')
for i,g in enumerate(lista_gols):
    print(f'=> Na partida {i}, fez {g} gols.')
print(f'Foi um total de {soma} gols.')
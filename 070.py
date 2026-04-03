print('-' * 30  )
print(f'{'LOJA DO LUCAS':^30}')
print('-' * 30)

soma = produto_mil = menor_preco = cont = 0
nome_barato = ''
while True:
    nome_produto = str(input('Qual o nome do produto: ')).strip().upper()
    preco = float(input('Quanto custa o protudo: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        produto_mil += 1
    if cont == 1:
        menor_preco = preco
        nome_barato = nome_produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_barato = nome_produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O total da compra ficou R${soma:.2f}')
print(f'{produto_mil} produto(s) custam mais de R$1000')
print(f'O produto mais barato é {nome_barato} e custa R${menor_preco:.2f}')

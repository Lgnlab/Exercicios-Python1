preco_produto = float(input('Digite o valor do produto R$'))
desconto = preco_produto * (5 / 100)
final = preco_produto - desconto
print(f'Valor sem desconto R${preco_produto:.2f}\nDesconto R${desconto:.2f}\nValor com desconto R${final:.2f}')
compra = float(input('Valor da compra (R$): '))
print(f'{' LOJAS LUCAS' :=^30}')    #NOME FORMATO EM UM DETERMINADO ESPAÇO 
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual é sua opção: '))

if escolha == 1:
    print(f'Sua compra de R${compra:.2f} vai ter um desconto de 10%')
    desconto = compra - (compra *    10 / 100)
    print(f'Valor com desconto R${desconto:.2f}')
elif escolha == 2:
    print(f'Sua compra de R${compra:.2f} vai ter um desconto de 5%')
    desconto2 = compra - (compra * 5 / 100)
    print(f'Valor com desconto R${desconto2:.2f}')
elif escolha == 3:
    parcelado = compra / 2
    print(f'Sua compra de R${compra:.2f} ficará em 2x de R${parcelado:.2f}')
elif escolha == 4:
    quantidade_parcelas = int(input('Quantidade de parcelas: '))
    if quantidade_parcelas >= 3:
        juros = compra * ( 20 / 100)
        total_juros = compra + juros
        print(f'Sua compra de R${compra:.2f} parcelado em {quantidade_parcelas} terá um juros de 20%: {juros}')
        print(f'Valor com juros: R${total_juros:.2f}')
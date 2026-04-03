valores = []

while True:
    valor = (input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')
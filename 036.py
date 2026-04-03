valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite sua renda mensal: '))
tempo = int(input('Em quantos anos você vai pagar: '))

parcela = valor_casa / (tempo * 12)
minimo = salario * 30 / 100

if parcela <= minimo:
    print(f'Para pagar uma de R${valor_casa:2f} em {tempo} anos a prestação será de R${parcela:.2f}')
    print(f'\033[0;32;42mEmpréstimo concedido!\033[0m')
else:
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {tempo} anos a prestação será de R${parcela:.2f}')
    print(f'\033[0;31;41mEmpréstimo negado!\033[0m')
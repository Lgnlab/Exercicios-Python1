salario = float(input('Digite seu salário atual R$'))
aumento = salario * (15 / 100)
salarionovo = aumento + salario
print(f'Salário atual R${salario:.2f}\nAumento R${aumento:.2f}\nNovo salário R${salarionovo:.2f}')
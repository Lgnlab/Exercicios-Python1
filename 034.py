salario = float(input('Digite o seu salário atual para ver seu aumento: '))

if salario > 1250:
    aumento1 = salario * 0.1     #CALCULO: (SALARIO * 15 / 100)
    soma1 = salario + aumento1
    print(f'Seu salário atual é: R${salario:.2f}')
    print(f'Você teve um aumento de 10%: R${aumento1:.2f}')
    print(f'Novo salário: R${soma1:.2f}')
if salario < 1250 or salario == 1250:
    aumento2 = salario * 0.15     #CALCULO: (SALARIO * 10 / 100)
    soma2 = salario + aumento2
    print(f'Seu salário atual é: R${salario:.2f}')
    print(f'Você teve um aumento de 15%: R${aumento2:.2f}')
    print(f'Novo salário: R${soma2:.2f}')
from datetime import date 
ano_atual = date.today().year
ano = int(input('Digite seu ano de nascimeto: '))
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')

if idade == 18:
    print(f'Quem nasceu em {ano} tem {idade} em {ano_atual}')
    print('Você tem que se alistar \033[0;31;41mIMEDIATAMENTE\033[m')
elif idade < 18:
    alistamento = 18 - idade
    print(f'Ainda faltam {alistamento} anos para o alistamento')
    falta = ano_atual + alistamento
    print(f'Seu alistamento será em {falta}')
elif idade > 18:
    alistamento2 = idade - 18
    print(f'Você deveria ter se alistado há {alistamento2} anos')
    perdeu = ano_atual - alistamento2
    print(f'Seu alistamento foi em {perdeu}')



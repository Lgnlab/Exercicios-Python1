def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade > 65:
        print(f'Com {idade} anos: Voto OPCIONAL.')
    else:
        print(f'Com {idade} anos: Voto OBRIGATÓRIO.')

nasc = int(input('Em que ano você nasceu? '))
voto(nasc)

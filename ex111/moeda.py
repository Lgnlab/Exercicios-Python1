def aumentar(n = 0, percentual = 0, formato=False):
    calculo = n + (n * percentual / 100)
    return calculo if formato is False else moeda(calculo)


def diminuir(n = 0,percentual = 0, formato=False):
    calculo = n - (n * percentual / 100)
    return calculo if formato is False else moeda(calculo)


def dobro(n = 0, formato=False):
    calculo = n * 2
    return calculo if formato is False else moeda(calculo)


def metade(n = 0, formato=False):
    calculo = n / 2
    return calculo if formato is False else moeda(calculo)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, paumento = 0, pdiminuindo = 0, formato=False):
    print('-' * 25)
    print(f'{"RESUMO DO VALOR":>20}')
    print('-' * 25)
    print(f'Dobro do preço: {dobro(n, True)}')
    print(f'Metade do preço: {metade(n, True)}')
    calculo = n + (n * paumento / 100)
    print(f'{paumento}% de aumento: {moeda(calculo)}')
    calculo = n - (n * pdiminuindo / 100)
    print(f'{pdiminuindo}% de redução: {moeda(calculo)}')
    print('-' * 25)
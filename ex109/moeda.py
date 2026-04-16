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

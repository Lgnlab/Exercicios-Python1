def aumentar(n = 0, percentual = 0):
    calculo = n + (n * percentual / 100)
    return calculo


def diminuir(n = 0,percentual = 0):
    calculo = n - (n * percentual / 100)
    return calculo


def dobro(n = 0):
    calculo = n * 2
    return calculo


def metade(n = 0):
    calculo = n / 2
    return calculo


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

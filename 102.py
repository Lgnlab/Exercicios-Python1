def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: Mostra o passo a passo do cálculo ou não
    :return: O fatorial
    """
    fat = 1
    print('-' * 24)
    for calculo in range(num, 0, -1):
        if show:
            print(calculo, end='')
            if calculo > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= calculo
    return fat


print(fatorial(5,show=True))
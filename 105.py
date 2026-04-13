def notas(*num, sit=False):
    """
    -> Função para analisar notas
    :param num: números do alunos
    :param sit: determina a situação do aluno
    :return: os dados pedidos
    """
    r =dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num) / len(num)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa principal
dados = notas(5.5, 2.5, 8.5)
print(dados)
from random import randint
from time import sleep
from operator import itemgetter
resultado = dict()
resultado['jogador1'] = randint(1, 6)
resultado['jogador2'] = randint(1, 6)
resultado['jogador3'] = randint(1, 6)
resultado['jogador4'] = randint(1, 6)
ranking = list()
print('Valores Sorteados:')
for k,v in resultado.items():
        print(f'O {k} tirou {v}')
        sleep(1)
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)  #Ordena do maior para o menor
print('=' * 25)
for i, v in enumerate(ranking):
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')
        sleep(1)
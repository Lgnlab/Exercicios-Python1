import random, time
jogos = int(input('Quantos jogos você quer gerar? '))
#O random.sample(range(inicio, fim), quantidade de números) sorteia com um intervalo e limita a quantidade de números
print(f'{jogos} Jogo(s) Gerados:')
for c in range(1, jogos + 1):
    sorteio = random.sample(range(1, 61), 6)
    time.sleep(1)
    print(sorted(sorteio))
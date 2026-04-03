from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1, 10), randint(1,10))

for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO menor número sorteado foi: {min(numeros)}')  # min() informa o menor valor 
print(f'O maior número sorteado foi: {max(numeros)}')    # max() informa o maior valor 
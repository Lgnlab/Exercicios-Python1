lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    sair = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if sair == 'N':
        break
for c in lista:
    if c == 5:
        print('O número 5 está na lista!')

print('O número 5 não está na lista!')
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')

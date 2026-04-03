lista = []

for valor in range(0, 5):
    numero = int(input('Digite um valor: '))
    if valor == 0:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    elif numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')
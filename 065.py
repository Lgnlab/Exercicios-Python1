escolha = 'S'
media = soma = quanti = maior = menor = 0

while escolha in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quanti += 1
    if quanti == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero 
        if numero < menor:
            menor = numero 
    escolha = str(input('Quer continuar[s/n]: ')).upper().strip()[0]
media = soma / quanti
print(f'Você digitou {quanti} números e a média ficou {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

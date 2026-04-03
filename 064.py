numero = soma = contador = 0
numero = int(input('Digite um número [Digite 999 para parar]: '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [Digite 999 para parar: ')) #Usado para parar o programa sem soma o flag
print(f'Você digitou {contador} vezes e a soma total é {soma}')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('\033[31mNúmero inválido! Tente novamente.\033[m')
for i, c in enumerate(extenso):
    if numero == i:
        print(f'Você digitou o número {numero} que por extenso fica {c}')
    
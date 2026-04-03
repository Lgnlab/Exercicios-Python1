velocidade = int(input('Digite a valocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Velocidade máxima ultrapassada!')
    print(f'Multa de R${multa:.2f} aplicada!')
print('Velocidade máxima de 80km respeitada!')
viagem = float(input('De quantos KM será sua viagem: '))

if viagem <= 200:
    valor1 = viagem * 0.50
    print(f'O valor total da sua viagem de {viagem:.1f}KM vai ser R${valor1:.2f}')
elif viagem > 200:
    valor2 = viagem * 0.45
    print(f'O valor total da sua viagem de {viagem:.1f}KM vai ser R${valor2:.2f}')
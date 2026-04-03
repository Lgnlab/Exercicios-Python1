carro = float(input('Quantos KM o carro percorreu: '))
dias = int(input('Quantos dias o carro ficou alugado: '))
total = (dias * 60) + carro * 0.15
print('Dia: R$60,00 / KM rodados: R$0,15')
print(f'KM percorridos: {carro:.1f}\nDias com o carro: {dias}\nValor final: R${total:.2f}')
primeiro = int(input('Primeiro termo: '))  #INICIO DA CONTAGEM
razao = int(input('Razão: '))              #NÚMERO PARA PULAR E SOMAR 

for c in range(10):
    termo = primeiro + (c * razao)  #Do 1 ao 10 * razão
    print(termo, end=' -> ')
print('\033[0;32mFIM\033[m')
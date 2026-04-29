from rich import print, align
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
console = Console()

class Produto:
    def __init__(self, nome='Vazio', valor=0):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        texto = Align.center(f'{self.nome} \nR${self.valor:,.2f}')
        caixa = Panel(texto, title='Produto', width=30, height=5)
        print(caixa)



p1 = Produto('Computador', 5_000)
p1.etiqueta()
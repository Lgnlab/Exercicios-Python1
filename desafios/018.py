from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo='Vazio', quantidade=0):
        self.titulo = titulo
        self.quantidade = quantidade

    def __str__(self):
        return f"Esse é {self.titulo} com {self.quantidade} pessoas participando."

    def analisar(self):
        caixa = Panel(f'Analisando o [green]{self.titulo}[/] com {self.quantidade} [blue]convidados[/]\nCada participante comerá 0.4kg e cada kg custa R$82.40\nRecomendo [blue]comprar {self.quantidade * 0.4:.3f}kg[/] de carne\nO custo total será de [green]R${(self.quantidade * 0.4) * 82.40:.2f}[/]\nCada pessoa pagará [yellow]R${(self.quantidade * 0.4 * 82.40) / self.quantidade:.2f}[/] para participar.', title=self.titulo)
        print(caixa)


c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()
from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome='Vazio', nick='Vazio'):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)


    def ficha(self):
        conteudo = f"Nome real: [blue on black] {self.nome} [/]"
        conteudo += f"\nJogos Favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        caixa = Panel(conteudo, title=f"Jogador {self.nick}", width=45)
        print(caixa)

j1 = Gamer('Lucas Gabriel Do Nascimento', 'Lgn')
j1.add_favoritos('GTA 5')
j1.add_favoritos('Sonic')
j1.add_favoritos('Mario Bros')
j1.add_favoritos('Gof of War')
j1.ficha()

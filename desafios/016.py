from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f':hand: Olá, sou [blue bold]{self.nome}[/] e sou [yellow bold]{self.cargo}[/] do setor de [red bold]{self.setor}[/]'

c1 = Funcionario('Lucas', 'TI', 'Programador')
print(c1.apresentar())
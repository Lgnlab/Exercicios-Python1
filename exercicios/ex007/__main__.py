from rich import print, inspect
from classes import Aluno, Professor, Funcionario

a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()


p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()


f1 = Funcionario("Lucas", 25, "Programador", "TI")
f1.fazer_aniversario()
f1.bater_ponto()

a1.estudar()
p1.estudar()
f1.estudar()
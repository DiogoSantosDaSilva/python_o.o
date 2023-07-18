"""
Herança simples - Relações entre classes
Associação - usa.
Agregação - tem
Composição - é dono de.
Herança - é um.

Herança vs Composição

Classe principal (Pessoa)
    -> seper class, base class, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class
"""


class Pessoa:

    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem sai da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'Aluno'
    ...


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)

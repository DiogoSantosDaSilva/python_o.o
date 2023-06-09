"""
Class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instanciais) que 
podem ter seus próprios atributos e metodos, 
Os objetos gerados pela classe podem usar dados 
internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de 
classes.
"""
# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joana'
print(p2.nome)
print(p2.sobrenome)

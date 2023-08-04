"""
dataclasses - O que são dataclasses?
O módulo dataclasses fornece um decorador e funções para cria métodos com
__init__(), __pepr__(), __eq__() (entre outros) em classes definidas pelo
usuário.
Em resumo: dataclasses são syntax sugar para criar classes normais.
foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc: https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    print(p1 == p2)

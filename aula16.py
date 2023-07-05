"""
Relações entre classes associação, agregação e composição
Associação é um tipo de relação onde os objetos
estão ligados dentro do sistema.
Essa é a relação mais comum entre os objetos e tem subconjuntos
como agregação e composição (que veremos depois).
Geralemte, temos uma associação quando um objeto tem
um atributo que referência outro objeto.
A associação não especifica como um objeto controla
o ciclo de vida de outro objeto.
"""


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina')
escritor.ferramenta = maquina_de_escrever


print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
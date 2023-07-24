#   Método especial __call__
#   callable é algo que poder ser excutado com parênteses
#   Em classes normais, __call__ faz a instância de uma
#   classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 1234


call1 = CallMe('81984526256')
retorno = call1('Diogo')
print(retorno)

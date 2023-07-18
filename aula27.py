# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    pass


class AnotherError(Exception):
    pass


def up():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('look at note 1')
    exception_.add_note('you mistake this')
    raise exception_


try:
    up()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('I will launch again')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('one more note')
    raise exception_ from error

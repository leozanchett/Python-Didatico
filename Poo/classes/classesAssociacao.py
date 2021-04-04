class Escritor:
    def __init__(self, _anome):
        self.__nome = _anome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, _aferramenta):
        self.__ferramenta = _aferramenta

class Caneta:
    def __init__(self, _amarca):
        self.__marca = _amarca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaqEscrever:
    @staticmethod
    def escrever():
        print('MaqEscrever está escrevendo...')
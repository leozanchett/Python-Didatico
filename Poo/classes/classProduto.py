class Produto:
    def __init__(self, _anome, _apreco):
        self.nome = _anome
        self.preco = _apreco

    def desconto(self, _apercentual):
        self.preco = self.preco - (self.preco * (_apercentual / 100))

    # Getters
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    # Setters
    @nome.setter
    def nome(self, _avalor):
        self._nome = _avalor.title()

    @preco.setter
    def preco(self, _avalor):
        valortratado = ''
        self._preco = _avalor
        if isinstance(_avalor, str):
            for x in range(len(_avalor)):
                if _avalor[x].isnumeric():
                    valortratado = valortratado + str(_avalor[x])
        if len(valortratado) > 0:
            self._preco = float(valortratado)
        else:
            self._preco = float(_avalor)
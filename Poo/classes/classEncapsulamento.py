# _ 1 underline protected (convenção)
# __ 2 underline privado (convenção)

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, _aid, _anome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {_aid: _anome}
        else:
            self.__dados['clientes'].update({_aid: _anome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, _aid):
        del self.__dados['clientes'][_aid]
class CarinhoCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, _aproduto):
        self.produtos.append(_aproduto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print(total)

    def __del__(self):
        print('Carinho foi apagado')


class Produto:
    def __init__(self, _anome, _avalor):
        self.nome = _anome
        self.valor = _avalor

    def __del__(self):
        print('Produto foi apagado')
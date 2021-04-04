class Cliente:
    def __init__(self, _anome, _aidade):
        self.nome = _anome
        self.idade = _aidade
        self.enderecos = []

    def insere_endereco(self, _andereco):
        self.enderecos.append(_andereco)

    def lista_enderecos(self):
        for end in self.enderecos:
            print(end.cidade, end.uf)

    def lista_info_cliente(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}')

    def __del__(self):
        print(f'{self.nome} foi apagado da memória')

class Endereco:
    def __init__(self, _acidade, _auf):
        self.cidade = _acidade
        self.uf = _auf

    def __del__(self):
        print(f'{self.cidade} ({self.uf}) foi apagado da memória')
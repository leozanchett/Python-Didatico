class HPessoa:
    def __init__(self, _anome, _aidade):
        self.nome = _anome
        self.idade = _aidade
        self.nomeClasse = self.__class__.__name__
        self.apresentaInformacaoCadastro()

    def apresentaInformacaoCadastro(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}\nClasse: {self.nomeClasse}\n'+'='*40)

    def falar(self):
        print(f'{self.nome} está falando')

class HCliente(HPessoa):
    def __del__(self):
        print(f'{self.nomeClasse} foi deletada')

    def comprar(self):
        print(f'{self.nomeClasse} comprando...')


class HAluno(HPessoa):
    def __del__(self):
        print(f'{self.nomeClasse} foi deletada')

    def estudar(self):
        print(f'{self.nomeClasse} estudando...')
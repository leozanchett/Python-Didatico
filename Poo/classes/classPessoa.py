from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, _aassunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {_aassunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, _aalimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo {_aalimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        self.comendo = False
        print(f'{self.nome} parou de comer ')

    def get_ano_nasciment(self):
        return self.ano_atual - self.idade
from classes.classPessoa import Pessoa

def exemploPessoa():
    p2 = Pessoa('Creide', 32)
    p1 = Pessoa('Raul', 1)
    p1.comer('Maçã')
    p1.falar('Aliens')
    p1.comer('Maçã')
    p1.parar_comer()
    p1.falar('Aliens')
    p1.comer('Pera')
    p1.parar_falar()
    p1.parar_falar()
    p1.comer('Pera')
    print(f'{p1.ano_atual} é o ano atual')
    print(f'{p1.nome} nasceu em {p1.get_ano_nasciment()}')
    print(f'{p2.nome} nasceu em {p2.get_ano_nasciment()}')

if __name__ == '__main__':
    exemploPessoa()


from classes.classPessoa import Pessoa
from classes.classProduto import Produto
from classes.classVariaveisDeClasse import A


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
    p3 = Pessoa.por_ano_nascimento('Maria', 1992)
    print(f'{p3.nome} tem {p3.idade} anos')
    print(f'Número do id: {Pessoa.gera_id()} ')

def exemploProdutos():
    prod = Produto('leITE', 10)
    prod.desconto(50)
    print(f'Nome: {prod.nome} | Valor: R$ {prod.preco}')
    prod2 = Produto('CaNECA', 'R$100asdsa')
    prod2.desconto(50)
    print(f'Nome: {prod2.nome} | Valor: R$ {prod2.preco}')

def exemploVariaveisDeClasse():
    a1 = A()
    a2 = A()
    # A.vc = 321 # muda o valor da váriavel de classe para todos os objetos
    a2.vc = 321
    print(a1.vc)
    print(a2.vc)
    print(a2.__dict__)
    print(A.vc)

if __name__ == '__main__':
    # exemploPessoa()
    # exemploProdutos()
    exemploVariaveisDeClasse()


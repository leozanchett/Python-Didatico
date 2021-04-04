from classes.classesAssociacao import Escritor, Caneta, MaqEscrever
from classes.classPessoa import Pessoa
from classes.classProduto import Produto
from classes.classVariaveisDeClasse import A
from classes.classEncapsulamento import BaseDeDados


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

def encapsulamento():
    bd = BaseDeDados()
    bd.inserir_cliente(1, 'Leo')
    bd.inserir_cliente(2, 'Rose')
    bd.inserir_cliente(3, 'Miranda')
    bd.lista_clientes()
    print('=' * 40)
    bd.apaga_cliente(2)
    bd.lista_clientes()
    # quando há dois underlines é criado uma nova variável de classe
    bd.__dados = 'Outra coisa'
    print(bd.__dados)
    # para acessar a variável real da classe, é necessário declarar desta maneira:
    print(bd._BaseDeDados__dados)

def exemploAssociacao():
    escrit = Escritor('Joaozin')
    caneta = Caneta('bic')
    maq = MaqEscrever()
    print(escrit.nome)
    print(caneta.marca)
    caneta.escrever()
    maq.escrever()

    escrit.ferramenta = caneta
    escrit.ferramenta.escrever()
    del escrit
    #print(escrit)  # aqui gera exceção pois o objeto escrit não existe mais na memória
    print(caneta.marca) # o porém de fazer esse tipo de associação é que o objeto caneta ainda fica existindo na memória.

if __name__ == '__main__':
    # ver sobre packages
    # exemploPessoa()
    # exemploProdutos()
    # exemploVariaveisDeClasse()
    # exemploEncapsulamento
    # encapsulamento()
    exemploAssociacao()



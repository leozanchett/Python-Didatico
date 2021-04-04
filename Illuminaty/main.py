class Piramide:
    def __init__(self, _aalturaMaxima):
        self.alturaMaxima = _aalturaMaxima

    def desenhaPiramideInvertida(self):
        for x in range(self.alturaMaxima):
            colunas = ''
            for y in range(self.alturaMaxima - x):
                colunas = colunas + '*' + ' '
            print(' ' * x + colunas)

    def desenhaPiramide(self):
        for x in range(self.alturaMaxima):
            colunas = ''
            for y in range(x):
                colunas = colunas + '*' + ' '
            print(' ' * (self.alturaMaxima - x) + colunas)

if __name__ == '__main__':
    piramide = Piramide(10)
    piramide.desenhaPiramideInvertida()
    piramide.desenhaPiramide()
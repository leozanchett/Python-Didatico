import pygame
from uteis.style import AZUL_CLARO

class ConfigTela:
    def __init__(self):
        pygame.init()
        self.width = 840
        self.heigth = 480
        self.tela = pygame.display.set_mode([self.width, self.heigth])
        pygame.display.set_caption('Ninja 2D')
        self.tela.fill(AZUL_CLARO)
        self.keys = None
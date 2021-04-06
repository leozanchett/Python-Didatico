import pygame
from uteis.style import AZUL_CLARO

class ConfigTela:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode([840, 480])
        pygame.display.set_caption('Ninja 2D')
        self.display.fill(AZUL_CLARO)

    def corTelaDefault(self):
        self.display.fill(AZUL_CLARO)

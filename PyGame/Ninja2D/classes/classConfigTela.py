import pygame
from uteis.style import CINZA_CLARO

class ConfigTela:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode([840, 480])
        pygame.display.set_caption('KILL THEM ALL')
        self.display.fill(CINZA_CLARO)
        self.clock = pygame.time.Clock()

    def corTelaDefault(self):
        self.display.fill(CINZA_CLARO)

import pygame
from uteis.style import WHITE


class ConfigTela:
    def configsIniciais(self):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode([840, 480])
        pygame.display.set_caption('Ninja 2D')
        self.DISPLAY.fill(WHITE)

    def __init__(self):
        DISPLAY = pygame.display.set_mode([840, 480])
        self.configsIniciais()
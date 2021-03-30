import pygame
from classes.classCoresTela import *


class DisplayGame:
    def __init__(self):
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((700, 400), 0, 32)
        self.DISPLAYSURF.fill(WHITE)
        pygame.display.set_caption('Titulo do jogo!')

    def desenhacirculo(self):
        pygame.draw.circle(self.DISPLAYSURF, BLUE, (300, 50), 20, 0)

    def desenhapoligono(self):
        pygame.draw.polygon(self.DISPLAYSURF, BLUE, ((186, 0), (331, 106), (276, 277), (96, 277), (40, 106)))

    def desenhaz(self):
        pygame.draw.line(self.DISPLAYSURF, RED, (60, 60), (120, 60), 4)
        pygame.draw.line(self.DISPLAYSURF, RED, (120, 60), (60, 120))
        pygame.draw.line(self.DISPLAYSURF, RED, (60, 120), (120, 120), 4)

    def elipses(self):
        pygame.draw.ellipse(self.DISPLAYSURF, RED, (300, 250, 40, 80), 1)

    def rect(self):
        pygame.draw.rect(self.DISPLAYSURF, RED, (400, 150, 200, 50))
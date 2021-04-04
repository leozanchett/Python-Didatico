import sys

import pygame

from classes.classConfigTela import ConfigTela
from uteis.style import WHITE


class Acoes(ConfigTela):

    def aplicarCorDefault(self):
        self.tela.fill(WHITE)

    def diminuirTela(self):
        self.DISPLAY = pygame.display.set_mode([300, 400])
        self.aplicarCorDefault()

    @staticmethod
    def fecharJogo():
        print('Fechou o jogo !')
        pygame.quit()
        sys.exit()
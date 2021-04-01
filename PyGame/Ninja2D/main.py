
import pygame
from pygame.locals import *

from classes.classAcoes import Acoes
from classes.classConfigTela import ConfigTela


if __name__ == '__main__':
    configTela = ConfigTela()
    acoesJogo = Acoes()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                acoesJogo.fecharJogo()
        pygame.display.update()


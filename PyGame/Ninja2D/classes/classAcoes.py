import sys

import pygame


class Acoes:
    @staticmethod
    def fecharJogo():
        pygame.quit()
        sys.exit()

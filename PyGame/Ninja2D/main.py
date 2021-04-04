
import pygame
from pygame.locals import *

from classes.classAcoes import Acoes

if __name__ == '__main__':
    controleAcoes = Acoes()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                Acoes().fecharJogo()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Acoes().fecharJogo()
                elif event.key == pygame.K_w:
                    print('Apertou o W')
            elif event.type == KEYUP:
                print('Soltou a tecla')
        controleAcoes.keys = pygame.key.get_pressed() # Captura os eventos de tecla pressionada
        if controleAcoes.keys[pygame.K_w]:
            print('Segurando W')
            
        pygame.display.update()
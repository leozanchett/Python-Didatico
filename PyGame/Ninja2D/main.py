import pygame

from classes.classConfigTela import ConfigTela
from classes.classEfeitosSonoros import Som
from classes.classNave import NavePrincipal
from pygame.locals import *

if __name__ == '__main__':
    tela = ConfigTela()
    som = Som()
    objectGroup = pygame.sprite.Group()
    personagem = NavePrincipal(objectGroup)
    # personagem2 = PersonagemPrincipal(objectGroup)
    # personagem2.rect = pygame.Rect(50, 250, 100, 100)
    while True:
        tela.clock.tick(60) # frames por segundo
        for event in pygame.event.get():
            if event.type == QUIT:
                tela.fecharJogo()
        tela.corTelaDefault()
        objectGroup.update()
        objectGroup.draw(tela.display)
        # pygame.key.get_pressed()  # Captura os eventos de tecla pressionada
        pygame.display.update()

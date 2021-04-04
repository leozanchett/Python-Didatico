
import pygame

from classes.classAcoes import Acoes
from classes.classPersonagem import Personagem

if __name__ == '__main__':
    personagem = Personagem()
    controleAcoes = Acoes(personagem)
    while True:
        for event in pygame.event.get():
            controleAcoes.eventtype(event)
        controleAcoes.escutaKeyPressed(pygame.key.get_pressed()) #Captura os eventos de tecla pressionada
        controleAcoes.desenharRostoPersonagem()
        pygame.display.update()
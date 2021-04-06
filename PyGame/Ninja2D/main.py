import pygame

from classes.classAcoes import Acoes
from classes.classConfigTela import ConfigTela
from classes.classEfeitosSonoros import Som
from classes.classPersonagem import Personagem

if __name__ == '__main__':
    tela = ConfigTela()
    som = Som()
    personagem = Personagem(som)
    personagem.desenharRostoPersonagem(tela)
    controleAcoes = Acoes(personagem, tela)
    while True:
        for event in pygame.event.get():
            controleAcoes.eventtype(event)
        controleAcoes.escutaKeyPressed(pygame.key.get_pressed())  # Captura os eventos de tecla pressionada
        pygame.display.update()

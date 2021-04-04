import sys

import pygame

from classes.classConfigTela import ConfigTela
from classes.classPersonagem import Personagem
from uteis.style import WHITE
from pygame.locals import *


class Acoes(ConfigTela):

    def __init__(self, _aPersonagem):
        self.player = _aPersonagem

    def eventtype(self, _aevento):
        if _aevento.type == QUIT:
            self.fecharJogo()
        elif _aevento.type == KEYDOWN:
            self.keydown(_aevento.key)
        elif _aevento.type == KEYUP:
            self.keyup()

    def desenharRostoPersonagem(self):
        self.player.personagem.image = pygame.image.load( self.player.imagemRosto())
        #redimensiona a imagem.
        self.player.personagem.image = pygame.transform.scale(self.player.personagem.image, [100, 100])
        self.player.personagem.rect = pygame.Rect(50, 50, 100, 100)
        self.player.drawGroup.draw(self.tela)

    def desenharRetangulo(self):
        retangulo = pygame.Rect(0, 0, 200, 100)  # left / top / width / heigth
        retangulo.center = [self.tela.get_width() / 2, self.tela.get_height() / 2]
        pygame.draw.rect(self.tela, [255, 255, 255, 255], retangulo)

    def aplicarCorDefault(self):
        self.tela.fill(WHITE)

    def diminuirTela(self):
        self.DISPLAY = pygame.display.set_mode([300, 400])
        self.aplicarCorDefault()

    def keydown(self, _aKey):
        if _aKey == pygame.K_ESCAPE:
            Acoes().fecharJogo()
        elif _aKey == pygame.K_w:
            print('pressiona W')
        elif _aKey == pygame.K_q:
            self.desenharRostoPersonagem()
            #self.desenharRetangulo()

    def escutaKeyPressed(self, _akey):
        self.keys = _akey
        if self.keys[pygame.K_w]:
            print('Segurando W')

    @staticmethod
    def fecharJogo():
        print('Fechou o jogo !')
        pygame.quit()
        sys.exit()

    @staticmethod
    def keyup():
        print('Soltou a tecla')

import sys

import pygame

from classes.classConfigTela import ConfigTela
from classes.classPersonagem import Personagem
from uteis.style import WHITE
from pygame.locals import *


class Acoes():

    def __init__(self, _aPersonagem, _aTela):
        self.personagem = _aPersonagem
        self.tela = _aTela

    def eventtype(self, _aevento):
        if _aevento.type == QUIT:
            self.fecharJogo()
        elif _aevento.type == KEYDOWN:
            self.keydown(_aevento.key)
        elif _aevento.type == KEYUP:
            self.keyup()

    def desenharRostoPersonagem(self):
        self.personagem.sprite.image = pygame.image.load(self.personagem.imagemRosto())
        #redimensiona a imagem.
        self.personagem.sprite.image = pygame.transform.scale(self.personagem.sprite.image, [100, 100])
        self.personagem.sprite.rect = pygame.Rect(50, 50, 100, 100)
        self.personagem.drawGroup.draw(self.tela.display)

    def keydown(self, _aKey):
        if _aKey == pygame.K_ESCAPE:
            self.fecharJogo()
        elif _aKey == pygame.K_w:
            print('pressiona W')

    def escutaKeyPressed(self, _akey):
        if _akey[pygame.K_d]:
            self.personagem.sprite.rect.x += 1
        if _akey[pygame.K_a]:
            self.personagem.sprite.rect.x -= 1
        if _akey[pygame.K_s]:
            self.personagem.sprite.rect.y += 1
        if _akey[pygame.K_w]:
            self.personagem.sprite.rect.y -= 1
        self.tela.corTelaDefault()
        self.personagem.drawGroup.draw(self.tela.display)


    @staticmethod
    def fecharJogo():
        print('Fechou o jogo !')
        pygame.quit()
        sys.exit()

    @staticmethod
    def keyup():
        print('Soltou a tecla')

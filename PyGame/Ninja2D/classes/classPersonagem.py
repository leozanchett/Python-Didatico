import pygame
from pathlib import Path


class Personagem():
    diretorio = 'images'

    def __init__(self, _asom):
        self.drawGroup = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.drawGroup)
        self.som = _asom

    @classmethod
    def imagemRosto(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorio+'/rosto.png'
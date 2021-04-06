import pygame
from pathlib import Path


class Personagem():
    diretorio = 'images'

    def __init__(self, _asom):
        self.drawGroup = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.drawGroup)
        self.som = _asom

    def desenharRostoPersonagem(self, _atela):
        self.sprite.image = pygame.image.load(self.imagemRosto())
        #redimensiona a imagem.
        self.sprite.image = pygame.transform.scale(self.sprite.image, [100, 100])
        self.sprite.rect = pygame.Rect(50, 50, 100, 100)
        self.drawGroup.draw(_atela.display)

    @classmethod
    def imagemRosto(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorio+'/rosto.png'
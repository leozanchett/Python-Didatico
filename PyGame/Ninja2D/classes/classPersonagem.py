import pygame
from pathlib import Path


class Personagem():
    def __init__(self):
        self.drawGroup = pygame.sprite.Group()
        self.personagem = pygame.sprite.Sprite(self.drawGroup)

    @staticmethod
    def imagemRosto():
        path = Path().cwd().as_posix()
        path = path + '/images/rosto.png'
        return path
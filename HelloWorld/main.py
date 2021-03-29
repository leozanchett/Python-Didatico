import sys

from pygame.locals import *
from classes.classDesignTela import *

DisplayGame = DisplayGame()

DisplayGame.desenhapoligono()
DisplayGame.desenhaz()
DisplayGame.desenhacirculo()
DisplayGame.elipses()
DisplayGame.rect()

pixObj = pygame.PixelArray(DisplayGame.DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



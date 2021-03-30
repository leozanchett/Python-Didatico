import sys

from pygame.locals import *
from classes.classDesignTela import *

'''DisplayGame = DisplayGame()

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
    pygame.display.update() '''

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Hello World!')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2)
while True:  # main game loop
    DISPLAYSURF.fill(GREEN)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

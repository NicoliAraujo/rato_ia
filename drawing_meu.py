'''
Created on 13 de mai de 2017

@author: nicoli
'''
'''
Created on 13 de mai de 2017

@author: nicoli
'''
import pygame, sys
from pygame import *
  
pygame.init()
  
# set up the window
width = 900
height = 1200
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Drawing')
  
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
  
  
dict_salas = {0: ((0,0),(width/3,height/4)),
                      1: ((width/3,0), (2*width/3,height/4)),
                      2: ((2*width/3,0), (width,height/4)),
                      3: ((0,height/4), (width/3,height/2)),
                      4: ((0,height/2), (width/3,3*height/4)),
                      5: ((0,3*height/4), (width/3,height)),
                      6: ((width/3,height/4), (2*width/3,height)),
                      7: ((2*width/3,3*height/4), (width,height)),
                      8: ((2*width/3,height/2), (width,3*height/4)),
                      9: ((2*width/3,height/4) ,(width,height/2))}


# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,width,height))
#sala 0
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[0])
#sala 1
pygame.draw.lines(DISPLAYSURF,  BLACK, False, dict_salas[1])
#sala 2
pygame.draw.lines(DISPLAYSURF,  BLACK, False, dict_salas[2])
#sala 3
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[3])
#sala 4
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[4])
#sala 5
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[5])
#sala 6
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[6])
#sala 7
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[7])
#sala 8
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[8])
#sala 9
pygame.draw.lines(DISPLAYSURF, BLACK, False, dict_salas[9])
       
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[380][280] = BLACK
pixObj[382][282] = BLACK
pixObj[384][284] = BLACK
pixObj[386][286] = BLACK
pixObj[388][288] = BLACK
del pixObj
  
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
  
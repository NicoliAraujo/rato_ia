'''
Created on 28 de mar de 2017

@author: nicoli
'''

import time as tm
import pygame as pg

import sys
from rato import markov_rato
from pygame import *
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BROWN = (139,  69,  19)
class canvas():
    def __init__(self):
        self.width = 600
        self.height = 600
        self.jerry = pg.image.load('./img/rato.jpg')
        self.cheese = pg.image.load('./img/cheese.png')
        self.jerry = pg.transform.scale(self.jerry, (80,80))
        self.cheese = pg.transform.scale(self.cheese, (80,80))
        pg.init()
        self.screen = pg.display.set_mode((self.width,self.height))
        pg.display.set_caption("Rato IA")
        
                
        self.dict_salas = self.cria_dict_salas(self.width, self.height)
        self.dict_portas = self.cria_dict_portas(self.width, self.height)
        self.dict_centro_salas = self.cria_dict_centro_salas(self.width, self.height)
        
        self.mark_rato = markov_rato()
        
    def cria_dict_salas(self, width, height):
        dict_salas = {0: (0,0,width/3,height/4),
                      1: (width/3,0,2*width/3,height/4),
                      2: (2*width/3,0,width,height/4),
                      3: (0,height/4,width/3,height/2),
                      4: (0,height/2,width/3,3*height/4),
                      5: (0,3*height/4,width/3,height),
                      6: (width/3,height/4,2*width/3,height),
                      7: (2*width/3,3*height/4,width,height),
                      8: (2*width/3,height/2,width,3*height/4),
                      9: (2*width/3,height/4,width,height/2)}
        
        return dict_salas
    
    def cria_dict_portas(self, width, height):
        dict_portas = {1: ((int(width/9), height/4), 
                           (int(2*width/9), height/4)),
                       2: ((int(width/3), int(height/12)), 
                            (int(width/3), int(height/6))),
                       3: ((int(7*width/9), int(height/4)), 
                           (int(8*width/9), int(height/4))),
                       4: ((width/3, int(height/3)),
                           (width/3, int(5*height/12))),
                       5: ((2*width/3, int(height/3)),
                           (2*width/3, int(5*height/12))),
                       6: ((width/3, int(7*height/12)), 
                           (width/3, int(2*height/3))),
                       7: ((2*width/3, int(7*height/12)), 
                           (2*width/3, int(2*height/3))),
                       8:((width/3, int(5*height/6)), 
                          (width/3, int(11*height/12))),
                       9: ((int(7*width/9), int(3*height/4)), 
                           (int(8*width/9), int(3*height/4)))}
        return dict_portas
    
    def cria_dict_centro_salas(self, width, height):
        dict_centro_salas = {0: (int(width/6)-50, int(height/8)-50),
                             1: (int(width/2)-50, int(height/8)-50),
                             2: (int(5*width/6)-50, int(height/8)-50),
                             3: (int(width/6)-50, int(3*height/8)-50),
                             4: (int(width/6)-50, int(5*height/8)-50),
                             5: (int(width/6)-50, int(7*height/8)-50),
                             6: (int(width/2)-50, int(5*height/8)-50),
                             7: (int(5*width/6)-50, int(height/8)-50),
                             8: (int(5*width/6)-50, int(5*height/8)-50),
                             9: (int(5*width/6)-50, int(3*height/8)-50)}
        return dict_centro_salas
    
    def cria_pequenos(self, filename):
        img = pg.image.load(filename).convert()
        return img.subsurface((3,3,30-3,30-3))
    
    def preenche_canvas(self):
        self.screen.fill(WHITE)
        pg.draw.rect(self.screen, BLACK, (0,0,self.width,self.height), 10)
        #sala 0
        pg.draw.rect(self.screen, BLACK, self.dict_salas[0], 10)
        #sala 1
        pg.draw.rect(self.screen,  BLACK, self.dict_salas[1], 10)
        #sala 2
        pg.draw.rect(self.screen,  BLACK, self.dict_salas[2], 10)
        
        #sala 3
        pg.draw.rect(self.screen, BLACK, self.dict_salas[3], 10)
        #sala 4
        pg.draw.rect(self.screen, BLACK, self.dict_salas[4], 10)
        #sala 5
        pg.draw.rect(self.screen, BLACK, self.dict_salas[5], 10)
        #sala 6
        pg.draw.rect(self.screen, BLACK, self.dict_salas[6], 10)
        #sala 7
        pg.draw.rect(self.screen, BLACK, self.dict_salas[7], 10)
        #sala 8
        pg.draw.rect(self.screen, BLACK, self.dict_salas[8], 10)
        #sala 9
        pg.draw.rect(self.screen, BLACK, self.dict_salas[9], 10)
    
        self.abre_portas()
    
    def abre_portas(self):
        #PORTA 1
        pg.draw.line(self.screen, WHITE, self.dict_portas[1][0], self.dict_portas[1][1], 12)
        #porta 2
        pg.draw.line(self.screen, WHITE, self.dict_portas[2][0], self.dict_portas[2][1], 12)
        #porta 3
        pg.draw.line(self.screen, WHITE, self.dict_portas[3][0], self.dict_portas[3][1], 12)
        #Porta 4
        pg.draw.line(self.screen, WHITE, self.dict_portas[4][0], self.dict_portas[4][1], 12)
        #porta 5
        pg.draw.line(self.screen, WHITE, self.dict_portas[5][0], self.dict_portas[5][1], 12)
        #porta 6
        pg.draw.line(self.screen, WHITE, self.dict_portas[6][0], self.dict_portas[6][1], 12)
        #porta 7
        pg.draw.line(self.screen, WHITE, self.dict_portas[7][0], self.dict_portas[7][1], 12)
        #porta 8
        pg.draw.line(self.screen, WHITE, self.dict_portas[8][0], self.dict_portas[8][1], 12)
        #porta 9
        pg.draw.line(self.screen, WHITE, self.dict_portas[9][0], self.dict_portas[9][1], 12)
    
    def fecha_porta(self, porta):
        if porta!=None:
            pg.draw.line(self.screen, BROWN, self.dict_portas[porta][0], self.dict_portas[porta][1], 12)
    def caminha(self, saida, chegada):
        self.preenche_canvas()
        local = saida
        self.screen.blit(self.jerry,self.dict_centro_salas[local])
        self.screen.blit(self.cheese, self.dict_centro_salas[chegada])
        local_ant=None
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
            while local != chegada:
                self.preenche_canvas()
                self.screen.blit(self.cheese, self.dict_centro_salas[chegada])
                local_ant = local
                local = self.mark_rato.sorteia(local)
                self.screen.blit(self.jerry,self.dict_centro_salas[local])
                self.fecha_porta(self.mark_rato.fecha_porta(local_ant, local))
                
                self.mark_rato.mat[local_ant][local]+=1
                
                pg.display.update()
                tm.sleep(1)
        self.mark_rato.set_matriz()
        self.mark_rato.multiplica_mat()
        self.mark_rato.salva_mat()
    
    '''def abre_porta(self, sala_saida, sala_chegada):
        porta = self.rato'''
if __name__=='__main__':
    
    
    
    c = canvas()
    #c.cria_canvas() 
    c.caminha(0,2)
        
        
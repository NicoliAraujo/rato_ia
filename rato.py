# -*- coding: utf-8 -*-
'''
Created on 8 de mar de 2017

@author: pibic-elloa-nicoli
'''
import numpy as np
import random

class rato(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.vizinhança = {0:[1,3],
                           1:[0],
                           2:[9],
                           3:[0,6],
                           4:[6],
                           5:[6],
                           6:[3,4,5,8,9],
                           7:[8],
                           8:[6,7],
                           9:[6,2]}
        
        self.vizinhança_mudada=self.vizinhança.copy()
    def sorteia(self, saida):
        return random.choice(self.vizinhança_mudada[saida])

    def fecha_porta(self, porta_ant, porta):
        self.vizinhança_mudada=self.vizinhança.copy()
        #print('fecha_porta ', self.vizinhança[porta], porta_ant, porta)
        if porta_ant!=None:
            if len(self.vizinhança[porta_ant])==1:
                self.vizinhança_mudada[porta].remove(porta_ant)
    
class markov_rato():
    def __init__(self, rato):
        self.rato = rato
        self.dict_trans = rato.vizinhança
        tam = len(self.dict_trans)
        self.mat = np.zeros((tam,tam))
        self.mat_markov = np.zeros((tam, tam))
    
    
    
    def caminha(self, saida, chegada):
        local = saida
        local_ant=None
        while local != chegada:
            local_ant = local
            local = self.rato.sorteia(local)
            self.rato.fecha_porta(local, local_ant)
            self.mat[local_ant][local]+=1
        print(self.mat)
    
    def set_matriz(self):
        for saida in self.dict_trans:
            for chegada in self.dict_trans[saida]:
                self.mat[saida][chegada] = 1
        
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                self.mat_markov[i][j] = self.mat[i][j]/self.mat[i].sum()
        
    def multiplica_mat(self, threshold=0.00005):
        dif = 10
        while dif>threshold:
            val_1 = self.mat_markov.sum()
            self.mat_markov = self.mat_markov*self.mat_markov
            dif = val_1 - self.mat_markov.sum()
    def salva_mat(self):
        with open('cadeia_markov.txt', 'w') as file:
            for line in self.mat_markov:
                file.write(str(line)+'\n')
            
if __name__ == '__main__':
    meu_rato = rato()
    
    mark_rato = markov_rato(meu_rato)
    mark_rato.caminha(0, 9)
    '''mark_rato.set_matriz()
    mark_rato.multiplica_mat()
    mark_rato.salva_mat()
    '''
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
        
    def sorteia(self, saida):
        return random.choice(self.vizinhança[saida])
    
    def caminha(self, saida, chegada):
        local = saida
        while local != chegada:
            local = self.sorteia(local)
            print(local)
    
class markov_rato():
    def __init__(self, dict_trans):
        self.dict_trans = dict_trans
        tam = len(dict_trans)
        self.mat = np.zeros((tam,tam))
        self.mat_markov = np.zeros((tam, tam))
    def set_matriz(self):
        for saida in self.dict_trans:
            print(saida)
            for chegada in self.dict_trans[saida]:
                self.mat[saida][chegada] = 1
        
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                self.mat_markov[i][j] = self.mat[i][j]/self.mat[i].sum()
        print(self.mat, '\n', self.mat_markov)
    
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
    meu_rato.caminha(1, 7)
    mark_rato = markov_rato(meu_rato.vizinhança)
    mark_rato.set_matriz()
    mark_rato.multiplica_mat()
    mark_rato.salva_mat()
    
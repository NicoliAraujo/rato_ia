# -*- coding: utf-8 -*-
'''
Created on 8 de mar de 2017

@author: pibic-elloa-nicoli
'''
import numpy as np
import random

    
class markov_rato():
    def __init__(self):
        
        self.dict_trans = self.set_dict_trans()
        self.dict_trans_mudado = self.dict_trans.copy()
        self.dict_portas = self.set_dict_portas()
        tam = len(self.dict_trans)
        self.mat = np.zeros((tam,tam))
        self.mat_markov = np.zeros((tam, tam))
    
    def set_dict_portas(self):
        dict_portas = {1: [0,3],
                       2: [0,1],
                       3: [2,9],
                       4: [3,6],
                       5: [6,9],
                       6: [4,6],
                       7: [6,8],
                       8: [5,6],
                       9: [8,7]}
        return dict_portas
    def set_dict_trans(self):
        dict_trans = {0:[1,3],
                       1:[0],
                       2:[9],
                       3:[0,6],
                       4:[6],
                       5:[6],
                       6:[3,4,5,8,9],
                       7:[8],
                       8:[6,7],
                       9:[6,2]}
        return(dict_trans)
    
    def sorteia(self, saida):
        return random.choice(self.dict_trans_mudado[saida])

    def fecha_porta(self, porta_ant, porta):
        self.dict_trans_mudado=self.dict_trans.copy()
        #print('fecha_porta ', self.vizinhança[porta], porta_ant, porta)
        if porta_ant!=None:
            if len(self.dict_trans[porta_ant])==1:
                self.dict_trans_mudado[porta].remove(porta_ant)
                for key in self.dict_portas:
                    if porta_ant in self.dict_portas[key]:
                        return(key)

    def caminha(self, saida, chegada):
        local = saida
        local_ant=None
        while local != chegada:
            local_ant = local
            local = self.sorteia(local)
            self.fecha_porta(local, local_ant)
            self.mat[local_ant][local]+=1
        #print(self.mat)
        
    def cria_mat_prob_rato(self):
        dict_prob={}
        for sala in self.dict_trans:
            dict_prob[sala] = [i for i in self.dict_trans[sala]], [self.mat_markov[i] for i in self.dict_trans[sala]]
        print(dict_prob)
        return dict_prob
    
    def set_matriz(self):

        for i in range(len(self.mat)):
            if self.mat[i].sum()!=0:
                for j in range(len(self.mat)):
                    self.mat_markov[i][j] = self.mat[i][j]/self.mat[i].sum()
        #print(self.mat_markov)
        
    def multiplica_mat(self, threshold=0.00005):
        dif = 10
        while dif>threshold:
            #print(self.mat_markov.sum())
            val_1 = self.mat_markov.sum()
            self.mat_markov = self.mat_markov*self.mat_markov
            dif = val_1 - self.mat_markov.sum()
            #print(val_1, dif)
        #self.mat_markov = round(self.mat_markov, 3)
    def salva_mat(self):
        with open('cadeia_markov.txt', 'w') as file:
            for line in self.mat_markov:
                file.write(str(line)+'\n')

if __name__ == '__main__':
    
    mark_rato = markov_rato()
    mark_rato.caminha(0, 9)
    mark_rato.set_matriz()
    mark_rato.multiplica_mat()
    mark_rato.salva_mat()
    
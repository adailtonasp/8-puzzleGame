# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:39:20 2019

@author: adail
"""

import copy

class Puzzle:
    
    def __init__(self,initState):
        self.nullPosition = []
        self.mat = initState
        self.n = len(self.mat)
        for i in range(0, len(self.mat)):
           for j in range(0, len(list(self.mat[0]))):
               if self.mat[i][j] == -1:
                   self.nullPosition = [i,j]
                   break
        
    def move_down(self): #generate_for = 0
        if self.nullPosition[0] + 1 > self.n - 1:
            return [1, None] #não é possivel realizar a operação, pois ultrapassa o limte da matriz
        else:
            novoEstado = copy.deepcopy(self)
            aux = novoEstado.mat[novoEstado.nullPosition[0] + 1][novoEstado.nullPosition[1]] #armazena o valor que está na futura posicao do espaco vazio em aux
            novoEstado.mat[novoEstado.nullPosition[0] + 1][novoEstado.nullPosition[1]] = -1
            novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1]] = aux #armazena o valor de aux na antiga posicao do espaco vazio
            novoEstado.nullPosition[0] += 1  # atualizar a posicao do espaco vazio
            return [0, novoEstado]
        
    def move_up(self): #generate_for = 1
        if self.nullPosition[0] - 1 < 0:
            return [1, None]
        else:
            novoEstado = copy.deepcopy(self)
            aux = novoEstado.mat[novoEstado.nullPosition[0] - 1][novoEstado.nullPosition[1]]
            novoEstado.mat[novoEstado.nullPosition[0] - 1][novoEstado.nullPosition[1]] = -1
            novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1]] = aux
            novoEstado.nullPosition[0] -= 1
            return [0, novoEstado]
    
    def move_right(self): #generate_for = 2
        if self.nullPosition[1] + 1 >= self.n:
            return [1, None]
        else:
            novoEstado = copy.deepcopy(self)
            aux = novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1] + 1]
            novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1] + 1] = -1
            novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1]] = aux
            novoEstado.nullPosition[1] += 1
            return [0, novoEstado]
   
    def move_left(self): #generate_for = 3
        if self.nullPosition[1] - 1 < 0:
            return [1, None]
        else:
            novoEstado = copy.deepcopy(self)
            aux = novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1] - 1]
            novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1] - 1] = -1
            novoEstado.mat[novoEstado.nullPosition[0]][novoEstado.nullPosition[1]] = aux
            novoEstado.nullPosition[1] -= 1
            return [0, novoEstado]

    def compare(self,estadoFinal):
        for i in range(0,len(self.mat)):
            for j in range(0,len(self.mat[i])):
                if(self.mat[i][j] != estadoFinal[i][j]):
                    return 1
        return 0 
     
    
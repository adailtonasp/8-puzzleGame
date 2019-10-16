# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:38:42 2019

@author: adail
"""
import numpy as np
#from std import puzzle

#pai é o nó pai
#puzzle_state é um objeto puzzle com o estado corrente do jogo
#generate_from é a operação que foi feita no pai que fez gerar esse filho
#   -1 - significa que ele é o root
#   0 - significa que foi feita uma operação move_down
#   1 - significa que foi feita uma operação move_up
#   2 - significa que foi feita uma operação move_right
#   3 - significa que foi feita uma operação move_left

class Node:
    
    def __init__(self,pai,statePuzzle,generateFrom,custo,profundidade,funcaoCusto):
        self.pai = pai
        self.statePuzzle = statePuzzle
        self.generateFrom = generateFrom
        self.custo = custo #quantas operações foram realizadas até chegar a esse nó - vamos considerar como o g(n)
        self.profundidade = profundidade #em que nível se encontra o nó
        self.filhos = [] #lista de nós filhos
        self.listaDeNodes = []
        self.funcaoCusto = funcaoCusto # f (n) = g (n) + h (n)  

### Métodos de Largura
    
    def findIndex(self,estadoFinal,ele):
        auxLista = []
        for i in range(0,len(estadoFinal)):
            for j in range(0,len(estadoFinal)):
                if estadoFinal[i][j] == ele:
                    auxLista.append(i)
                    auxLista.append(j)
                    return auxLista
        return auxLista        


    def avalia_funcao_custo(self,puzzleFilho):
        #calcula distancia de manhattan
        manhattanSoma = 0
    
        for i in range(0,len(puzzleFilho.mat)):
            for j in range(0,len(puzzleFilho.mat)):
    
                auxLista = self.findIndex(self.estadoFinal,puzzleFilho.mat[i][j])
                
                manhattanSoma += (np.abs(i - auxLista[0]) + np.abs(j - auxLista[1]))
                
        return manhattanSoma 
    
    def avalia_funcao_custo2(self,puzzleFilho):
        aux = 0;
        for i in range(0,len(self.estadoFinal)):
            for j in range(0,len(self.estadoFinal[0])):
                if(puzzleFilho.mat[i][j] != self.estadoFinal[i][j]):
                    aux = aux + 1
        return aux
    
    def move_up(self):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]:
            auxCusto = self.custo + len(self.listaDeNodes) + 1
            auxNode = Node(self,auxPuzzle[1],0,auxCusto,self.profundidade + 1,self.avalia_funcao_custo(auxPuzzle[1] ) + auxCusto)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
    
    def move_down(self):
        auxPuzzle = self.statePuzzle.move_down()
        if not auxPuzzle[0]:
            auxCusto = self.custo + len(self.listaDeNodes) + 1
            auxNode = Node(self,auxPuzzle[1],1,auxCusto,self.profundidade + 1,self.avalia_funcao_custo(auxPuzzle[1] ) + auxCusto)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
    
    def move_right(self):
        auxPuzzle = self.statePuzzle.move_right()
        if not auxPuzzle[0]:
            auxCusto = self.custo + len(self.listaDeNodes) + 1
            auxNode = Node(self,auxPuzzle[1],2,auxCusto,self.profundidade + 1,self.avalia_funcao_custo(auxPuzzle[1] ) + auxCusto)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
    
    def move_left(self):
        auxPuzzle = self.statePuzzle.move_left()
        if not auxPuzzle[0]:
            auxCusto = self.custo + len(self.listaDeNodes) + 1
            auxNode = Node(self,auxPuzzle[1],3,auxCusto,self.profundidade + 1,self.avalia_funcao_custo(auxPuzzle[1] ) + auxCusto)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
            
    def set_filhos(self,listaDeNodes,estadoFinal):
        self.listaDeNodes = listaDeNodes
        self.estadoFinal = estadoFinal
        #os generate_from é estabelecido aqui!!
        
        #se o estado foi gerado de um move_down, por exemplo, não se pode aplicar a operacao contraria
        #, no caso, o move_up, pois isso expandira nos repetidos sem necessidade
        
        if self.generateFrom == 0: #significa que foi gerado por um move_up então não faca move_down!
            #move_up
            self.move_up()
            #move_right
            self.move_right()
            #move_left    
            self.move_left()
        elif self.generateFrom == 1:
            #move_down
            self.move_down()
            #move_right    
            self.move_right()
            #move_left
            self.move_left()
        elif self.generateFrom == 2:
            #move_up
            self.move_up()
            #move_down
            self.move_down()
            #move_right
            self.move_right()
        elif self.generateFrom == 3:
             #move_up
            self.move_up()             
            #move_down
            self.move_down()
            #move_left
            self.move_left()
        else: #caso seja o root!
            #move_up
            self.move_up()             
            #move_down
            self.move_down()
            #move_right
            self.move_right()
            #move_left
            self.move_left()

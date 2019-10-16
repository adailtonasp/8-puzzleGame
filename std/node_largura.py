# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:38:42 2019

@author: adail
"""

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
    
    def __init__(self,pai,statePuzzle,generateFrom,custo,profundidade):
        self.pai = pai
        self.statePuzzle = statePuzzle
        self.generateFrom = generateFrom
        self.custo = custo #quantas operações foram realizadas até chegar a esse nó
        self.profundidade = profundidade #em que nível se encontra o nó
        self.filhos = [] #lista de nós filhos
        self.listaDeNodes = []

### Métodos de Largura
    
    def move_up(self,visitList):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxNode = Node(self,auxPuzzle[1],"move_up",self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
                self.filhos.append(auxNode)
                self.listaDeNodes.append(auxNode)
    
    def move_down(self,visitList):
        auxPuzzle = self.statePuzzle.move_down()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxNode = Node(self,auxPuzzle[1],"move_down",self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
                self.filhos.append(auxNode)
                self.listaDeNodes.append(auxNode)
    
    def move_right(self,visitList):
        auxPuzzle = self.statePuzzle.move_right()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxNode = Node(self,auxPuzzle[1],"move_right",self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
                self.filhos.append(auxNode)
                self.listaDeNodes.append(auxNode)
    
    def move_left(self,visitList):
        auxPuzzle = self.statePuzzle.move_left()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxNode = Node(self,auxPuzzle[1],"move_left",self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
                self.filhos.append(auxNode)
                self.listaDeNodes.append(auxNode)
            
    def set_filhos(self,listaDeNodes,visitList):
        self.listaDeNodes = listaDeNodes
        #os generate_from é estabelecido aqui!!
        
        #move_up
        self.move_up(visitList)             
        #move_down
        self.move_down(visitList)
        #move_right
        self.move_right(visitList)
        #move_left
        self.move_left(visitList)

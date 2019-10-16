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
    
    def move_up(self):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]:
            auxNode = Node(self,auxPuzzle[1],0,self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
    
    def move_down(self):
        auxPuzzle = self.statePuzzle.move_down()
        if not auxPuzzle[0]:
            auxNode = Node(self,auxPuzzle[1],1,self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
    
    def move_right(self):
        auxPuzzle = self.statePuzzle.move_right()
        if not auxPuzzle[0]:
            auxNode = Node(self,auxPuzzle[1],2,self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
    
    def move_left(self):
        auxPuzzle = self.statePuzzle.move_left()
        if not auxPuzzle[0]:
            auxNode = Node(self,auxPuzzle[1],3,self.custo + len(self.listaDeNodes) + 1,self.profundidade + 1)
            self.filhos.append(auxNode)
            self.listaDeNodes.append(auxNode)
            
    def set_filhos(self,listaDeNodes):
        self.listaDeNodes = listaDeNodes
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

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
#   0 - significa que foi feita uma operação move_up
#   1 - significa que foi feita uma operação move_down
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

### Métodos de Profundidade            

    def move_up(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]: # se o estado gerado for valido
            if not auxPuzzle[1].mat in visitList:
               # if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
#                else:
#                    self.lag = 1

    def move_down(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_down()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
               if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
               else:
                   self.flag = 1 
            
    
    def move_right(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_right()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                else:
                    self.flag = 1
            
    
    def move_left(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_left()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                else:
                    self.flag = 1
                    
    def set_filhos(self,visitList,moveList,estadoFinal):
#        print("visitList" + str(visitList) + "\n")
        self.auxCusto = self.custo
        self.estadoFinal = estadoFinal
        #os generate_from é estabelecido aqui!!
        self.flag = 0
        #move_up
        self.move_up(visitList,moveList)             
        #move_down
        self.move_down(visitList,moveList)
        #move_right
        self.move_right(visitList,moveList)
        #move_left
        self.move_left(visitList,moveList)
        
        if self.flag:
            aux = moveList.pop()
            moveList.clear()
            moveList.append(aux)
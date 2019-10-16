# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:38:42 2019

@author: adail
"""

class Node:
    
    def __init__(self,pai,statePuzzle,generateFrom,custo,profundidade):
        self.pai = pai
        self.statePuzzle = statePuzzle
        self.generateFrom = generateFrom
        self.custo = custo #quantas operações foram realizadas até chegar a esse nó
        self.profundidade = profundidade #em que nível se encontra o nó
        self.filhos = [] #lista de nós filhos

    def checkElements(self,estadoFinal,statePuzzle,moveList):
        for i in range (0,len(statePuzzle.mat)):
            for j in range(0,len(statePuzzle.mat[0])):
                if not ([i,j] in moveList):
                    if not (statePuzzle.mat[i][j] == estadoFinal[i][j]):
                        return False
        return True

    def move_up(self,visitList,moveList,estadoFinal):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]: # se o estado gerado for valido
            if not auxPuzzle[1].mat in visitList:  # se o estado gerado já nao foi expandido anteriormente
                auxPosition = auxPuzzle[1].nullPosition
                if not auxPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                else:
                   if self.checkElements(estadoFinal,auxPuzzle[1],moveList):
                      self.auxCusto += 1
                      auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                      self.filhos.append(auxNode)
                   else:
                      visitList.append(auxPuzzle[1].mat)
                      self.flag = 1

    def move_down(self,visitList,moveList,estadoFinal):
        auxPuzzle = self.statePuzzle.move_down()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxPosition = auxPuzzle[1].nullPosition
                if not auxPosition in moveList:
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                else:
                   if self.checkElements(estadoFinal,auxPuzzle[1],moveList):
                      self.auxCusto += 1
                      auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                      self.filhos.append(auxNode)
                   else:
                      visitList.append(auxPuzzle[1].mat)
                      self.flag = 1

    def move_right(self,visitList,moveList,estadoFinal):
        auxPuzzle = self.statePuzzle.move_right()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxPosition = auxPuzzle[1].nullPosition
                if not auxPosition in moveList:
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                else:
                   if self.checkElements(estadoFinal,auxPuzzle[1],moveList):
                      self.auxCusto += 1
                      auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                      self.filhos.append(auxNode)
                   else: 
                      visitList.append(auxPuzzle[1].mat)
                      self.flag = 1

    def move_left(self,visitList,moveList,estadoFinal):
        auxPuzzle = self.statePuzzle.move_left()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                auxPosition = auxPuzzle[1].nullPosition
                if not auxPosition in moveList:
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                else:
                   if self.checkElements(estadoFinal,auxPuzzle[1],moveList):
                      self.auxCusto += 1
                      auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                      self.filhos.append(auxNode)
                   else:
                      visitList.append(auxPuzzle[1].mat)
                      self.flag = 1
                      
    def set_filhos(self,visitList,moveList,estadoFinal):
        self.auxCusto = self.custo
        self.flag = 0
        #move_up
        self.move_up(visitList,moveList,estadoFinal)
        #move_down
        self.move_down(visitList,moveList,estadoFinal)
        #move_right
        self.move_right(visitList,moveList,estadoFinal)
        #move_left
        self.move_left(visitList,moveList,estadoFinal)
        if self.flag:
            moveList.clear()
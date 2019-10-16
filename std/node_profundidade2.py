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
    
    def __init__(self,pai,statePuzzle,generateFrom,custo,profundidade,restrict):
        self.pai = pai
        self.statePuzzle = statePuzzle
        self.generateFrom = generateFrom
        self.custo = custo #quantas operações foram realizadas até chegar a esse nó
        self.profundidade = profundidade #em que nível se encontra o nó
        self.filhos = [] #lista de nós filhos
        self.restrict = restrict
        
    def checkElements(self,statePuzzle,moveList):
        for i in range (0,len(statePuzzle.mat)):
            for j in range(0,len(statePuzzle.mat[0])):
                if not ([i,j] in moveList):
                    if not (statePuzzle.mat[i][j] == self.estadoFinal[i][j]):
                        return 1
        return 0;                

    #funcao que  procura um estado pai que tem o nullPosition passado como paramento
    def findState(self,auxPosition,auxPuzzle,moveList,visitList):
        auxState = auxPuzzle.pai
        while auxState.statePuzzle.nullPosition != auxPosition:
            auxState = auxState.pai
        return auxState    
### Métodos de Profundidade            
            
    def move_up(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]: # se o estado gerado for valido
            if not auxPuzzle[1].mat in visitList:  # se o estado gerado já nao foi expandido anteriormente
                if self.restrict:
                         self.auxCusto += 1
                         auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                         auxNode.restrict = True
                         self.filhos.append(auxNode)
                elif not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                    moveList.append(auxPuzzle[1].nullPosition)
                else:
                    #checkar se o elementos que nao estao em loop estao nas posicoes corretas
                    if not self.checkElements(auxPuzzle[1],moveList):
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                        auxNode.restrict = True
                        self.filhos.append(auxNode)
                    else:
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                        self.filhos.append(auxNode)
                        moveList.append(auxPuzzle[1].nullPosition)

    def move_down(self,visitList,moveList):
            auxPuzzle = self.statePuzzle.move_down()
            if not auxPuzzle[0]: # se o estado gerado for valido
                if not auxPuzzle[1].mat in visitList:  # se o estado gerado já nao foi expandido anteriormente
                    if self.restrict:
                         self.auxCusto += 1
                         auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                         auxNode.restrict = True
                         self.filhos.append(auxNode)
                    elif not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                        self.filhos.append(auxNode)
                        moveList.append(auxPuzzle[1].nullPosition)
                    else:
                        #checkar se o elementos que nao estao em loop estao nas posicoes corretas
                        if not self.checkElements(auxPuzzle[1],moveList):
                            self.auxCusto += 1
                            auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                            auxNode.restrict = True
                            self.filhos.append(auxNode)
                        else:
                            self.auxCusto += 1
                            auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                            self.filhos.append(auxNode)
                            moveList.append(auxPuzzle[1].nullPosition)

    def move_right(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]: # se o estado gerado for valido
            if not auxPuzzle[1].mat in visitList:  # se o estado gerado já nao foi expandido anteriormente
                if self.restrict:
                         self.auxCusto += 1
                         auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                         auxNode.restrict = True
                         self.filhos.append(auxNode)
                elif not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                    moveList.append(auxPuzzle[1].nullPosition)
                else:
                    #checkar se o elementos que nao estao em loop estao nas posicoes corretas
                    if not self.checkElements(auxPuzzle[1],moveList):
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                        auxNode.restrict = True
                        self.filhos.append(auxNode)
                    else:
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                        self.filhos.append(auxNode)
                        moveList.append(auxPuzzle[1].nullPosition)
    
    def move_left(self,visitList,moveList):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]: # se o estado gerado for valido
            if not auxPuzzle[1].mat in visitList:  # se o estado gerado já nao foi expandido anteriormente
                if self.restrict:
                         self.auxCusto += 1
                         auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                         auxNode.restrict = True
                         self.filhos.append(auxNode)
                elif not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                    self.auxCusto += 1
                    auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                    self.filhos.append(auxNode)
                    moveList.append(auxPuzzle[1].nullPosition)
                else:
                    #checkar se o elementos que nao estao em loop estao nas posicoes corretas
                    if not self.checkElements(auxPuzzle[1],moveList):
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                        auxNode.restrict = True
                        self.filhos.append(auxNode)
                    else:
                        self.auxCusto += 1
                        auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                        self.filhos.append(auxNode)
                        moveList.append(auxPuzzle[1].nullPosition)
                
    def set_filhos(self,visitList,moveList,estadoFinal):
        self.auxCusto = self.custo
        self.estadoFinal = estadoFinal
        
        if self.restrict:
            auxPosition = self.statePuzzle.nullPosition
            if auxPosition[0]-1 in moveList: #equivalente ao move_up
               self.move_up(visitList,moveList)
               
            if auxPosition[0]+1 in moveList: #equivalente ao move_down
               self.move_down(visitList,moveList)
               
            if auxPosition[1]+1 in moveList: #equivalente ao move_right
               self.move_right(visitList,moveList) 
               
            if auxPosition[1]-1 in moveList: #equivalente ao move_left
               self.move_lefts(visitList,moveList) 
        else:
            #move_up
            self.move_up(visitList,moveList)
            #move_down
            self.move_down(visitList,moveList)
            #move_right
            self.move_right(visitList,moveList)
            #move_left
            self.move_left(visitList,moveList)
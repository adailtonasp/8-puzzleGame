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

### Método Guloso
    def findIndex(self,estadoFinal,ele):
        auxLista = []
        for i in range(0,len(estadoFinal)):
            for j in range(0,len(estadoFinal)):
                if estadoFinal[i][j] == ele:
                    auxLista.append(i)
                    auxLista.append(j)
                    return auxLista
        return auxLista        


    def avalia2(self,nodeFilho):
        #calcula distancia de manhattan
        manhattanSoma = 0
    
        for i in range(0,len(nodeFilho.statePuzzle.mat)):
            for j in range(0,len(nodeFilho.statePuzzle.mat)):
    
                auxLista = self.findIndex(self.estadoFinal,nodeFilho.statePuzzle.mat[i][j])
                
                manhattanSoma += (abs(i - auxLista[0]) + abs(j - auxLista[1]))
              
        return manhattanSoma * self.avalia(nodeFilho)


    #avalia o estado do filho de acordo com  a quantidade de células que estão fora do lugar
    def avalia(self,estadoFilho):
        aux = 0
        for i in range(0,len(self.estadoFinal)):
            for j in range(0,len(self.estadoFinal)):
                if estadoFilho.statePuzzle.mat[i][j] != self.estadoFinal[i][j]:
                    aux += 1
        return aux
          
    def move_up(self,visitList):
        auxPuzzle = self.statePuzzle.move_up()
        if not auxPuzzle[0]: # se o estado gerado for valido
            if not auxPuzzle[1].mat in visitList:
                #if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                self.auxCusto += 1
                auxNode = Node(self,auxPuzzle[1],"move_up",self.auxCusto,self.profundidade + 1)
                self.filhos.append(auxNode)


    def move_down(self,visitList):
        auxPuzzle = self.statePuzzle.move_down()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                #if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                self.auxCusto += 1
                auxNode = Node(self,auxPuzzle[1],"move_down",self.auxCusto,self.profundidade + 1)
                self.filhos.append(auxNode)
  
    
    def move_right(self,visitList):
        auxPuzzle = self.statePuzzle.move_right()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                #if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                self.auxCusto += 1
                auxNode = Node(self,auxPuzzle[1],"move_right",self.auxCusto,self.profundidade + 1)
                self.filhos.append(auxNode)

            
    
    def move_left(self,visitList):
        auxPuzzle = self.statePuzzle.move_left()
        if not auxPuzzle[0]:
            if not auxPuzzle[1].mat in visitList:
                #if not auxPuzzle[1].nullPosition in moveList:  # se o nullPosition já esteve nessa posição antes
                self.auxCusto += 1
                auxNode = Node(self,auxPuzzle[1],"move_left",self.auxCusto,self.profundidade + 1)
                self.filhos.append(auxNode)

                    
    def set_filhos(self,estadoFinal,visitList):
        #print(visitList)
        self.auxCusto = self.custo
        self.estadoFinal = estadoFinal
        #os generate_from é estabelecido aqui!!
        self.flag = 0
        #move_up
        self.move_up(visitList)             
        #move_down
        self.move_down(visitList)
        #move_right
        self.move_right(visitList)
        #move_left
        self.move_left(visitList)

        #ordena
        self.filhos.sort(key = self.avalia2)
        self.filhos.reverse()
        
        for i in self.filhos:
            print(i.statePuzzle.mat)
            print(self.avalia2(i))
        
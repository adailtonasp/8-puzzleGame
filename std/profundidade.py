# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:54:14 2019

@author: adail
"""

import random

class Profundidade:

    def __init__(self, root,estadoFinal):
        self.listaDeNodes = []
        self.listaDeNodes.append(root)
        self.estadoFinal = estadoFinal
        self.visitList = [] #lista que guarda todos os estados ja visitados
        self.moveList = []
        self.teste_lista()
        
    def teste_lista(self):
        arq = open('output_Profundidade.txt','w')
        arq.write("Busca em Profundidade\n")
        while(True):
            elementoAtual = self.listaDeNodes.pop()
            print(elementoAtual.statePuzzle.mat) #  <----PRINT
            #vamos gravar as saidas no arquivo
            if elementoAtual.generateFrom == "move_up":
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_up custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")
            elif elementoAtual.generateFrom == "move_down":
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_down custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")   
            elif elementoAtual.generateFrom == "move_right":
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_right custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")    
            elif elementoAtual.generateFrom == "move_left":
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_left custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")
            else:
                arq.write(str(elementoAtual.statePuzzle.mat) + " generate_from: root\n")
               
            if not elementoAtual.statePuzzle.compare(self.estadoFinal):
                #o elementoAtual possui o estado final!!
                arq.write("Estado final encontrado!!!\nCusto = " + str(elementoAtual.custo) + "\nProfundidade = " + str(elementoAtual.profundidade)) 
                arq.close()
                print("O elementoAtual possui o estado final!!\n")
                return elementoAtual
            else:
                #o elementoAtual nao é o estado final devemos expandir seus filhos
                #os nós criados sáo adicionas a listadeNodes dentro do for
                self.visitList.append(elementoAtual.statePuzzle.mat)
                elementoAtual.set_filhos(self.visitList,self.moveList,self.estadoFinal)
                print("Quantidade de filhos %d: "% (len(elementoAtual.filhos)))
                print("Quantidade nos em visitList %d: "% (len(self.visitList)))
                #embaralha os elementos para evitar loop
                #random.shuffle(elementoAtual.filhos)
                for i in elementoAtual.filhos:
                    self.listaDeNodes.append(i)
                arq.write("Número de nós da fronteira: " + str(len(self.listaDeNodes)) + " ")
        arq.close()
   

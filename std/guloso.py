# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:54:14 2019

@author: adail
"""

class Guloso:

    def __init__(self, root,estadoFinal):
        self.listaDeNodes = []
        self.listaDeNodes.append(root)
        self.estadoFinal = estadoFinal
        self.tempRoot = root.statePuzzle.nullPosition
        self.teste_lista()  
        
    def teste_lista(self):
        arq = open('output_Guloso.txt','w')
        arq.write("Busca Heurística - Busca Gulosa\n")
        while(True):
            elementoAtual = self.listaDeNodes.pop()
            print(elementoAtual.statePuzzle.mat) #  <----PRINT
            #vamos gravar as saidas no arquivo
            if elementoAtual.generateFrom == 0:
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_up custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")
            elif elementoAtual.generateFrom == 1:
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_down custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")   
            elif elementoAtual.generateFrom == 2:
                arq.writelines(str(elementoAtual.statePuzzle.mat) + " generate_from: move_right custo: " + str(elementoAtual.custo) + " profundidade: " + str(elementoAtual.profundidade) + "\n")    
            elif elementoAtual.generateFrom == 3:
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
                elementoAtual.set_filhos(self.estadoFinal)
                #os filhos são organizados em ordem decrescente de custo estimado dentro da função anterior!
                for i in elementoAtual.filhos:
                    self.listaDeNodes.append(i)
                arq.write("Número de nós da fronteira: " + str(len(self.listaDeNodes)) + " ")
        arq.close()
   

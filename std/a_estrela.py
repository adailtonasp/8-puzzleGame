# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:54:03 2019

@author: adail
"""

class A_estrela:

    def __init__(self, root,estadoFinal):
        self.listaDeNodes = []
        self.listaDeNodes.append(root)
        self.estadoFinal = estadoFinal
        self.teste_lista()
        
    def avalia_lista_node(self,elemento):
        return(elemento.funcaoCusto)
        
        
    def teste_lista(self):
        arq = open('output_A-estrela.txt','w')
        arq.write("Busca usando A-estrela\n")
        while(True):
            elementoAtual = self.listaDeNodes.pop(0)
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
                elementoAtual.set_filhos(self.listaDeNodes,self.estadoFinal)
                self.listaDeNodes.sort(key = self.avalia_lista_node)
                arq.write("Número de nós da fronteira: " + str(len(self.listaDeNodes)) + " ")
        arq.close()

      




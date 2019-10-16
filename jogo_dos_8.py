from tkinter import *
from tkinter import messagebox

from std import *

import time
#tamanho da fonte:
large_font = ('Verdana',30)

#estado final


'''cria a janela'''
janela = Tk()
janela['bg'] = '#5F9EA0'  
janela.title ("JOGO DOS 8")
caminho = []
entradas = []  # vetor de Entrys
init = []  # entrada dos algoritmos
opcoes = []  # vetor de radioButtons
saidas = [] # vetor para Labels
var = IntVar()  # valorar as opções


def fazCaminho(elementoFinal):
    #print("Faz Caminho")
    global caminho
    while(elementoFinal != None):
        #print(elementoFinal.statePuzzle.mat) #<---
        caminho.append(elementoFinal.statePuzzle.mat)
        elementoFinal = elementoFinal.pai
    caminho.reverse() 
    print("Imprimir Caminho")
    for i in caminho:
        print(i)
    
###### ALGORITMOS PARA PESQUISA #######
def runFB_largura():
    # ps: O init tem o vetor da forma que os algoritmos precisam pra rodar 
    global init
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]]
    print("largura\n")
    initPuzzle = puzzle.Puzzle(init)
    time1 = time.clock()
    root_largura = node_largura.Node(None,initPuzzle,"root",0,0)
    larguraAux = largura.Largura(root_largura,estadoFinal)
    elemento = larguraAux.teste_lista()
    time2 = time.clock()
    info["text"] = "Custo: " + str(elemento[0].custo) + "\nPronfundidade: " + str(elemento[0].profundidade) + "\nTamanho: " + str(len(elemento[1])) +"\nTempo: " + str(time2 - time1) + "\n"
    fazCaminho(elemento[0])
def runFB_profund():
    global init
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]]
    print("profundidade\n")
    time1 = time.clock()
    initPuzzle = puzzle.Puzzle(init)
    root_profundidade = node_profundidade.Node(None,initPuzzle,"root",0,0)
    profundidadeAux = profundidade.Profundidade(root_profundidade,estadoFinal)
    elemento = profundidadeAux.teste_lista()
    time2 = time.clock()
    info["text"] = "Custo: " + str(elemento[0].custo) + "\nPronfundidade: " + str(elemento[0].profundidade) + "\nTamanho: " + str(len(elemento[1])) +"\nTempo: " + str(time2 - time1) + "\n"
    fazCaminho(elemento[0])
def run_guloso():
    global init
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]]
    print("guloso\n")
    time1 = time.clock()
    initPuzzle = puzzle.Puzzle(init)
    root_guloso = node_guloso.Node(None,initPuzzle,"root",0,0)
    gulosoAux = guloso.Guloso(root_guloso,estadoFinal)
    elemento = gulosoAux.teste_lista()
    time2 = time.clock()
    info["text"] = "Custo: " + str(elemento[0].custo) + "\nPronfundidade: " + str(elemento[0].profundidade) + "\nTamanho: " + str(len(elemento[1])) +"\nTempo: " + str(time2 - time1) + "\n"
    fazCaminho(elemento[0])
def runFB_A_estrela():
    global init
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]]
    initPuzzle = puzzle.Puzzle(init)
    root_a_estrela = node_a_estrela.Node(None,initPuzzle,"root",0,0,-1)
    a_estrelaAux = a_estrela.A_estrela(root_a_estrela,estadoFinal)
    elemento = a_estrelaAux.teste_lista()
    info["text"] = "Custo: " + str(elemento[0].custo) + "\nPronfundidade: " + str(elemento[0].profundidade) + "\nTamanho: " + str(len(elemento[1]))
    fazCaminho(elemento[0])

#METODO PARA VERIFICAR DADOS DIGITADOS NAS ENTRADAS:
def verifica():  #Ok
    vetor =[]
    global entradas
    global init
    
    for i in range (9):  # verifica se todos os campos foram preenchidos e substitui o zero por -1
        if (entradas[i].get() == ''):
            vetor.append(-1)
        else:
            vetor.append(int(entradas[i].get()))
            
    for i in range(-1,9):  # verifica se tem todos os numeros validos
        if i != 0 and i not in vetor:
            return False
    aux =[]
    cont = 0;
    for i in range (3): # deixa o vetor de entradas da forma que as funções estão esperando
        for j in range(3):
            aux.append(vetor[cont])
            cont+=1
        init.append(aux)
        aux = []
    print(init)    
    return True

# AÇÕES DOS BOTÕES 
def gerarJogo(): #Ok
    global opcoes
    global init
    # verificação de validade dos dados digitados:
    if (verifica()):
        for i in range(4):
            opcoes[i]['state']='normal'
            opcoes[i].configure(background='white')
        fundo.configure(background='white')
        #print(init)
    else:
        messagebox.showinfo("DADOS INVALIDOS!", " dados invalidos! digite uma sequência de números válidos")

# REABILITAR COMANDO: 
def sel():  #Ok
    global var
    print(var.get())
    rumAlg['state']='normal'
    rumAlg.configure(background='white')

def rodaAlg():  # falta atualizar as informações depois que roda o algoritmo selecionado
    global var
    if var.get() == 1 :
        runFB_largura()
    elif var.get() ==2 :
        runFB_profund()
    elif var.get() == 3 :
        print("Executar Guloso\n")
        run_guloso()
    else:
        print("Executar a_estrela\n")
        runFB_A_estrela()
        
    simJogo['state']='normal'
    simJogo.configure(background='white')

def attSaida(i):
    global saidas
    saidas[0].configure(text = str(i[0][0]))
    saidas[1].configure(text = str(i[0][1]))
    saidas[2].configure(text = str(i[0][2]))
    saidas[3].configure(text = str(i[1][0]))
    saidas[4].configure(text = str(i[1][1]))
    saidas[5].configure(text = str(i[1][2]))
    saidas[6].configure(text = str(i[2][0]))
    saidas[7].configure(text = str(i[2][1]))
    saidas[8].configure(text = str(i[2][2]))

#def simulaJogo():  # falta tudo
#    print("simula Jogo")
#    global caminho # vetor de matrizes
#    global saidas
#    for i in caminho:  # para cada matriz
#        print("valor de i: "+ str(i))
##        for j in range (3):
##            print("valor de j: "+ str(j))
##            w = 0
##            print("valor de w: "+ str(w))
##            for x in range (3):
##                print("valor de x: "+ str(x))
###                saidas[j + x + w] = i[j][x]
##                saidas[j + x + w].configure(text = str(i[j][x]))
##            w += 2
#        attSaida(i)
#        time.sleep(1)
#        janela.update()
#        #caminho.pop()
    
def simulaJogo():  # falta tudo
    global caminho # vetor de matrizes
    for i in caminho:  # para cada matriz
        w = 0
        for j in range (3):
            for x in range (3):
                if(i[j][x] != -1):
                    saidas[w].configure(text = str(i[j][x]))
                else:
                    saidas[w].configure(text = "")  #não coloca nada para representar o vazio
                w+=1
        time.sleep(1)
        janela.update()


def limpar():
    global init
    global saidas
    global caminho
    init.clear()
    caminho.clear()
    #limpa as saidas
    saidas[0].configure(text = '')
    saidas[1].configure(text = '')
    saidas[2].configure(text = '')
    saidas[3].configure(text = '')
    saidas[4].configure(text = '')
    saidas[5].configure(text = '')
    saidas[6].configure(text = '')
    saidas[7].configure(text = '')
    saidas[8].configure(text = '')

    for i in entradas:
        i.delete(0,END)
    info["text"] = "AINDA SEM INFORMAÇÕES!"
    for i in opcoes:
        i['state']='disabled'
        i.configure(background='#5F9EA0')
    fundo.configure(background='#5F9EA0')
    rumAlg['bg'] = '#5F9EA0'
    rumAlg.configure(state ='disabled')
    simJogo['bg'] = '#5F9EA0'
    simJogo.configure(state ='disabled')
    for i in saidas:
        i["text"] = ""
        

    
        
################################## funções para criar botões #################################
def criar_entradas():
    global entradas
    largura, altura,cont  = 40, 40, 0
    for i in range(3):
        for j in range(3):
            entradas.append(Entry(janela, font=large_font, justify = "center"))
            entradas[cont].place(width = 40, height= 40)
            entradas[cont].place(x=largura, y =altura)
            largura +=40
            cont+=1
        largura = 40
        altura +=40

def criar_opcoes():
    global var
    cont = 0
    aux = 1
    textos = ["Força Bruta(LARGURA)","Força Bruta(PROFUNDIDADE)","Busca Gulosa","           A*            "]
    for i in range (4):
        opcoes.append(Radiobutton(janela, text=textos[i], variable=var, value=aux, command=sel, state ='disabled'))
        opcoes[i].place(x=170, y=90 + cont)
        opcoes[i].configure(background='#5F9EA0')
        cont +=20
        aux +=1

def criar_saidas():
    global saidas
    largura, altura,cont  = 40, 260, 0
    for i in range(3):
        for j in range(3): 
            saidas.append( Label (janela, font=large_font, justify = "center"))
            saidas[cont].place(width = 39, height= 39)
            saidas[cont].place(x=largura, y =altura)
            largura +=40
            cont+=1
        largura = 40
        altura +=40

        
##########################   informações da tela #################################
lab = Label(janela,text ="INSERIR DADOS INICIAIS DO JOGO")
lab['bg'] =  '#00cccc'
lab.place(x=10, y=10)

criar_entradas()

# BOTÃO PARA GERAR O  JOGO 
gera =Button(janela, text='GERAR JOGO', command=gerarJogo)
gera.place(x=200, y=50)

# FUNDO DAS OPÇÕES:
fundo = Label(janela)
fundo.place(x=165, y=90)
fundo.place(width = 190, height= 85)
fundo['bg'] = '#5F9EA0'

criar_opcoes()

# BOTÃO PARA RODAR ALGORITMO:
rumAlg =Button(janela, text='RODAR ALGORITMO', command=rodaAlg)
rumAlg.place(x=180, y=180)
rumAlg['bg'] = '#5F9EA0'
rumAlg.configure(state ='disabled')

# AREA PARA PLOTAR INFORMAÇÕES OBTIDAS (LATERAL DIREITA)
lab2 = Label(janela,text ="INFORMAÇÕES OBTIDAS NA EXECUÇÃO:")
lab2['bg'] =  '#00cccc'
lab2.place(x=440, y=10)

info = Label(janela, text ="AINDA SEM INFORMAÇÕES!")
info.place(width = 400, height= 300)
info.place(x=360, y=40)

#AREA PARA PLOTAR SIMULAÇÃO DE EXECUÇÃO DO JOGO (CANTO INFERIOR ESQUERDO)
simJogo =Button(janela, text='RODAR SIMULAÇÃO', command=simulaJogo)
simJogo.place(x=40, y=230)
simJogo['bg'] = '#5F9EA0'
simJogo.configure(state ='disabled')

criar_saidas()

#BOTÃO PARA LIMPAR INFORMAÇÕES:
limpa = Button(janela, text='LIMPAR', command=limpar)
limpa.place(x=710, y=370)
#######################################################################################

#alterar tamanho
# LxA+e+t  
janela.geometry("770x400+250+60")
'''bloqueia a possibilidade de redimencionar a tela'''
janela.resizable(width=False, height=False)
janela.mainloop()

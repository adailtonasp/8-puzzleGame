from tkinter import *
from tkinter import messagebox

from std import *

#tamanho da fonte:
large_font = ('Verdana',30)

#variaveis para coordenada :
valX = 10
valY = 10

'''cria a janela'''
janela = Tk()
janela['bg'] = '#5F9EA0'  
janela.title ("JOGO DOS 8")

initState = []


#METODO PARA VERIFICAR DADOS DIGITADOS NAS ENTRADAS:
def verifica():
    global initState
    vetor = [ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), ent7.get(), ent8.get(), ent9.get()]
    if ('' in vetor):
        return False
    vetor = [int(ent1.get()), int(ent2.get()), int(ent3.get()), int(ent4.get()), int(ent5.get()), int(ent6.get()), int(ent7.get()), int(ent8.get()), int(ent9.get())]
    
    for i in range(-1, 9):
        if i == 0:
            return False
        if i not in vetor:
            return False
    initState = [[int(ent1.get()), int(ent2.get()), int(ent3.get())], [int(ent4.get()), int(ent5.get()), int(ent6.get())], [int(ent7.get()), int(ent8.get()), int(ent9.get())]]
    return True

# AÇÕES DOS BOTÕES 
def gerarJogo():
    # verificação de validade dos dados digitados:
    if (verifica()):
        R1['state']='normal'
        R1.configure(background='white')
        R2['state']='normal'
        R2.configure(background='white')
        R3['state']='normal'
        R3.configure(background='white')
        R4['state']='normal'
        R4.configure(background='white')
        fundo.configure(background='white')
    else:
        messagebox.showinfo("DADOS INVALIDOS!", " dados invalidos! digite uma sequencia de numeros validos")


# REABILITAR COMANDO: 
def sel():  #Ok
   rumAlg['state']='normal'
   rumAlg.configure(background='white')

def rodaAlg():  # falta verificação de preenchimento das entradas
                # falata atualizar as informações depois que roda o algoritmo selecionado
    
    global initState
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]]           
    simJogo['state']='normal'
    simJogo.configure(background='white')
    initPuzzle = []
    aux = []
    if var.get() == 1:
        print(estadoFinal)
        
        print(var.get())
        
        print(initState)
        
        initPuzzle = puzzle.Puzzle(initState)

        root_largura = node_largura.Node(None,initPuzzle,-1,0,0)

        elemento = largura.Largura(root_largura,estadoFinal)
        info["text"] = "custo = " + elemento.custo + "\nprofundidade = " + elemento.profundidade + "\nelementos na fronteira = " + elemento.listaDeNodes

    elif var.get() == 2:
        print(var.get())
    elif var.get() == 3:
        print(var.get())
    elif var.get() == 4:
        print(var.get())
    

def simulaJogo():  # falta tudo
    #falta add
    #cond temp.
    valY = 10

def limpar(): # Ok
    #limpar entrada
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)
    ent7.delete(0,END)
    ent8.delete(0,END)
    ent9.delete(0,END)
    #limpar dados obtidos:
    info["text"] = "AINDA SEM INFORMAÇÕES!"
    #desabilita botões ativados:
    R1['state']='disabled'
    R1.configure(background='#5F9EA0')
    R2['state']='disabled'
    R2.configure(background='#5F9EA0')
    R3['state']='disabled'
    R3.configure(background='#5F9EA0')
    R4['state']='disabled'
    R4.configure(background='#5F9EA0')
    fundo.configure(background='#5F9EA0')
    rumAlg['bg'] = '#5F9EA0'
    rumAlg.configure(state ='disabled')
    simJogo['bg'] = '#5F9EA0'
    simJogo.configure(state ='disabled')
    #limpar saidas:
    sai1["text"] = ""
    sai2["text"] = ""
    sai3["text"] = ""
    sai4["text"] = ""
    sai5["text"] = ""
    sai6["text"] = ""
    sai7["text"] = ""
    sai8["text"] = ""
    sai9["text"] = ""
    
    

#plano de fundo:
#fundo = PhotoImage(file = "matrix3.gif")
#w = Label(janela, image=fundo)
#w.place(x=0, y=0)

lab = Label(janela,text ="INSERIR DADOS INICIAIS DO JOGO")
lab['bg'] =  '#00cccc'
lab.place(x=valX, y=valY)

# PRIMEIRA LINHA
ent1 = Entry (janela, font=large_font, justify = "center")
ent1.place(width = 40, height= 40)
ent1.place(x=valX*4 ,y=valY*4)

ent2 = Entry (janela, font=large_font, justify = "center")
ent2.place(width = 40, height= 40)
ent2.place(x=valX*8,y=valY*4)

ent3 = Entry (janela, font=large_font, justify = "center")
ent3.place(width = 40, height= 40)
ent3.place(x=valX*12 ,y=valY*4)
# SEGUNDA LINHA
ent4 = Entry (janela, font=large_font, justify = "center")
ent4.place(width = 40, height= 40)
ent4.place(x=valX*4 ,y=valY*8)

ent5 = Entry (janela, font=large_font, justify = "center")
ent5.place(width = 40, height= 40)
ent5.place(x=valX*8,y=valY*8)

ent6 = Entry (janela, font=large_font, justify = "center")
ent6.place(width = 40, height= 40)
ent6.place(x=valX*12 ,y=valY*8)
# TERCEIRA LINHA
ent7 = Entry (janela, font=large_font, justify = "center")
ent7.place(width = 40, height= 40)
ent7.place(x=valX*4 ,y=valY*12)

ent8 = Entry (janela, font=large_font, justify = "center")
ent8.place(width = 40, height= 40)
ent8.place(x=valX*8,y=valY*12)

ent9 = Entry (janela, font=large_font, justify = "center")
ent9.place(width = 40, height= 40)
ent9.place(x=valX*12 ,y=valY*12)

# BOTÃO PARA GERAR O  JOGO 
gera =Button(janela, text='GERAR JOGO', command=gerarJogo)
gera.place(x=valX*20, y=valY*5)



# OPÇÕES:
fundo = Label(janela)
fundo.place(x=valX*16+5, y=valY*5+40)
fundo.place(width = 190, height= 85)
fundo['bg'] = '#5F9EA0'

var = IntVar()
R1 = Radiobutton(janela, text="Força Bruta(LARGURA)            ", variable=var, value=1, command=sel)
R1.place(x=valX*17, y=valY*5+40)
R1['bg'] = '#5F9EA0'
R1.configure(state ='disabled')

R2 = Radiobutton(janela, text="Força Bruta(PROFUNDIDADE)", variable=var, value=2, command=sel)
R2.place(x=valX*17, y=valY*5+60)
R2['bg'] = '#5F9EA0'
R2.configure(state ='disabled')

R3 = Radiobutton(janela, text="Busca Gulosa        ", variable=var, value=3, command=sel)
R3.place(x=valX*17, y=valY+120)
R3['bg'] = '#5F9EA0'
R3.configure(state ='disabled')

R4 = Radiobutton(janela, text="           A*            ", variable=var, value=4, command=sel)
R4.place(x=valX*17, y=valY+140)
R4['bg'] = '#5F9EA0'
R4.configure(state ='disabled')

# BOTÃO PARA RODAR ALGORITMO:
rumAlg =Button(janela, text='RODAR ALGORITMO', command=rodaAlg)
rumAlg.place(x=valX*20-20, y=valY+170)
rumAlg['bg'] = '#5F9EA0'
rumAlg.configure(state ='disabled')

# AREA PARA PLOTAR INFORMAÇÕES OBTIDAS (LATERAL DIREITA)
lab2 = Label(janela,text ="INFORMAÇÕES OBTIDAS NA EXECUÇÃO:")
lab2['bg'] =  '#00cccc'
lab2.place(x=valX*44, y=valY)

info = Label(janela, text ="AINDA SEM INFORMAÇÕES!")
info.place(width = 400, height= 300)
info.place(x=valX*36, y=valY*4)

#AREA PARA PLOTAR SIMULAÇÃO DE EXECUÇÃO DO JOGO (CANTO INFERIOR ESQUERDO)
simJogo =Button(janela, text='RODAR SIMULAÇÃO', command=simulaJogo)
simJogo.place(x=valX*4, y=valY+220)
simJogo['bg'] = '#5F9EA0'
simJogo.configure(state ='disabled')

# PRIMEIRA LINHA
sai1 = Label (janela)
sai1.place(width = 39, height= 39)
sai1.place(x=valX*4 ,y=valY*4+220)
sai1['bg'] = '#00cccc'

sai2 = Label (janela, font=large_font, justify = "center")
sai2.place(width = 39, height= 39)
sai2.place(x=valX*8,y=valY*4+220)
sai2['bg'] = '#00cccc'

sai3 = Label (janela, font=large_font, justify = "center")
sai3.place(width = 39, height= 39)
sai3.place(x=valX*12 ,y=valY*4+220)
sai3['bg'] = '#00cccc'

# SEGUNDA LINHA
sai4 = Label (janela, font=large_font, justify = "center")
sai4.place(width = 39, height= 39)
sai4.place(x=valX*4 ,y=valY*8+220)
sai4['bg'] = '#00cccc'

sai5 = Label (janela, font=large_font, justify = "center")
sai5.place(width = 39, height= 39)
sai5.place(x=valX*8,y=valY*8+220)
sai5['bg'] = '#00cccc'

sai6 = Label (janela, font=large_font, justify = "center")
sai6.place(width = 39, height= 39)
sai6.place(x=valX*12 ,y=valY*8+220)
sai6['bg'] = '#00cccc'

# TERCEIRA LINHA
sai7 = Label (janela, font=large_font, justify = "center")
sai7.place(width = 39, height= 39)
sai7.place(x=valX*4 ,y=valY*12+220)
sai7['bg'] = '#00cccc'

sai8 = Label (janela, font=large_font, justify = "center")
sai8.place(width = 39, height= 39)
sai8.place(x=valX*8,y=valY*12+220)
sai8['bg'] = '#00cccc'

sai9 = Label (janela, font=large_font, justify = "center")
sai9.place(width = 39, height= 39)
sai9.place(x=valX*12 ,y=valY*12+220)
sai9['bg'] = '#00cccc'

#BOTÃO PARA LIMPAR INFORMAÇÕES:
limpa = Button(janela, text='LIMPAR', command=limpar)
limpa.place(x=710, y=370)


#alterar tamanho
# LxA+e+t  
janela.geometry("770x400+250+60")
'''bloqueia a possibilidade de redimencionar a tela'''
janela.resizable(width=False, height=False)
janela.mainloop()

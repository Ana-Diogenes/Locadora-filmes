from lib import *
from tkinter import *
from tkinter.scrolledtext import *

locadora = Tk()
locadora.title('Locadora de filmes :)')
locadora.geometry('800x500')
locadora.resizable(False,False)
locadora.configure(background="#fff3ac")
modo = 'inicio'

def modo_busca():
    global modo
    modo = 'busca'
    tela()

def modo_locar():
    global modo
    modo = 'locar'
    tela()

def modo_devolver():
    global modo
    modo = 'devolver'
    tela()

def modo_cadastrar():
    global modo
    modo = 'cadastrar'
    tela()

def modo_remover():
    global modo
    modo = 'remover'
    tela()

def modo_recomendar():
    global modo
    modo = 'recomendar'
    tela()

def modo_inicio():
    global modo
    modo = 'inicio'
    tela()




def tela():
    def pegar_texto():
        return texto.get()
    
    def fazer_busca():
        buscado = pegar_texto()
        resultado = buscar_filme(buscado)
        resposta ['text'] = resultado

    limpar_tela(locadora)
    if modo == 'inicio':
        h1 = Label(locadora, text='Seja bem vindo a locadora!', background='#fff3ac', font=('Arial',32,"bold"))
        h1.place(relx=0.5,y=30, anchor='center')
        h2 = Label(locadora, text='O que deseja fazer?', background='#fff3ac', font=('Arial',20))
        h2.place(relx=0.5,y=75,anchor='center')

        buscar = Button(locadora, text='Buscar filme', command=modo_busca, font=('Arial',12))
        buscar.place(relx=0.1,y=140, width=120, height=50, anchor='center')
        locar = Button(locadora, text='Locar filme', command=modo_locar, font=('Arial',12))
        locar.place(relx=0.3, y=140, width=120, height=50, anchor='center')
        devolver = Button(locadora, text='Devolver filme', command=modo_devolver, font=('Arial',12))
        devolver.place(relx=0.5, y=140, width=120, height=50, anchor='center')
        cadastrar = Button(locadora, text='Cadastrar filme', command=modo_cadastrar, font=('Arial',12))
        cadastrar.place(relx=0.7, y=140, width=120, height=50, anchor='center')
        remover = Button(locadora, text='Remover filme', command=modo_remover, font=('Arial',12))
        remover.place(relx=0.9, y=140, width=120, height=50, anchor='center')

        catalogo = Label(locadora, text='Catalogo:',background='#fff3ac', font=('Arial',16))
        catalogo.place(relx=0.5,y=190,anchor='center')
        filmes = ScrolledText(locadora, width=70, height=12, font=('Arial',12))
        filmes.place(relx=0.5, y=330,anchor='center')
        filmes.insert(INSERT,mostrar_filmes())
        filmes.configure(state='disabled')

        recomendacao = Button(locadora,text='Recomendação personalizada!', command=modo_recomendar,font=('Arial',12))
        recomendacao.place(relx=0.5, y= 470, anchor='center')

    elif modo == 'busca':
        h1 = Label(locadora, text='Qual filme deseja buscar?', background='#fff3ac', font=('Arial',32,"bold"))
        h1.place(relx=0.5,y=30, anchor='center')
        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12))
        info.place(relx=0.5, y=90, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Procurar', font=('Arial',12), width=7, command=fazer_busca)
        enviar_info.place(relx=0.45,y=130, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7)
        voltar.place(relx=0.55, y=130, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#fff3ac', wraplength=400)
        resposta.place(relx=0.5,y=200, anchor=N)


    elif modo == 'locar':
        h1 = Label()

    elif modo == 'devolver':
        h1 = Label()

    elif modo == 'cadastrar':
        h1 = Label()

    elif modo == 'remover':
        h1 = Label()
    
    elif modo == 'recomendar':
        h1 = Label()

tela()
locadora.mainloop()
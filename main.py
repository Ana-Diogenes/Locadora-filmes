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

def tela():
    limpar_tela(locadora)
    if modo == 'inicio':
        h1 = Label(locadora, text='Seja bem vindo a locadora!', background='#fff3ac', font=('Arial',32,"bold"))
        h1.place(relx=0.5,y=30, anchor='center')
        h2 = Label(locadora, text='O que deseja fazer?', background='#fff3ac', font=('Arial',20))
        h2.place(relx=0.5,y=75,anchor='center')

        buscar = Button(locadora, text='Buscar filme', command=modo_busca, font=('Arial',12))
        buscar.place(relx=0.1,y=140, width=120, height=50, anchor='center')
        locar = Button(locadora, text='Locar filme', command=locar_filme, font=('Arial',12))
        locar.place(relx=0.3, y=140, width=120, height=50, anchor='center')
        devolver = Button(locadora, text='Devolver filme', command=devolver_filme, font=('Arial',12))
        devolver.place(relx=0.5, y=140, width=120, height=50, anchor='center')
        cadastrar = Button(locadora, text='Cadastrar filme', command=inserir_filme, font=('Arial',12))
        cadastrar.place(relx=0.7, y=140, width=120, height=50, anchor='center')
        remover = Button(locadora, text='Remover filme', command=excluir_filme, font=('Arial',12))
        remover.place(relx=0.9, y=140, width=120, height=50, anchor='center')

        catalogo = Label(locadora, text='Catalogo:',background='#fff3ac', font=('Arial',16))
        catalogo.place(relx=0.5,y=190,anchor='center')
        filmes = ScrolledText(locadora, width=70, height=12, font=('Arial',12))
        filmes.place(relx=0.5, y=330,anchor='center')
        filmes.insert(INSERT,mostrar_filmes())
        filmes.configure(state='disabled')

        recomendacao = Button(locadora,text='Recomendação personalizada!', command=indicação_personalizada,font=('Arial',12))
        recomendacao.place(relx=0.5, y= 470, anchor='center')
    else:
        h1=Label(text='a')
        h1.place(y=0,x=0)

tela()
locadora.mainloop()
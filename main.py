from lib import *
from tkinter import *

locadora = Tk()
locadora.title('Locadora de filmes :)')
locadora.geometry('800x500')
locadora.resizable(False,False)
locadora.configure(background="#fff3ac")
h1 = Label(locadora, text='Seja bem vindo a locadora!', background='#fff3ac', font=('Arial',32,"bold"))
h1.place(relx=0.5,y=30, anchor='center')
h2 = Label(locadora, text='O que deseja fazer?', background='#fff3ac', font=('Arial',20))
h2.place(relx=0.5,y=75,anchor='center')

buscar = Button(locadora, text='Buscar filme', command=buscar_filme, font=('Arial',12))
buscar.place(relx=0.1,y=140, width=120, height=50, anchor='center')
locar = Button(locadora, text='Locar filme', command=locar_filme, font=('Arial',12))
locar.place(relx=0.3, y=140, width=120, height=50, anchor='center')
devolver = Button(locadora, text='Devolver filme', command=devolver_filme, font=('Arial',12))
devolver.place(relx=0.5, y=140, width=120, height=50, anchor='center')
cadastrar = Button(locadora, text='Cadastrar filme', command=inserir_filme, font=('Arial',12))
cadastrar.place(relx=0.7, y=140, width=120, height=50, anchor='center')
remover = Button(locadora, text='Remover filme', command=excluir_filme, font=('Arial',12))
remover.place(relx=0.9, y=140, width=120, height=50, anchor='center')

locadora.mainloop()
from lib import *
from tkinter import *

locadora = Tk()
locadora.title('Locadora de filmes :)')
locadora.geometry('800x500')
locadora.resizable(False,False)
locadora.configure(background='#f8f6a2')
h1 = Label(locadora, text='Seja bem vindo a locadora!', background='#f8f6a2', font=('Arial',32,"bold"))
h1.place(relx=0.5,y=30, anchor='center')
h2 = Label(locadora, text='O que deseja fazer?', background='#f8f6a2', font=('Arial',20))
h2.place(relx=0.5,y=75,anchor='center')

locadora.mainloop()
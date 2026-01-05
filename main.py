from lib import *
from tkinter import *
from tkinter.scrolledtext import *

locadora = Tk()
locadora.title('Locadora de filmes :)')
locadora.geometry('800x500')
locadora.resizable(False,False)
locadora.configure(background="#2d3250")
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
    def pegar_texto(texto):
        return texto.get()
    
    def fazer_busca():
        buscado = pegar_texto(texto)
        resultado = buscar_filme(buscado)
        resposta ['text'] = resultado

    def fazer_locacao():
        locado = pegar_texto(texto)
        resultado = locar_filme(locado)
        resposta ['text'] = resultado

    def fazer_devolucao():
        devolvido = pegar_texto(texto)
        resultado = devolver_filme(devolvido)
        resposta ['text'] = resultado

    limpar_tela(locadora)
    if modo == 'inicio':
        h1 = Label(locadora, text='Seja bem vindo a locadora!', background='#2d3250', font=('Arial',32,"bold"),foreground='#ffffff')
        h1.place(relx=0.5,y=30, anchor='center')
        h2 = Label(locadora, text='O que deseja fazer?', background='#2d3250', font=('Arial',20), foreground="#ffffff")
        h2.place(relx=0.5,y=75,anchor='center')

        buscar = Button(locadora, text='Buscar filme', command=modo_busca, font=('Arial',12), foreground='#2d3250', background='#ffcbcf')
        buscar.place(relx=0.1,y=140, width=120, height=50, anchor='center')
        locar = Button(locadora, text='Locar filme', command=modo_locar, font=('Arial',12), foreground='#2d3250', background='#ffcbcf')
        locar.place(relx=0.3, y=140, width=120, height=50, anchor='center')
        devolver = Button(locadora, text='Devolver filme', command=modo_devolver, font=('Arial',12), foreground='#2d3250', background='#ffcbcf')
        devolver.place(relx=0.5, y=140, width=120, height=50, anchor='center')
        cadastrar = Button(locadora, text='Cadastrar filme', command=modo_cadastrar, font=('Arial',12), foreground='#2d3250', background='#ffcbcf')
        cadastrar.place(relx=0.7, y=140, width=120, height=50, anchor='center')
        remover = Button(locadora, text='Remover filme', command=modo_remover, font=('Arial',12), foreground='#2d3250', background='#ffcbcf')
        remover.place(relx=0.9, y=140, width=120, height=50, anchor='center')

        catalogo = Label(locadora, text='Catalogo:',background='#2d3250', font=('Arial',16), foreground='#ffffff')
        catalogo.place(relx=0.5,y=190,anchor='center')
        filmes = ScrolledText(locadora, width=70, height=12, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        filmes.place(relx=0.5, y=330,anchor='center')
        filmes.insert(INSERT,mostrar_filmes())
        filmes.configure(state='disabled')

        recomendacao = Button(locadora,text='Recomendação personalizada!', command=modo_recomendar,font=('Arial',12), foreground='#2d3250',background='#ffcbcf')
        recomendacao.place(relx=0.5, y= 470, anchor='center')

    elif modo == 'busca':
        h1 = Label(locadora, text='Qual filme deseja buscar?', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=30, anchor='center')
        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info.place(relx=0.5, y=90, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Procurar', font=('Arial',12), width=7, command=fazer_busca, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.45,y=130, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.55, y=130, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=200, anchor=N)


    elif modo == 'locar':
        h1 = Label(locadora, text='Qual filme deseja locar?', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=30, anchor='center')
        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info.place(relx=0.5, y=90, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Locar', font=('Arial',12), width=7, command=fazer_locacao, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.45,y=130, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.55, y=130, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=200, anchor=N)

    elif modo == 'devolver':
        h1 = Label(locadora, text='Qual filme deseja devolver', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=30, anchor='center')
        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info.place(relx=0.5, y=90, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Devolver', font=('Arial',12), width=7, command=fazer_devolucao, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.45,y=130, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.55, y=130, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=200, anchor=N)

    elif modo == 'cadastrar':
        h1 = Label(locadora, text='Adicione as informações do \n novo filme', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=50, anchor='center')

        titulo_l = Label (locadora, text='Titulo:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        titulo_l.place(x=100, y=130)
        titulo = StringVar()
        info_t = Entry(locadora,textvariable=titulo, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info_t.place(x=100, y=160,  width=600, height=30)

        titulo_c = Label (locadora, text='Classificacao indicativa:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        titulo_c.place(x=100, y=200)
        classificacoes = ["L", "10", "12", "14","16","18"]
        classificacao = StringVar()
        classificacao.set("Classificacoes")
        menu_c = OptionMenu(locadora, classificacao, *classificacoes)
        menu_c.place(x=100, y=230)

        titulo_g = Label (locadora, text='Genero:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        titulo_g.place(x=100, y=270)
        generos = ['drama','romance','ficcao cientifica','acao','fantasia','aventura','animacao','terror','comedia']
        genero = StringVar()
        genero.set("Generos")
        menu_g = OptionMenu(locadora, genero, *generos, )
        menu_g.place(x=100, y=300)

        titulo_s = Label (locadora, text='Sinopse:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        titulo_s.place(x=100, y=340)
        sinopse = StringVar()
        info_s = Entry(locadora,textvariable=sinopse, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info_s.place(x=100, y=370,  width=600, height=30)

        enviar_info = Button(locadora, text='Cadastrar', font=('Arial',12), width=8, command='', foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(x=300,y=420)
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(x=400, y=420)

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=200, anchor=N)
    elif modo == 'remover':
        h1 = Label()
    
    elif modo == 'recomendar':
        h1 = Label()

tela()
locadora.mainloop()
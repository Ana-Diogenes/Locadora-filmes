from lib import *
from tkinter import *
from tkinter.scrolledtext import *

#Configurações iniciais da interface
locadora = Tk()
locadora.title('Locadora de filmes :)')
locadora.geometry('800x500')
locadora.resizable(False,False)
locadora.configure(background="#2d3250")
modo = 'inicio'

#Funções para mudar o modo da tela:
def modo_busca():
    global modo
    modo = 'busca' #Mudo o modo
    tela() #Chamo a função tela pra ela renderizar a tela de novo
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

def tela(): #Função principal do projeto
    
    #Funções para executar as funções nos botões e mostrar a resposta
    def fazer_busca():
        buscado = texto.get() #Pego o texto que o usuario digitou
        resultado = buscar_filme(buscado) #Executo a função desejada usando o texto do usuario como parametro
        resposta ['text'] = resultado #Pego o resultado da função e faço ele aparecer no texto do label resposta
    def fazer_locacao():
        locado = texto.get()
        resultado = locar_filme(locado)
        resposta ['text'] = resultado
    def fazer_devolucao():
        devolvido = texto.get()
        resultado = devolver_filme(devolvido)
        resposta ['text'] = resultado
    def fazer_cadastro():
        titulo_cadastro = titulo.get()
        classificacao_cadastro = classificacao.get()
        genero_cadastro = genero.get()
        sinopse_cadastro = sinopse.get()
        resultado = inserir_filme(titulo_cadastro, classificacao_cadastro,genero_cadastro,sinopse_cadastro)
        resposta ['text']=resultado
    def fazer_remocao():
        removido = texto.get()
        resultado = excluir_filme(removido)
        resposta['text']= resultado
    def fazer_recomendação():
        classificacao_rec = classificacao.get()
        genero_rec = genero.get()
        resultado = indicação_personalizada(classificacao_rec, genero_rec)
        resposta['text']= resultado

    limpar_tela(locadora) #Limpo a tela antes de começar para apagar as informações da tela anterior

    if modo == 'inicio': #Tela inicial

        #Titulo e subtitulo da pagina
        h1 = Label(locadora, text='Seja bem vindo a locadora!', background='#2d3250', font=('Arial',32,"bold"),foreground='#ffffff') #Parametros do item
        h1.place(relx=0.5,y=30, anchor='center') #Posicionando o item
        h2 = Label(locadora, text='O que deseja fazer?', background='#2d3250', font=('Arial',20), foreground="#ffffff")
        h2.place(relx=0.5,y=75,anchor='center')

        #Botões para trocar de tela e fazer alguma das funções listadas
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
        recomendacao = Button(locadora,text='Recomendação personalizada!', command=modo_recomendar,font=('Arial',12), foreground='#2d3250',background='#ffcbcf')
        recomendacao.place(relx=0.5, y= 470, anchor='center')

        #Mostrando o catalogo de filmes
        catalogo = Label(locadora, text='Catalogo:',background='#2d3250', font=('Arial',16), foreground='#ffffff')
        catalogo.place(relx=0.5,y=190,anchor='center')
        filmes = ScrolledText(locadora, width=70, height=12, font=('Arial',12), background = "#606378", foreground = '#ffffff') #Tetxo com barra de rolagem (por padrão, deve ser digitado pelo usuario)
        filmes.place(relx=0.5, y=330,anchor='center')
        filmes.insert(INSERT,mostrar_filmes()) #Coloco a função mostrar_filmes para executar dentro do campo de texto
        filmes.configure(state='disabled') #Bloqueio o usuario de mudar o texto 

    elif modo == 'busca': #Tela para buscar filmes
        h1 = Label(locadora, text='Qual filme deseja buscar?', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=110, anchor='center')

        texto = StringVar() #Variavel para armazenar texto dos inputs
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff') #Input
        info.place(relx=0.5, y=170, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Procurar', font=('Arial',12), width=7, command=fazer_busca, foreground='#2d3250', background='#ffcbcf') #Chamo a função que faz a busca quando clico nesse botão
        enviar_info.place(relx=0.45,y=210, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf') #Botão para voltar a tela inicial
        voltar.place(relx=0.55, y=210, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff') #Espaço onde o resultado da função vai aparecer quando ela for chamada
        resposta.place(relx=0.5,y=270, anchor=N)


    elif modo == 'locar': #Tela para locar filmes
        h1 = Label(locadora, text='Qual filme deseja locar?', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=110, anchor='center')

        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info.place(relx=0.5, y=170, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Locar', font=('Arial',12), width=7, command=fazer_locacao, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.45,y=210, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.55, y=210, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=270, anchor=N)

    elif modo == 'devolver': #Tela para devolver filmes
        h1 = Label(locadora, text='Qual filme deseja devolver', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=110, anchor='center')

        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info.place(relx=0.5, y=170, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Devolver', font=('Arial',12), width=7, command=fazer_devolucao, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.45,y=210, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.55, y=210, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=270, anchor=N)

    elif modo == 'cadastrar': #Tela para cadastrar filmes
        h1 = Label(locadora, text='Adicione as informações do \n novo filme', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=50, anchor='center')

        label_t = Label (locadora, text='Titulo:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        label_t.place(x=100, y=110)
        titulo = StringVar()
        info_t = Entry(locadora,textvariable=titulo, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info_t.place(x=100, y=140,  width=600, height=30)

        label_c = Label (locadora, text='Classificacao indicativa:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        label_c.place(x=100, y=180)
        classificacoes = ["L", "10", "12", "14","16","18"] #Lista com as opçoes disponiveis para o menu
        classificacao = StringVar() #Variavel para guardar a opção escolhida
        classificacao.set("Classificacoes") #Aparece enquanto nenhuma opção for escolhida
        menu_c = OptionMenu(locadora, classificacao, *classificacoes) #Crio o menu
        menu_c.place(x=100, y=210)

        label_g = Label (locadora, text='Genero:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        label_g.place(x=100, y=250)
        generos = ['drama','romance','ficcao cientifica','acao','fantasia','aventura','animacao','terror','comedia']
        genero = StringVar()
        genero.set("Generos")
        menu_g = OptionMenu(locadora, genero, *generos, )
        menu_g.place(x=100, y=280)

        label_s = Label (locadora, text='Sinopse:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        label_s.place(x=100, y=320)
        sinopse = StringVar()
        info_s = Entry(locadora,textvariable=sinopse, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info_s.place(x=100, y=350,  width=600, height=30)

        enviar_info = Button(locadora, text='Cadastrar', font=('Arial',12), width=8, command=fazer_cadastro, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(x=300,y=400)
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(x=400, y=400)

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=440, anchor=N)

    elif modo == 'remover': #Tela para remover filmes
        h1 = Label(locadora, text='Qual filme deseja remover?', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=110, anchor='center')
        texto = StringVar()
        info = Entry(locadora,textvariable=texto, font=('Arial',12), background = "#606378", foreground = '#ffffff')
        info.place(relx=0.5, y=170, anchor='center', width=300, height=30)
        enviar_info = Button(locadora, text='Remover', font=('Arial',12), width=7, command=fazer_remocao, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.45,y=210, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.55, y=210, anchor='center' )

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=270, anchor=N)    

    elif modo == 'recomendar': #Tela para receber uma recomendação
        h1 = Label(locadora, text='Que tipo de filme você gosta?', background='#2d3250', font=('Arial',32,"bold"), foreground='#ffffff')
        h1.place(relx=0.5,y=50, anchor='center')

        label_c = Label (locadora, text='Classificacao indicativa:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        label_c.place(relx=0.4, y=110, anchor='center')
        classificacoes = ["L", "10", "12", "14","16","18"]
        classificacao = StringVar()
        classificacao.set("Classificacoes")
        menu_c = OptionMenu(locadora, classificacao, *classificacoes)
        menu_c.place(relx=0.4, y=140, anchor='center')

        label_g = Label (locadora, text='Genero:', background='#2d3250', font=('Arial',12), foreground='#ffffff')
        label_g.place(relx=0.6, y=110, anchor='center')
        generos = ['drama','romance','ficcao cientifica','acao','fantasia','aventura','animacao','terror','comedia']
        genero = StringVar()
        genero.set("Generos")
        menu_g = OptionMenu(locadora, genero, *generos, )
        menu_g.place(relx=0.6, y=140, anchor='center')

        enviar_info = Button(locadora, text='Encontrar filme', font=('Arial',12), command=fazer_recomendação, foreground='#2d3250', background='#ffcbcf')
        enviar_info.place(relx=0.4,y=190, anchor='center')
        voltar = Button(locadora, text='Inicio', font=('Arial',12), command=modo_inicio, width=7, foreground='#2d3250', background='#ffcbcf')
        voltar.place(relx=0.6, y=190, anchor='center')

        resposta = Label(locadora, text='',font=('Arial',12), background='#2d3250', wraplength=400, foreground='#ffffff')
        resposta.place(relx=0.5,y=220, anchor=N)
        

tela() #Chamo a função principal

locadora.mainloop() #Função para tela ficar aparecendo
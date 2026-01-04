import csv
from tkinter import *


def mostrar_filmes():
    catalogo = ''
    with open('filmes.csv',"r") as filmes:
        lista_filmes = csv.reader(filmes, delimiter=",")
        for i,linha in enumerate(lista_filmes):
            if i!=0 and linha[4]=="disponivel":
                catalogo += str(i) + ': ' + linha[0] + '\n'
            elif i!=0 and linha[4]!= "disponivel":
                catalogo += str(i) + ': ' + linha[0] +' (alugado)'+ '\n'
    return catalogo

def inserir_filme():
    titulo = input('Informe o titulo do filme: ')
    classificacao = input('Informe a classificação indicativa do filme: ')
    genero = input('Informe o genero do filme: ')
    sinopse = input ('Informe a sinopse do filme: ')
    mensagem = '\n'+ titulo +','+ classificacao +',' + genero.lower() +',' + sinopse + ',disponivel'
    with open('filmes.csv',"a") as filmes:
        filmes.write(mensagem)

def excluir_filme():
    excluido = input('Informe o nome do filme que deseja excluir: ')
    lista_nova = []
    with open('filmes.csv',"r") as filmes:
        lista_filmes = csv.reader(filmes, delimiter=",")
        for linha in lista_filmes:
            if (linha [0]).lower() != (excluido).lower():
                lista_nova.append(linha)
    with open ('filmes.csv','w') as filmes:
        for i,linha in enumerate(lista_nova):
            titulo = linha[0]
            classificacao = linha[1]
            genero = linha[2]
            sinopse = linha[3]
            status = linha [4]
            mensagem = titulo +','+ classificacao +',' + genero.lower() +',' + sinopse +','+ status
            if i==0:
                filmes.write(mensagem)
            else:
                filmes.write('\n'+mensagem)

def buscar_filme():
    buscado = input('Informe o filme que deseja buscar: ')
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes, delimiter=',')
        encontrado = False
        for linha in lista_filmes:
            if (linha[0]).lower() == buscado.lower():
                encontrado = True
                print('Titulo:',linha[0])
                print('Classificacao indicativa:',linha[1])
                print('Genero:',linha[2])
                print('Sinopse:',linha[3])
                if linha[4]=='disponivel':
                    print('O filme está disponivel para aluguel!')
                else:
                    print ('O filme não está disponivel para aluguel')
        if encontrado == False:
            print('Não encontramos o filme que deseja')

def locar_filme():
    locado = input('Informe o filme que deseja locar: ')
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        lista_nova =[]
        for linha in lista_filmes:
            if (linha[0]).lower() == locado.lower() and linha[4]== 'disponivel':
                filme = [linha[0],linha[1],linha[2],linha[3],'alugado']
                lista_nova.append(filme)
                print('O filme foi locado com sucesso! Não se esqueça de devolver!')
            elif (linha[0]).lower() == locado.lower() and linha[4]!= 'disponivel':
                print ('O filme que você deseja não está disponivel!')
                return
            else:
                lista_nova.append(linha)
        with open ('filmes.csv','w') as filmes:
            for i,linha in enumerate(lista_nova):
                titulo = linha[0]
                classificacao = linha[1]
                genero = linha[2]
                sinopse = linha[3]
                status = linha [4]
                mensagem = titulo +','+ classificacao +',' + genero.lower() +',' + sinopse +','+ status
                if i==0:
                    filmes.write(mensagem)
                else:
                    filmes.write('\n'+mensagem)

def devolver_filme():
    devolvido = input('Informe o filme que deseja devolver: ')
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        lista_nova =[]
        for linha in lista_filmes:
            if (linha[0]).lower() == devolvido.lower() and linha[4]== 'alugado':
                filme = [linha[0],linha[1],linha[2],linha[3],'disponivel']
                lista_nova.append(filme)
                print('O filme foi devolvido com sucesso!')
            elif (linha[0]).lower() == devolvido.lower() and linha[4]!= 'alugado':
                print ('O filme em questão já foi devolvido!')
                return
            else:
                lista_nova.append(linha)
        with open ('filmes.csv','w') as filmes:
            for i,linha in enumerate(lista_nova):
                titulo = linha[0]
                classificacao = linha[1]
                genero = linha[2]
                sinopse = linha[3]
                status = linha [4]
                mensagem = titulo +','+ classificacao +',' + genero.lower() +',' + sinopse +','+ status
                if i==0:
                    filmes.write(mensagem)
                else:
                    filmes.write('\n'+mensagem)

def indicação_personalizada():
    classificacao = input('Informe a classificacao que prefere: ')
    genero = input('Informe o genero de filme que gosta: ')
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        for linha in lista_filmes:
            if linha[1].lower() == classificacao.lower() and linha[2].lower()== genero.lower() and linha[4]=='disponivel':
                print ('voce pode gostar do filme',linha[0],'!')
                print('sinopse:',linha[3])

def limpar_tela(locadora):
    for widget in locadora.winfo_children():
        widget.place_forget()

# def modo_busca():
#     global modo
#     modo = 'busca'
#     main()

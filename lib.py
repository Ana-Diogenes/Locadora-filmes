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

def buscar_filme(buscado):
    resposta = ''
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes, delimiter=',')
        encontrado = False
        for linha in lista_filmes:
            if (linha[0]).lower() == buscado.lower():
                encontrado = True
                resposta += ('Titulo: '+ str(linha[0])+'\n')
                resposta += ('Classificacao indicativa: '+(linha[1])+'\n')
                resposta += ('Genero: '+ str(linha[2])+'\n')
                resposta += ('Sinopse: '+ str(linha[3])+'\n')
                if linha[4]=='disponivel':
                    resposta += ('O filme está disponivel para aluguel!')
                else:
                    resposta += ('O filme não está disponivel para aluguel')
        if encontrado == False:
            resposta = ('Não encontramos o filme que deseja')
    return resposta

def locar_filme(locado):
    resposta = ''
    achou = False
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        lista_nova =[]
        for linha in lista_filmes:
            if (linha[0]).lower() == locado.lower() and linha[4]== 'disponivel':
                filme = [linha[0],linha[1],linha[2],linha[3],'alugado']
                lista_nova.append(filme)
                resposta = ('O filme foi locado com sucesso! Não se esqueça de devolver!')
                achou = True
            elif (linha[0]).lower() == locado.lower() and linha[4]!= 'disponivel':
                achou = True
                return ('O filme que você deseja não está disponivel!')
                
            else:
                lista_nova.append(linha)
        if achou == False:
            return 'Não achamos o filme que deseja locar'
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
    return resposta

def devolver_filme(devolvido):
    achou = False
    resposta = ''
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        lista_nova =[]
        for linha in lista_filmes:
            if (linha[0]).lower() == devolvido.lower() and linha[4]== 'alugado':
                filme = [linha[0],linha[1],linha[2],linha[3],'disponivel']
                lista_nova.append(filme)
                resposta = ('O filme foi devolvido com sucesso!')
                achou = True
            elif (linha[0]).lower() == devolvido.lower() and linha[4]!= 'alugado':
                achou = True
                return ('O filme em questão não foi alugado')
                
            else:
                lista_nova.append(linha)

        if achou == False:
            return ('Não encontramos o filme que deseja devolver')
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
    return resposta

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



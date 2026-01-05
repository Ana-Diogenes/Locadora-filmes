import csv
from tkinter import *


def mostrar_filmes(): #Função que mostra todos os filmes
    catalogo = '' #Variavel para armazenar o catalogo
    with open('filmes.csv',"r") as filmes: #Abro o arquivo csv no modo leitura
        lista_filmes = csv.reader(filmes, delimiter=",") #Cria um objeto csv em que cada linha é uma lista
        for i,linha in enumerate(lista_filmes):
            if i!=0 and linha[4]=="disponivel": #Confere que o item não é o primeiro e se está disponivel
                catalogo += str(i) + ': ' + linha[0] + '\n'
            elif i!=0 and linha[4]!= "disponivel": #Confere que o item não é o primeiro e se está alugado
                catalogo += str(i) + ': ' + linha[0] +' (alugado)'+ '\n'
    return catalogo

def inserir_filme(titulo, classificacao, genero, sinopse): #Função que adiciona filmes novos
    if titulo =='' or classificacao =='Classificacoes' or genero =='Generos' or sinopse =='': #Verifica se algum dos campos não foi preenchido
        return 'Preencha os campos em branco'
    mensagem = '\n'+ titulo +','+ classificacao +',' + genero.lower() +',' + sinopse + ',disponivel'
    with open('filmes.csv',"a") as filmes: #Abro o arquivo csv no modo append (adicionar informações)
        filmes.write(mensagem) #Adiciono o novo filme
    return 'Filme inserido com sucesso'

def excluir_filme(excluido): #Função que apaga filmes
    lista_nova = []
    achou = False
    with open('filmes.csv',"r") as filmes:
        lista_filmes = csv.reader(filmes, delimiter=",")
        for linha in lista_filmes:
            if (linha [0]).lower() != (excluido).lower(): #Se o filme que está sendo percorrido tiver um titulo diferente do excluido, ele é adicionado a lista nova
                lista_nova.append(linha)
            elif (linha [0]).lower() == (excluido).lower(): #Se o titulo for igual ao excluido, ele não é adicionado
                achou = True
    if achou == False: #Se o filme não for encontrado, não há necessidade de reescrevor o arquivo, retorna uma mensagem de erro
        return 'O filme que deseja excluir não foi encontrado'
    with open ('filmes.csv','w') as filmes: #Reescreve o arquivo linha por linha usando os filmes da lista_nova (que não tem o filme excluido)
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
    return 'Filme deletado com sucesso!'

def buscar_filme(buscado): #Função que procura filmes
    resposta = ''
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes, delimiter=',')
        encontrado = False
        for linha in lista_filmes:
            if (linha[0]).lower() == buscado.lower(): #Procura o filme no arquivo
                encontrado = True
                resposta += ('Titulo: '+ str(linha[0])+'\n')
                resposta += ('Classificacao indicativa: '+(linha[1])+'\n')
                resposta += ('Genero: '+ str(linha[2])+'\n')
                resposta += ('Sinopse: '+ str(linha[3])+'\n')
                if linha[4]=='disponivel': #Confere se o filme está disponivel
                    resposta += ('O filme está disponivel para aluguel!')
                else:
                    resposta += ('O filme não está disponivel para aluguel')
        if encontrado == False: 
            resposta = ('Não encontramos o filme que deseja') #Mensagem caso o filme não seja encontrado
    return resposta

def locar_filme(locado): #Função que loca os filme
    resposta = ''
    achou = False
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        lista_nova =[]
        for linha in lista_filmes:
            if (linha[0]).lower() == locado.lower() and linha[4]== 'disponivel': #Confere se achou o filme e se está disponivel
                filme = [linha[0],linha[1],linha[2],linha[3],'alugado'] #O filme agora é adicionado na lista com o status 'alugado'
                lista_nova.append(filme)
                resposta = ('O filme foi locado com sucesso! Não se esqueça de devolver!')
                achou = True
            elif (linha[0]).lower() == locado.lower() and linha[4]!= 'disponivel':
                achou = True
                return ('O filme que você deseja não está disponivel!')  #Mensagem caso o filme locado não esteja disponivel
            else:
                lista_nova.append(linha)
        if achou == False:
            return 'Não achamos o filme que deseja locar' #Mensagem caso o filme não seja encontrado
        with open ('filmes.csv','w') as filmes:
            for i,linha in enumerate(lista_nova): #Reescreve o arquivo com o filme locado
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

def devolver_filme(devolvido): #Função para devolver filmes
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

def indicação_personalizada(classificacao, genero): #Função que faz recomendação
    quantidade_filmes = 0 #Variavel para controlar a quantidade de filmes recomendados
    mensagem = 'Voce pode gostar do(s) filme(s):\n'
    with open ('filmes.csv','r') as filmes:
        lista_filmes = csv.reader(filmes,delimiter=',')
        for linha in lista_filmes:
            if linha[1].lower() == classificacao.lower() and linha[2].lower()== genero.lower() and linha[4]=='disponivel' and quantidade_filmes<2: #Confere se o filme é compativel com as caracteristicas desejadas, se está disponivel e se a quantidade limite não foi atingida
                mensagem += ('\ntitulo: '+str(linha[0])+'\nsinopse: '+ str(linha[3])+'\n') #adiciona o filme a mensagem
                quantidade_filmes+=1
    if mensagem == 'Voce pode gostar do(s) filme(s):\n':
        return 'Não encontramos o filme com as caracteristicas que deseja' #Resposta caso nenhum filme seja adicionado a mensagem
    return mensagem

def limpar_tela(locadora): #Função para limpar tela
    for widget in locadora.winfo_children(): #Percorre todos os widgets na tela
        widget.place_forget() #Remove o posicionamento desses itens
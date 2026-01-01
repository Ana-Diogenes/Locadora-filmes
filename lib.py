import csv

def mostrar_filmes():
    with open('filmes.csv',"r") as filmes:
        lista_filmes = csv.reader(filmes, delimiter=",")
        for i,linha in enumerate(lista_filmes):
            if i!=0 and linha[4]=="disponivel":
                print(i,':',linha[0])
            elif i!=0 and linha[4]!= "disponivel":
                print(i,':',linha[0],'(alugado)')



def inserir_filme():
    titulo = input('Informe o titulo do filme: ')
    classificacao = input('Informe a classificação indicativa do filme: ')
    genero = input('Informe o genero do filme: ')
    sinopse = input ('Informe a sinopse do filme: ')
    mensagem = '\n'+ titulo +','+ classificacao +',' + genero.lower() +',' + sinopse + ',disponivel'
    with open('filmes.csv',"a") as filmes:
        filmes.write(mensagem)


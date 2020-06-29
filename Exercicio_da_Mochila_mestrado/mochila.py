from heapq import heappop, heappush
import numpy as np
import sys 
import math



def mochila(capacidadeMochila,qtdeProdutos,custo,peso):
    matriz = [[] for x in range(capacidadeMochila+1)]
    for i in range (capacidadeMochila+1): 
        for j in range(qtdeProdutos+1): matriz[i].append([0,0])

    #Processamento i = linha j = coluna
    
    for i in range((qtdeProdutos - 1),-1,-1):
        for j in range(capacidadeMochila+1):
            if(peso[i] > j):
                matriz[j][i][0] = matriz[j][i+1][0]
                matriz[j][i][1] = 0
            else:
                gDeY =  matriz[(j - peso[i]) ][i+1][0] + custo[i]
                if (gDeY >= matriz[j][i+1][0]):
                    matriz[j][i][0] = gDeY
                    matriz[j][i][1] = 1
                else:
                    matriz[j][i][0] = matriz[j][i+1][0]
                    matriz[j][i][1] = 0
    
    print(matriz)
    print("")
    print("Valor: ",matriz[capacidadeMochila][0][0])

    j,S,res = capacidadeMochila,[],capacidadeMochila
    
    for i in range(qtdeProdutos):
        if(matriz[j][i][1] == 1 and res >= peso[i]  ):
            S.append("x"+ str(i+1))
            res = res - peso[i]
            while(matriz[j][i][1] == 1):
                j -= 1

            

    print("Itens escolhidos: ",S)

def lerArquivo():
    
    filename = 'instancias/' + sys.argv[1]
    f = open(filename, 'r')
    linha = f.readline()
    elementos = linha.rsplit()
    qtdeProdutos = int(elementos[0])
    capacidadeMochila = int(elementos[1])
    
     
    #matriz = [[] for x in range(qtdeVertices)]
    custo, peso = [],[]
    
    for i in range(qtdeProdutos):
        linha = f.readline()
        elementos = linha.rsplit()
        peso.append(int(elementos[0]))
        custo.append(int(elementos[1]))
    

    return capacidadeMochila,qtdeProdutos,custo,peso



if __name__ == '__main__':
    
    capacidadeMochila,qtdeProdutos,custo,peso = lerArquivo()
    mochila( capacidadeMochila,qtdeProdutos,custo,peso)
 
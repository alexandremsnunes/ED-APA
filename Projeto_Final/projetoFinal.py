import numpy as np
import sys 
import math

def inicializaMatrizQuadrada(tamanho, matriz):
    for i in range(tamanho):
        matriz.append([])
        for j in range(tamanho):
            matriz[i].append(math.inf)

def printMatriz(matriz,tamanho):
    for i in range(tamanho):
        print(matriz[i])

def custoTotal(matriz,solucao):
    custo = 0
    for i in range(len(solucao)-1): custo += matriz[solucao[i]][solucao[i+1]]
    return custo


###################################################################

def insercaoMaisProximo(matriz,tamanho):
    cidadesVisitadas,cidadeAtual,menorCusto = [],0,math.inf
     
    cidadesVisitadas.append(0)

    while(len(cidadesVisitadas) < tamanho):
        for i in range(tamanho):
            if(matriz[cidadeAtual][i] < menorCusto and ((i in cidadesVisitadas) == False) ):
                menorCusto = matriz[cidadeAtual][i]
                proximaCidade = i
        cidadeAtual = proximaCidade
        cidadesVisitadas.append(cidadeAtual)
        menorCusto = math.inf
    
    cidadesVisitadas.append(0)
        
    print("Cidades Visitadas:",cidadesVisitadas)
    print("Custo Total:",custoTotal(matriz,cidadesVisitadas))

def insercaoMaisAfastada(matriz,tamanho):
    cidadesVisitadas,cidadeAtual,maiorCusto = [],0,0
    cidadesVisitadas.append(0)

    while(len(cidadesVisitadas) < tamanho):
        for i in range(tamanho):
            if(matriz[cidadeAtual][i] > maiorCusto and ((i in cidadesVisitadas) == False) ):
                maiorCusto = matriz[cidadeAtual][i]
                proximaCidade = i

        cidadeAtual = proximaCidade
        cidadesVisitadas.append(cidadeAtual)
        maiorCusto = 0
    
    cidadesVisitadas.append(0)
    
    print("Cidades Visitadas:",cidadesVisitadas)
    print("Custo Total:",custoTotal(matriz,cidadesVisitadas))

def insercaoMaisBarata(matriz,tamanho):
    cidadesVisitadas,cidadesNaoVisitadas, menorValor = [],[],math.inf
    
    for i in range(tamanho): cidadesNaoVisitadas.append(i)

    cidadesVisitadas.append(0)
    cidadesNaoVisitadas.remove(0)

    for i in range(tamanho):
        if(matriz[cidadesVisitadas[0]][i] < menorValor):
            cidadeEscolhida = i
            menorValor = matriz[cidadesVisitadas[0]][i]
    
    cidadesVisitadas.append(cidadeEscolhida)
    cidadesNaoVisitadas.remove(cidadeEscolhida)
    menorValor = math.inf
    
    for i in range(tamanho):
        if((matriz[i][cidadesVisitadas[0]]+matriz[cidadesVisitadas[1]][i]) < menorValor and ((i in cidadesVisitadas) == False) ):
            cidadeEscolhida = i
            menorValor = matriz[i][cidadesVisitadas[0]]+matriz[cidadesVisitadas[1]][i]
    
    cidadesVisitadas.append(cidadeEscolhida)
    cidadesVisitadas.append(cidadesVisitadas[0])
    cidadesNaoVisitadas.remove(cidadeEscolhida)
    menorValor = math.inf
 
    while(len(cidadesNaoVisitadas) > 0):
        for a in range(len(cidadesVisitadas)-1):
            for k in range(len(cidadesNaoVisitadas)):
                if((matriz[cidadesVisitadas[a]][cidadesNaoVisitadas[k]] + matriz[cidadesNaoVisitadas[k]][cidadesVisitadas[a+1]] - matriz[cidadesVisitadas[a]][cidadesVisitadas[a+1]]) < menorValor):
                    cidadeEscolhida = cidadesNaoVisitadas[k]
                    menorValor = (matriz[cidadesVisitadas[a]][cidadesNaoVisitadas[k]] + matriz[cidadesNaoVisitadas[k]][cidadesVisitadas[a+1]] - matriz[cidadesVisitadas[a]][cidadesVisitadas[a+1]])
                    posicao = a+1
                    
        cidadesVisitadas.insert(posicao,cidadeEscolhida)
        cidadesNaoVisitadas.remove(cidadeEscolhida)
        menorValor = math.inf
 
    print("Cidades Visitadas:",cidadesVisitadas)
    print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    


###################################################################


def lerArquivo():
    
    filename = 'instancias/' + sys.argv[1]
    f = open(filename, 'r')
    qtdeVertices = int(f.readline())
    qtdeArestas = 0
    matrizAdjacencia = []
    inicializaMatrizQuadrada(qtdeVertices, matrizAdjacencia)

    for i in range(qtdeVertices-1):
        linha = f.readline()
        elementos = linha.rsplit()
        aux = 0
        for j in range(i+1, qtdeVertices):
            matrizAdjacencia[i][j] = int(elementos[aux])
            matrizAdjacencia[j][i] = int(elementos[aux])
            aux += 1
            
    return matrizAdjacencia,qtdeVertices

###################################################################

if __name__ == '__main__':

    matriz,tamanho = lerArquivo()
    #printMatriz(matriz,tamanho)
    insercaoMaisProximo(matriz,tamanho)
    insercaoMaisAfastada(matriz,tamanho)
    insercaoMaisBarata(matriz,tamanho)
    
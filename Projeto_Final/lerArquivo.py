import sys 
import math

def inicializaMatrizQuadrada(tamanho, matriz):
    for i in range(tamanho):
        matriz.append([])
        for j in range(tamanho):
            matriz[i].append(math.inf)


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
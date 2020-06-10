import numpy as np
import sys 
import math
from aresta import Aresta
from heapsort import heapSort

def makeSet(qtdeVertices):
    conjunto = []
    for i in range(qtdeVertices):
        conjunto.append([])
        conjunto[i].append(i)
    return conjunto

def makeArestas(matriz,qtdeVertices):
    arestas = []
    for i in range((qtdeVertices-1)):
        for j in range(i+1,qtdeVertices):
            if(matriz[i][j] > 0):
                arestas.append(Aresta(i,j,matriz[i][j]))
    return arestas

def isDifferent(conjunto, verticeA, verticeB):
    if(len(conjunto[verticeA]) == len(conjunto[verticeB])):
        for i in range(len(conjunto[verticeA])):
            if((conjunto[verticeA][i] in conjunto[verticeB]) == False ):
                return True
    else:
        return True

    return False

def union(conjunto,verticeA,verticeB):

    for i in range(len(conjunto[verticeB])):
        conjunto[verticeA].append(conjunto[verticeB][i])
    
    for j in range(1,len(conjunto[verticeA])):
        conjunto[conjunto[verticeA][j]] = conjunto[verticeA]


def kruskal(matriz,qtdeVertices):
    mstp = 0
    conjunto = makeSet(qtdeVertices)
    arestas = makeArestas(matriz,qtdeVertices)
    heapSort(arestas)
    
    for i in range(len(arestas)):
        if((isDifferent(conjunto, arestas[i].verticeA, arestas[i].verticeB)) == True):
            mstp += arestas[i].w
            union(conjunto,arestas[i].verticeA,arestas[i].verticeB) 
  
    print('MSTP: ',mstp)

#############################################

def criarMatrizQuadrada(n, matriz):
    for i in range(0, n):
        matriz.append([])
        for j in range(0, n):
            matriz[i].append(0)

def lerArquivo():
    
    filename = 'instancias/' + sys.argv[1]
    f = open(filename, 'r')
    qtdeVertices = int(f.readline())
    qtdeArestas = 0
    matrizAdjacencia = []
    criarMatrizQuadrada(qtdeVertices, matrizAdjacencia)

    for i in range(qtdeVertices-1):
        linha = f.readline()
        elementos = linha.rsplit()
        aux = 0
        for j in range(i+1, qtdeVertices):
            matrizAdjacencia[i][j] = int(elementos[aux])
            matrizAdjacencia[j][i] = int(elementos[aux])
            aux += 1
            
    return matrizAdjacencia,qtdeVertices



if __name__ == '__main__':

    entrada,qtdeVertices = lerArquivo()
    kruskal(entrada,qtdeVertices)
   
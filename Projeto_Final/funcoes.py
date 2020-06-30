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


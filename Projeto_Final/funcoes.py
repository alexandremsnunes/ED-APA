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

def copiaLista(lista):
    aux = []
    for i in range(len(lista)): aux.append(lista[i])
    return aux

def melhorConstrucao(matriz,maisProximo, maisAfastado, maisBarato):
    melhorcontrucao, melhorCusto = copiaLista(maisProximo), custoTotal(matriz,maisProximo)
    
    if(custoTotal(matriz,maisAfastado) < melhorCusto):
        melhorCusto = custoTotal(matriz,maisAfastado) 
        melhorcontrucao = copiaLista(maisAfastado)
    if(custoTotal(matriz,maisBarato) < melhorCusto):
        melhorCusto = custoTotal(matriz,maisBarato) 
        melhorcontrucao = copiaLista(maisBarato)
    
    return melhorcontrucao, melhorCusto
import math
import random
from funcoes import printMatriz,custoTotal
from heapSort import heapSort, heapSortmin

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
        
    #print("Cidades Visitadas:",cidadesVisitadas)
    #print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    return cidadesVisitadas,custoTotal(matriz,cidadesVisitadas)

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
    
    #print("Cidades Visitadas:",cidadesVisitadas)
    #print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    return cidadesVisitadas,custoTotal(matriz,cidadesVisitadas)


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
    
    #print("Cidades Visitadas:",cidadesVisitadas)
    #print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    return cidadesVisitadas,custoTotal(matriz,cidadesVisitadas)
    

################################## Randomicas ################################################

def insercaoMaisProximoRandomico(matriz,tamanho):
    cidadesVisitadas,cidadeAtual,candidatos = [],0,[]
     
    cidadesVisitadas.append(0)

    while(len(cidadesVisitadas) < tamanho):
        #print(cidadesVisitadas)
        for i in range(tamanho):
            if((i in cidadesVisitadas) == False and i != cidadeAtual):
                candidatos.append((i, matriz[cidadeAtual][i]))
        
        heapSort(candidatos)
        candidatos.append((0,math.inf))
        proximaCidade = random.choice(candidatos[:(int(len(candidatos)/2))])
        proximaCidade = proximaCidade[0]      
        
        cidadeAtual = proximaCidade
        cidadesVisitadas.append(cidadeAtual)
        
        candidatos = []
        
    cidadesVisitadas.append(0)
        
    #print("Cidades Visitadas:",cidadesVisitadas)
    #print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    return cidadesVisitadas,custoTotal(matriz,cidadesVisitadas)

def insercaoMaisAfastadaRandomica(matriz,tamanho):
    cidadesVisitadas,cidadeAtual,candidatos = [],0,[]
    cidadesVisitadas.append(0)

    while(len(cidadesVisitadas) < tamanho):
        #print(cidadesVisitadas)
        for i in range(tamanho):
            if((i in cidadesVisitadas) == False and i != cidadeAtual):
                candidatos.append((i, matriz[cidadeAtual][i]))

        heapSortmin(candidatos)
        #print(candidatos)
        candidatos.append((0,0))
        proximaCidade = random.choice(candidatos[:(int(len(candidatos)/2))])
        proximaCidade = proximaCidade[0]      
        
        cidadeAtual = proximaCidade
        cidadesVisitadas.append(cidadeAtual)
        
        candidatos = []
        
    cidadesVisitadas.append(0)
    
    #print("Cidades Visitadas:",cidadesVisitadas)
    #print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    return cidadesVisitadas,custoTotal(matriz,cidadesVisitadas)

def insercaoMaisBarataRandomica(matriz,tamanho):
    cidadesVisitadas,cidadesNaoVisitadas, menorValor,candidatos,cidadeEscolhida = [],[],math.inf,[],0
    
    for i in range(tamanho): cidadesNaoVisitadas.append(i)

    cidadesVisitadas.append(0)
    cidadesNaoVisitadas.remove(0)

    """ for i in range(tamanho):
        if(matriz[cidadesVisitadas[0]][i] < menorValor):
            cidadeEscolhida = i
            menorValor = matriz[cidadesVisitadas[0]][i] """
    for i in range(tamanho):
        if(i != cidadeEscolhida):
            candidatos.append((i, matriz[cidadesVisitadas[0]][i]))

    heapSort(candidatos)
    candidatos.append((0,math.inf))
    cidadeEscolhida = random.choice(candidatos[:(int(len(candidatos)/2))])
    cidadeEscolhida = cidadeEscolhida[0]      

    cidadesVisitadas.append(cidadeEscolhida)
    cidadesNaoVisitadas.remove(cidadeEscolhida)
    candidatos = []
    
    """ for i in range(tamanho):
        if((matriz[i][cidadesVisitadas[0]]+matriz[cidadesVisitadas[1]][i]) < menorValor and ((i in cidadesVisitadas) == False) ):
            cidadeEscolhida = i
            menorValor = matriz[i][cidadesVisitadas[0]]+matriz[cidadesVisitadas[1]][i] """

    for i in range(tamanho):
        if((i in cidadesNaoVisitadas) == True):
            candidatos.append((i, matriz[i][cidadesVisitadas[0]]+matriz[cidadesVisitadas[1]][i]))
    
    heapSort(candidatos)
    candidatos.append((0,math.inf))
    cidadeEscolhida = random.choice(candidatos[:(int(len(candidatos)/2))])
    cidadeEscolhida = cidadeEscolhida[0]      
    cidadesVisitadas.append(cidadeEscolhida)
    cidadesVisitadas.append(cidadesVisitadas[0])
    cidadesNaoVisitadas.remove(cidadeEscolhida)
    candidatos = []
 
    """  while(len(cidadesNaoVisitadas) > 0):
            for a in range(len(cidadesVisitadas)-1):
                for k in range(len(cidadesNaoVisitadas)):
                    if((matriz[cidadesVisitadas[a]][cidadesNaoVisitadas[k]] + matriz[cidadesNaoVisitadas[k]][cidadesVisitadas[a+1]] - matriz[cidadesVisitadas[a]][cidadesVisitadas[a+1]]) < menorValor):
                        cidadeEscolhida = cidadesNaoVisitadas[k]
                        menorValor = (matriz[cidadesVisitadas[a]][cidadesNaoVisitadas[k]] + matriz[cidadesNaoVisitadas[k]][cidadesVisitadas[a+1]] - matriz[cidadesVisitadas[a]][cidadesVisitadas[a+1]])
                        posicao = a+1 """

    while(len(cidadesNaoVisitadas) > 0):
        for a in range(len(cidadesVisitadas)-1):
            for k in range(len(cidadesNaoVisitadas)):            
                candidatos.append((cidadesNaoVisitadas[k], (matriz[cidadesVisitadas[a]][cidadesNaoVisitadas[k]] + matriz[cidadesNaoVisitadas[k]][cidadesVisitadas[a+1]] - matriz[cidadesVisitadas[a]][cidadesVisitadas[a+1]]),a+1))
        
        heapSort(candidatos)
        candidatos.append((0,math.inf))
        cidadeEscolhida = random.choice(candidatos[:(int(len(candidatos)/2))])
        cidadeEscolhida,posicao = cidadeEscolhida[0],cidadeEscolhida[2] 

        cidadesVisitadas.insert(posicao,cidadeEscolhida)
        cidadesNaoVisitadas.remove(cidadeEscolhida)
        candidatos = []
    
    #print("Cidades Visitadas:",cidadesVisitadas)
    #print("Custo Total:",custoTotal(matriz,cidadesVisitadas))
    return cidadesVisitadas,custoTotal(matriz,cidadesVisitadas)

def solucaoRamdomica(matriz,tamanho):
    solucao = []
    solucao.append(0)
    
    while(len(solucao) < tamanho):

        elemento = random.randint(1,tamanho-1)    
        if((elemento in solucao) == False):
            solucao.append(elemento) 

    solucao.append(0)
   
    return solucao, custoTotal(matriz,solucao)
from funcoes import copiaLista, custoTotal

def aplicaSwapCusto(matriz,solucao,i,j,custo):
    custoInicial,solucaoaux = custo,solucao[:]

    custoInicial = custoInicial - matriz[solucaoaux[i-1]][solucaoaux[i]]
    custoInicial = custoInicial - matriz[solucaoaux[i+1]][solucaoaux[i]]
    custoInicial = custoInicial - matriz[solucaoaux[j]][solucaoaux[j-1]]
    custoInicial = custoInicial - matriz[solucaoaux[j]][solucaoaux[j+1]]
        
    solucaoaux[i], solucaoaux[j] = solucaoaux[j], solucaoaux[i]  
     
    custoInicial = custoInicial + matriz[solucaoaux[i+1]][solucaoaux[i]]
    custoInicial = custoInicial + matriz[solucaoaux[i-1]][solucaoaux[i]]
    custoInicial = custoInicial + matriz[solucaoaux[j]][solucaoaux[j-1]]
    custoInicial = custoInicial + matriz[solucaoaux[j]][solucaoaux[j+1]]

    #print("Caminho:",solucaoaux,"Valor:",custoInicial)
    return custoInicial,solucaoaux

def reinsertion(matriz,solucao):
    menorCusto,melhorSolucao = custoTotal(matriz,solucao),solucao[:]
  
    for i in range(1,len(solucao)-1):
        for j in range(1,len(solucao)-1):
            if i != j :
                listaAux = melhorSolucao[:]
                #custoLocal,listaAux = aplicaSwapCusto(matriz,melhorSolucao,i,j,menorCusto)
                
                elemento = listaAux[i]
                listaAux.remove(elemento)
                listaAux.insert(j,elemento)
                custoLocal = custoTotal(matriz,listaAux)
                #print(listaAux)
                if(custoLocal < menorCusto):
                    menorCusto = custoLocal
                    melhorSolucao = listaAux[:]    

    #print("Melhor Solucao reinsertion: Custo = ",menorCusto)
    return melhorSolucao,menorCusto



def swapTwoOpt(matriz,solucao,i,j):
    
    solucaoAux = solucao[:i]
    aux = solucao[i:j+1] 
    solucaoAux += aux[::-1]
    solucaoAux += solucao[j+1:]
    
    return solucaoAux



def twoOpt(matriz,solucao):
    menorCusto,melhorSolucao = custoTotal(matriz,solucao),solucao[:]
  
    for i in range(1,len(solucao)-2):
        for j in range(i+1,len(solucao)-1):
        
            listaAux = swapTwoOpt(matriz,melhorSolucao,i,j)

            if(custoTotal(matriz,listaAux) < menorCusto):
                menorCusto = custoTotal(matriz,listaAux)
                melhorSolucao = listaAux[:]    

    #print("Melhor Solucao twoOpt: Custo = ",menorCusto)
    return melhorSolucao,menorCusto

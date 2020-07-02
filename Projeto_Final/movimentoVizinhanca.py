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

def twoOpt(matriz,solucao):
    menorCusto,melhorSolucao = custoTotal(matriz,solucao),solucao[:]
    
    
    for i in range(1,len(solucao)-2):
        for j in range(i+1,len(solucao)-1):
            
            custoLocal,listaAux = aplicaSwapCusto(matriz,melhorSolucao,i,j,menorCusto)

            if(custoLocal < menorCusto):
                menorCusto = custoLocal
                melhorSolucao = listaAux[:]    

    print("Melhor Solucao: Custo = ",menorCusto)
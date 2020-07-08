from movimentoVizinhanca import twoOpt,reinsertion

def vnd(matriz,custo,solucao):
    menorCusto,melhorSolucao,parada = custo, solucao[:],True
    

    while(parada == True):
        solucaoAtual,custoAtual = reinsertion(matriz,melhorSolucao)
        if( custoAtual < menorCusto):
            melhorSolucao = solucaoAtual
            menorCusto = custoAtual
        else:
            solucaoAtual,custoAtual = twoOpt(matriz,melhorSolucao)
            if( custoAtual < menorCusto):
                melhorSolucao = solucaoAtual
                menorCusto = custoAtual
            else:
                parada = False

    #print("Melhor custo VND:",menorCusto)
    return melhorSolucao,menorCusto      
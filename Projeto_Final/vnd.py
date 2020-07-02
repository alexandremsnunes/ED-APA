from movimentoVizinhanca import twoOpt,reinsertion

def vnd(matriz,custo,solucao):
    menorCusto,melhorSolucao,m1,m2 = custo, solucao[:],True,True
    

    while(m1 == True or m2 == True):
        solucaoAtual,custoAtual = reinsertion(matriz,melhorSolucao)
        if( custoAtual < menorCusto):
            melhorSolucao = solucaoAtual
            menorCusto = custoAtual
            m1 = True
        else:
            m1 = False
            solucaoAtual,custoAtual = twoOpt(matriz,melhorSolucao)
            if( custoAtual < menorCusto):
                melhorSolucao = solucaoAtual
                menorCusto = custoAtual
                m2 = True
            else:
                m2 = False
            
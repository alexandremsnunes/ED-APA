import math
import time
from vnd import vnd
from funcoes import custoTotal
from construcaoSolucao import (insercaoMaisAfastada,insercaoMaisProximo,insercaoMaisBarata,
insercaoMaisProximoRandomico,insercaoMaisAfastadaRandomica,insercaoMaisBarataRandomica)


def construaSolucao(controle,matriz,tamanho):
    if (controle <= 30):
        return insercaoMaisAfastadaRandomica(matriz,tamanho)
    if (controle > 30 and controle <= 60):
        return insercaoMaisProximoRandomico(matriz,tamanho)
    if (controle > 60 and controle <= 100):
        return insercaoMaisBarataRandomica(matriz,tamanho)

def multiStart(matriz,tamanho):
    custoMultiStart,parada = math.inf,1
    inicio = time.time()
    while(parada <= 100):
        solucaoAux,custoAux = construaSolucao(parada,matriz,tamanho)
        solucaoAux,custoAux = vnd(matriz,custoAux,solucaoAux)
        if(custoAux < custoMultiStart):
            custoMultiStart = custoAux
            solucaoMultiStart = solucaoAux
            print("")
            

        parada += 1
        fim = time.time()
        print("\033[K", str(math.trunc(parada)) + "%" + " - Custo Atual:" + str(custoMultiStart)+ " - Time: "+ str(fim - inicio), end="\r")

    fim = time.time()
    print("\nCusto Multi Start: ", custoMultiStart," - Time: ",str(fim - inicio))
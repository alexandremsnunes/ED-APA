import numpy as np
import math
from lerArquivo import lerArquivo,lerArquivo2
from funcoes import printMatriz,custoTotal,melhorConstrucao
from construcaoSolucao import insercaoMaisProximo,insercaoMaisAfastada,insercaoMaisBarata,solucaoRamdomica,insercaoMaisProximoRandomico,insercaoMaisAfastadaRandomica, insercaoMaisBarataRandomica
from movimentoVizinhanca import twoOpt,reinsertion
from vnd import vnd
from multistart import multiStart

if __name__ == '__main__':
    
    try:
        matriz,tamanho = lerArquivo2()
    except IndexError:
        matriz,tamanho = lerArquivo()
    
    #printMatriz(matriz,tamanho)
    #listaMaisProximo, custoMaisProximo = insercaoMaisProximoRandomico(matriz,tamanho)
    #listaMaisAfastada, custoMaisAfastada = insercaoMaisAfastadaRandomica(matriz,tamanho)
    #listaMaisBarata, custoMaisBarata =  insercaoMaisBarata(matriz,tamanho)

    #print("Caminho Insercao Mais Proxima: ", listaMaisBarata,"  Custo = ",custoMaisBarata)
    #print("Caminho Insercao Mais Afastada:  Custo = ",custoMaisAfastada)
    #print("Caminho Insercao Mais Barata:  Custo = ",custoMaisBarata,"\n")
    
    #reinsertion(matriz,listaMaisProximo)
    #melhorSolucao,menorCusto = reinsertion(matriz,listaMaisBarata)
    #melhorSolucao2,menorCusto2 = reinsertion2(matriz,listaMaisBarata)
    #print("")
    #twoOpt(matriz,listaMaisProximo)
    #twoOpt(matriz,listaMaisAfastada)
    #twoOpt(matriz,listaMaisBarata)
    

    multiStart(matriz,tamanho)
    
import numpy as np
import math
from lerArquivo import lerArquivo,lerArquivo2
from funcoes import printMatriz,custoTotal,melhorConstrucao
from construcaoSolucao import insercaoMaisProximo,insercaoMaisAfastada,insercaoMaisBarata
from movimentoVizinhanca import twoOpt,reinsertion 
from vnd import vnd

if __name__ == '__main__':
    
    try:
        matriz,tamanho = lerArquivo2()
    except IndexError:
        matriz,tamanho = lerArquivo()
    
    #printMatriz(matriz,tamanho)
    listaMaisProximo, custoMaisProximo = insercaoMaisProximo(matriz,tamanho)
    listaMaisAfastada, custoMaisAfastada = insercaoMaisAfastada(matriz,tamanho)
    listaMaisBarata, custoMaisBarata = insercaoMaisBarata(matriz,tamanho)

    print("Caminho Insercao Mais Proxima:  Custo = ",custoMaisProximo)
    print("Caminho Insercao Mais Afastada:  Custo = ",custoMaisAfastada)
    print("Caminho Insercao Mais Barata:  Custo = ",custoMaisBarata,"\n")
    
    #reinsertion(matriz,listaMaisProximo)
    #reinsertion(matriz,listaMaisAfastada)
    #reinsertion(matriz,listaMaisBarata)
    #print("")
    #twoOpt(matriz,listaMaisProximo)
    #twoOpt(matriz,listaMaisAfastada)
    #twoOpt(matriz,listaMaisBarata)


    vnd(matriz,custoMaisBarata,listaMaisBarata)

    

    
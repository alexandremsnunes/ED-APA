import numpy as np
import math
from lerArquivo import lerArquivo,lerArquivo2
from funcoes import printMatriz,custoTotal,melhorConstrucao
from construcaoSolucao import insercaoMaisProximo,insercaoMaisAfastada,insercaoMaisBarata
from movimentoVizinhanca import twoOpt

if __name__ == '__main__':

    matriz,tamanho = lerArquivo()
    
    
    #printMatriz(matriz,tamanho)
    listaMaisProximo, custoMaisProximo = insercaoMaisProximo(matriz,tamanho)
    listaMaisAfastada, custoMaisAfastada = insercaoMaisAfastada(matriz,tamanho)
    listaMaisBarata, custoMaisBarata = insercaoMaisBarata(matriz,tamanho)

    print("Caminho Insercao Mais Proxima:  Custo = ",custoMaisProximo)
    print("Caminho Insercao Mais Afastada:  Custo = ",custoMaisAfastada)
    print("Caminho Insercao Mais Barata:  Custo = ",custoMaisBarata,"\n")
    
    #melhorLista, melhorcusto = melhorConstrucao(matriz,listaMaisProximo,listaMaisAfastada,listaMaisBarata)
    
    #print("Melhor Caminho das 3: Custo = ",melhorcusto,"\n")
    
    twoOpt(matriz,listaMaisProximo)
    twoOpt(matriz,listaMaisAfastada)
    twoOpt(matriz,listaMaisBarata)

    
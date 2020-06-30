import numpy as np
import math
from lerArquivo import lerArquivo
from funcoes import printMatriz
from construcaoSolucao import insercaoMaisProximo,insercaoMaisAfastada,insercaoMaisBarata


if __name__ == '__main__':

    matriz,tamanho = lerArquivo()
    #printMatriz(matriz,tamanho)
    insercaoMaisProximo(matriz,tamanho)
    insercaoMaisAfastada(matriz,tamanho)
    insercaoMaisBarata(matriz,tamanho)
    
import numpy as np
import math
from lerArquivo import *
from multistart import multiStart

if __name__ == '__main__':
    
    try:
        matriz,tamanho = lerArquivo2()
    except IndexError:
        matriz,tamanho = lerArquivo()
    
    multiStart(matriz,tamanho)
    
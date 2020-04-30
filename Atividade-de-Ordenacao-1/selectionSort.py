import numpy as np
import sys 
import math

def selectionSort(entrada, tam):

    for i in range(tam-1):
        menor = i

        for j in range((i+1),tam):
            if(entrada[j] < entrada[menor]): menor = j

        if(menor != i):
            aux = entrada[i]
            entrada[i] = entrada[menor]
            entrada[menor] = aux

        porcento = (i/len(entrada)) * 100
        print("\033[K", str(math.trunc(porcento)) + "%", end="\r")

    return entrada

def lerArquivo():
    arquivo = 'instancias-num/' + sys.argv[1]
    f = open(arquivo,'r')
    conteudo = f.readlines()
    entrada = []   
    for i in range(len(conteudo)): entrada.append(int(conteudo[i]))
    return entrada

def escreveResultado(saida):
    arquivo = 'resposta-selection-' + sys.argv[1]
    f = open(arquivo, 'w')
    res = []
    for i in range(len(saida)): res.append(str(saida[i])+'\n')
    f.writelines(res)

if __name__ == '__main__':

    print("Lendo arquivo...")
    entrada = lerArquivo()
    print("Arquivo Lido!!")
    print("\nProcessando...")
    saida = selectionSort(entrada, len(entrada))
    print("\nProcessado!!!")
    print("Escrevendo Arquivo...")
    escreveResultado(saida)
    print("Concluído!")

import numpy as np
import sys 

def selectionSort(entrada, tam):

    for i in range(tam-1):
        menor = i

        for j in range((i+1),tam):
            if(entrada[j] < entrada[menor]): menor = j

        if(menor != i):
            aux = entrada[i]
            entrada[i] = entrada[menor]
            entrada[menor] = aux

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

    entrada = lerArquivo()
    #print("Entrada:")
    #print(entrada)
    saida = selectionSort(entrada, len(entrada))
    #print("Saída:")
    #print(saida)
    escreveResultado(saida)
    print("Concluído!")

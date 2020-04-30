import numpy as np
import sys 
import math
import time

def coutingSort(lista):
    B,C,k = [],[],max(lista)

    for i in range(k+1): C.append(0)
    for j in range(len(lista)): 
        C[lista[j]] += 1
        B.append(0)
    for i in range(1,k+1): C[i] = C[i] + C[i-1]
    for j in range((len(lista)-1), -1, -1):
        B[C[lista[j]]-1] = lista[j]
        C[lista[j]] = C[lista[j]] - 1
    
    return B


def lerArquivo():
    arquivo = 'instancias-num/' + sys.argv[1]
    f = open(arquivo,'r')
    conteudo = f.readlines()
    entrada = []   
    for i in range(len(conteudo)): 
        if(int(conteudo[i]) >= 0):
            entrada.append(int(conteudo[i]))
    return entrada

def escreveResultado(saida):
    arquivo = 'resposta-coutingSort-' + sys.argv[1]
    f = open(arquivo, 'w')
    res = []
    for i in range(len(saida)): res.append(str(saida[i])+'\n')
    f.writelines(res)

if __name__ == '__main__':
    
    print("Lendo arquivo...")
    entrada = lerArquivo()
    print("Arquivo Lido!!")
    print("\nProcessando...")
    start = time.time()
    saida = coutingSort(entrada)
    finish = time.time()
    print("\nProcessado em: ",(finish - start), "s")
    print("Escrevendo Arquivo...")
    escreveResultado(saida)
    #print(saida)
    print("Concluído!")
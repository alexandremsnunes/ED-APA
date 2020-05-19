import numpy as np
import sys 
import math

def maxHeapify(vetor,lenHeap,i):
    left = 2*i + 1
    right = 2*i + 2
    
    if((left < lenHeap) and (vetor[left] > vetor[i])): maior = left    
    else: maior = i
    if((right < lenHeap) and (vetor[right] > vetor[maior])): maior = right
    if(maior != i):
        vetor[i],vetor[maior] = vetor[maior],vetor[i]
        maxHeapify(vetor,lenHeap,maior)

def buildMaxHeap(vetor,lenHeap):
    for i in range(int(lenHeap/2) - 1, -1, -1): 
        maxHeapify(vetor, lenHeap, i) 

def heapSort(vetor):
    lenHeap = len(vetor)
    buildMaxHeap(vetor,lenHeap)
    for i in range(lenHeap-1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        maxHeapify(vetor,i,0)
    return vetor

def lerArquivo():
    arquivo = 'instancias-num/' + sys.argv[1]
    f = open(arquivo,'r')
    conteudo = f.readlines()
    entrada = []   
    for i in range(len(conteudo)): entrada.append(int(conteudo[i]))
    return entrada

def escreveResultado(saida):
    arquivo = 'resposta-heap-' + sys.argv[1]
    f = open(arquivo, 'w')
    res = []
    for i in range(len(saida)): res.append(str(saida[i])+'\n')
    f.writelines(res)

if __name__ == '__main__':
    
    print("Lendo arquivo...")
    entrada = lerArquivo()
    print("Arquivo Lido!!")
    print("\nProcessando...")
    saida = heapSort(entrada)
    print("\nProcessado!!!")
    #print(saida)
    escreveResultado(saida)
    print("Concluído!")
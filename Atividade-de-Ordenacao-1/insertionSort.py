import numpy as np
import sys 
import math

def insertionSort(vetor):
    
    for i in range(1,len(vetor)):
        chave = vetor[i]
        j = i-1
        while(chave < vetor[j] and j >= 0):
            vetor[j+1] = vetor[j]
            j = j - 1
        
        vetor[j+1] = chave

        porcento = (i/len(vetor)) * 100
        print("\033[K", str(math.trunc(porcento)) + "%", end="\r")
    return vetor

def lerArquivo():
    arquivo = 'instancias-num/' + sys.argv[1]
    f = open(arquivo,'r')
    conteudo = f.readlines()
    entrada = []   
    for i in range(len(conteudo)): entrada.append(int(conteudo[i]))
    return entrada

def escreveResultado(saida):
    arquivo = 'resposta-insertion-' + sys.argv[1]
    f = open(arquivo, 'w')
    res = []
    for i in range(len(saida)): res.append(str(saida[i])+'\n')
    f.writelines(res)

if __name__ == '__main__':
    
    print("Lendo arquivo...")
    entrada = lerArquivo()
    print("Arquivo Lido!!")
    print("\nProcessando...")
    saida = insertionSort(entrada)
    print("\nProcessado!!!")
    print("Escrevendo Arquivo...")
    escreveResultado(saida)
    print("Concluído!")
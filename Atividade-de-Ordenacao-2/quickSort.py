import numpy as np
import sys 
import math
import time

def partition(lista,inicio,fim):
    pivo = lista[inicio]
    i = inicio + 1 
    j = fim
    
    while (i <= j):
        
        if(lista[i] <= pivo):
            i += 1
        elif(lista[j] > pivo):
            j -= 1
        elif(i <= j):
            lista[i],lista[j] = lista[j],lista[i]
            i+= 1
            j-=1

    lista[inicio],lista[j] = lista[j],lista[inicio]
        
    return j    


def quickSort(lista,l,r):
    if(l < r):
        q = partition(lista,l,r)
        quickSort(lista,l,q-1)
        quickSort(lista,q+1,r)

def lerArquivo():
    arquivo = 'instancias-num/' + sys.argv[1]
    f = open(arquivo,'r')
    conteudo = f.readlines()
    entrada = []   
    for i in range(len(conteudo)): entrada.append(int(conteudo[i]))
    return entrada

def escreveResultado(saida):
    arquivo = 'resposta-quickSort-' + sys.argv[1]
    f = open(arquivo, 'w')
    res = []
    for i in range(len(saida)): res.append(str(saida[i])+'\n')
    f.writelines(res)

if __name__ == '__main__':
    
    print("Lendo arquivo...")
    entrada = lerArquivo()
    print("Arquivo Lido!!")
   
    print("\nProcessando...")
    inicio,fim = 0, len(entrada)-1
    start = time.time()
    #print(entrada)
    quickSort(entrada,inicio,fim)
    finish = time.time()
    print("\nProcessado em: ",(finish - start), "s")
    print("Escrevendo Arquivo...")
    #print(entrada)
    escreveResultado(entrada)
    print("Concluído!")
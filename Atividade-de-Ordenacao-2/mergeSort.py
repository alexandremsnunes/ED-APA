import numpy as np
import sys 
import math
import time

def merge(lista,p,q,r):
    L, R,i,j = [],[],0,0    
    for a in range(p,q+1): L.append(lista[a]) 
    for a in range(q+1,r+1): R.append(lista[a])
    L.append(math.inf)
    R.append(math.inf)
    for k in range(p,r+1):
        if (L[i] < R[j]):
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1
    

def mergeSort(lista,p,r):
    if (p < r):
        q = int((p+r)/2)
        mergeSort(lista,p,q)
        mergeSort(lista,q+1,r)
        merge(lista,p,q,r)


def lerArquivo():
    arquivo = 'instancias-num/' + sys.argv[1]
    f = open(arquivo,'r')
    conteudo = f.readlines()
    entrada = []   
    for i in range(len(conteudo)): entrada.append(int(conteudo[i]))
    return entrada

def escreveResultado(saida):
    arquivo = 'resposta-mergeSort-' + sys.argv[1]
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
    mergeSort(entrada,inicio,fim)
    finish = time.time()
    print("\nProcessado em: ",(finish - start), "s")
    print("Escrevendo Arquivo...")
  
    escreveResultado(entrada)
    print("Concluído!")
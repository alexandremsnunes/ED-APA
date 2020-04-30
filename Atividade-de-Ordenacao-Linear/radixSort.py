import numpy as np
import sys 
import math
import time



def coutingSort(lista,exp):
    B,C,k = [],[],10

    for i in range(k): C.append(0)
    for j in range(len(lista)): 
        C[int((lista[j] / exp) % 10)] += 1 
        B.append(0)
    for i in range(1,k): C[i] = C[i] + C[i-1]
    for j in range((len(lista)-1), -1, -1):
        B[C[int((lista[j] / exp) % 10)]-1] = lista[j]
        C[int((lista[j] / exp) % 10)] = C[int((lista[j] / exp) % 10)] - 1
    
    return B

def radixSort(lista):
    maior, exp =  max(lista), 1
        
    while(int(maior/exp) > 0): 
        res = coutingSort(lista,exp)
        lista = res
        exp *= 10
    return res
 
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
    arquivo = 'resposta-radixSort-' + sys.argv[1]
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
    saida = radixSort(entrada)
    finish = time.time()
    print("\nProcessado em: ",(finish - start), "s")
    print("Escrevendo Arquivo...")
    escreveResultado(saida)
    #print(saida)
    print("Concluído!")
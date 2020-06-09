import numpy as np
import sys 
import math

def maxHeapify(vetor,lenHeap,i):
    left = 2*i + 1
    right = 2*i + 2
    
    if((left < lenHeap) and (vetor[left].w > vetor[i].w)): maior = left    
    else: maior = i
    if((right < lenHeap) and (vetor[right].w > vetor[maior].w)): maior = right
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
    #return vetor
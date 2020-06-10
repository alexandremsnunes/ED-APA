from heapq import heappop, heappush
import numpy as np
import sys 
import math
from heapsort import heapSort,minHeapify,buildMinHeap


def add_edge(graph,v, u, w):
    graph[v].append((u,w))
    graph[u].append((v,w)) 

def setChaveQ(Q,v,chave):
    for i in range(len(Q)):
        if(Q[i][0] == v):
            Q[i][1] = chave

def prim(graph,r,qtdeVertices):
    chave,pai = [],[]
    
    for u in range(qtdeVertices):
        chave.append(math.inf)
        

    chave[r] = 0
    
    Q = [[] for x in range(qtdeVertices)]
   
    for u in range(qtdeVertices):
        Q[u].append(u)
        Q[u].append(chave[u])
        
    buildMinHeap(Q,len(Q))
    
    while(len(Q) != 0):
        u = Q[0][0]
        x = Q[0]
        pai.append(x[0])
        Q.remove(x)
        
        for v in range(len(graph[u])):
            
            if(((graph[u][v][0] in pai) == False) and (graph[u][v][1] < chave[graph[u][v][0]])):
                
                chave[graph[u][v][0]] = graph[u][v][1]
                setChaveQ(Q,graph[u][v][0],graph[u][v][1])
                
           
        buildMinHeap(Q,len(Q))

    mst = 0
    for j in range(len(chave)):
        mst += chave[j]
    print("MSTP: ",mst)

def lerArquivo():
    
    filename = 'instancias/' + sys.argv[1]
    f = open(filename, 'r')
    qtdeVertices = int(f.readline())
    
    graph = [[] for x in range(qtdeVertices)]
    
    for i in range(qtdeVertices-1):
        linha = f.readline()
        elementos = linha.rsplit()
        aux = 0
        #print(elementos)
        for j in range(i+1, qtdeVertices):
            if(int(elementos[aux]) > 0):
                #print(i,j,int(elementos[aux]))
                add_edge(graph,i, j, int(elementos[aux])) 
            aux += 1    
            
    return qtdeVertices,graph



if __name__ == '__main__':
    
    qtdeVertices,graph = lerArquivo()
    
   
    #print(graph)
    #res = prim(graph, Vi=0, edge=[], vis=[])
    prim(graph,0,qtdeVertices)
    #total = 0
    #for k in range (len(res)):
    #    total += res[k][0] 
    #print(res)
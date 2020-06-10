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

def dijkstra(graph,r,qtdeVertices):
    chave,S = [],[]
    
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
        S.append(x[0])
        Q.remove(x)
        
        for v in range(len(graph[u])):
            
            if(((graph[u][v][0] in S) == False) and ((graph[u][v][1] + chave[u] ) < chave[graph[u][v][0]])):
                #print("chave do",graph[u][v][0],"era ",chave[graph[u][v][0]])
                chave[graph[u][v][0]] = graph[u][v][1] + chave[u]
                setChaveQ(Q,graph[u][v][0],(graph[u][v][1] + chave[u]))
                #print("Ficou ",chave[graph[u][v][0]])
           
        buildMinHeap(Q,len(Q))
        
    print("Caminho mínimo: ",chave[len(S)-1])
    

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
    dijkstra(graph,0,qtdeVertices)
   
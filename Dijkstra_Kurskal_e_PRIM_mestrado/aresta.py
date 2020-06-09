class Aresta:
    def __init__(self, verticeA, verticeB, w):
        self.verticeA = verticeA
        self.verticeB = verticeB
        self.w = w
     
    def setVerticeA(self, verticeA):
        self.verticeA = verticeA

    def setVerticeB(self, verticeB):
        self.verticeB = verticeB
       
    def setW(self, w):
        self.w = w
     
    def getVerticeA(self):
        return self.verticeA

    def getVerticeB(self):
        return self.verticeB
         
    def getW(self):
        return self.w

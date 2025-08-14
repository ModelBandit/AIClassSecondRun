import random

class Node:
    def __init__(self, dataList):
        self.__parameters = dataList
        self.bias = 0.02

    def getParam(self):
        return self.__parameters

class Layer:
    def __init__(self, nodeList, nextLayerNodeCount):
        self.nodes = nodeList
        self.weights = []

        for i in range(len(self.nodes)):
            weight = []
            for j in range(nextLayerNodeCount):
                weight.append(random.uniform(-1.0,1.0))
            self.weights.append(weight)

    def forward(self):
        num = 0
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i].getParam())):
                param = self.nodes[i].getParam()[j]
                w = self.weights[j]
                num += param * w
        
        num += self.bias
        return num
                
baseInput = [[0,1,0,1][0,0,1,1][0,1,1,0]]




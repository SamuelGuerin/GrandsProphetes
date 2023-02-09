import numpy as np

import Graph2 as Graph
import Form


def generateLulus():
    i = 0
    array1 = []
    array2 = []
    while i < 5:
        i += 1
        cpt = 0 
        array1.clear()
        while cpt < 100:
            array1.append(Lulu(np.random.normal(50,10, size=None),np.random.normal(50,6, size=None),np.random.normal(50,7, size=None)))
            cpt += 1
        array2.append(array1.copy())
    return array2


class Lulu:
    def __init__(self, speed, sense, size):
        self.Speed = speed
        self.Sense = sense
        self.Size = size

class Index:
    ind = 0
    elev = 30
    azim = 130

    def isMax(self):
        if self.ind == len(generations) - 1:
            return True
        return False
    
    def isMin(self):
        if self.ind == 0:
            return True
        return False

class graphGeneration:
        def next(index):
            index.ind += 1
            if index.ind > len(generations) - 1:
                index.ind = len(generations) - 1
            return Graph.generateGraph(generations[index.ind], index.ind + 1, index.elev, index.azim)
            
        def previous(index):
            index.ind -= 1
            if index.ind < 0:
                index.ind = 0
            return Graph.generateGraph(generations[index.ind], index.ind + 1, index.elev, index.azim)

        def first(index):
            index.ind = 0
            return Graph.generateGraph(generations[index.ind], index.ind + 1, index.elev, index.azim)
        
        def last(index):
            index.ind = len(generations) - 1
            return Graph.generateGraph(generations[index.ind], index.ind + 1, index.elev, index.azim)
        
        def speedSize(index):
            return Graph.generateGraph(generations[index.ind], index.ind + 1, 0, 90)
        
        def sizeSense(index):
            return Graph.generateGraph(generations[index.ind], index.ind + 1, 0, 0)
        
        def senseSpeed(index):
            return Graph.generateGraph(generations[index.ind], index.ind + 1, -92, 0.44)
        
generations = generateLulus()





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

class graphGeneration:
        def next(index):
            index.ind += 1
            if index.ind > len(generations) - 1:
                index.ind = len(generations) - 1
            return Graph.generateGraph(generations[index.ind], index.ind + 1)
            

        def previous(index):
            index.ind -= 1
            if index.ind < 0:
                index.ind = 0
            return Graph.generateGraph(generations[index.ind], index.ind + 1)

        def first(index):
            index.ind = 0
            return Graph.generateGraph(generations[index.ind], index.ind + 1)
        
        def last(index):
            index.ind = len(generations) - 1
            return Graph.generateGraph(generations[index.ind], index.ind + 1)

generations = generateLulus()





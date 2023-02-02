import numpy as np

import Graph
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
        def next(ind):
            ind += 1
            if ind > len(generations) - 1:
                ind = len(generations) - 1
            return Graph.generateGraph(generations[ind], ind + 1)
            

        def previous(ind):
            ind -= 1
            if ind < 0:
                ind = 0
            return Graph.generateGraph(generations[ind], ind + 1)

        def first(ind):
            ind = 0
            return Graph.generateGraph(generations[ind], ind + 1)
        
        def last(ind):
            ind = len(generations) - 1
            return Graph.generateGraph(generations[ind], ind + 1)

generations = generateLulus()





import numpy as np
import Graph2 as Graph

def generateLulus():
    i = 0
    array1 = []
    array2 = []
    while i < 100:
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
    xaxis = [0, 100]
    yaxis = [0, 100]
    zaxis = [0, 100]

    def isMax(self):
        """Fonction qui sert à savoir si ind est à la dernière génération.

            :return: `True` si ind est à la dernière génération. 
            :rtype: bool
        """
        if self.ind == len(generations) - 1:
            return True
        return False
    
    def isMin(self):
        """Fonction qui sert à savoir si ind est à la première génération.

            :return: `True` si ind est à la première génération. 
            :rtype: bool
        """

        if self.ind == 0:
            return True
        return False
    
    def setAxis(self):
        maxSpeed = 0
        maxSense = 0
        maxSize = 0

        for generation in generations:
            for i in range(len(generation[0])):
                if (generation[0][i] > maxSpeed):
                    maxSpeed = generation[0][i]
                if (generation[1][i] > maxSense):
                    maxSense = generation[1][i]
                if (generation[2][i] > maxSize):
                    maxSize = generation[2][i]
        
        self.xaxis = [0, maxSpeed * 1.3]
        self.yaxis = [0, maxSense * 1.3]
        self.zaxis = [0, maxSize * 1.3]


class graphGeneration:
        def next(index):
            """Va générer le graphique de la prochaine génération.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            index.ind += 1
            if index.ind > len(generations) - 1:
                index.ind = len(generations) - 1
            return Graph.generateGraph(generations[index.ind], index.ind + 1, [index.elev, index.azim, index.xaxis, index.yaxis, index.zaxis])
            
        def previous(index):
            """Va générer le graphique de la génération précédente.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            index.ind -= 1
            if index.ind < 0:
                index.ind = 0
            return Graph.generateGraph(generations[index.ind], index.ind + 1, [index.elev, index.azim, index.xaxis, index.yaxis, index.zaxis])

        def first(index):
            """Va générer le graphique de la première génération.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            index.ind = 0
            return Graph.generateGraph(generations[index.ind], index.ind + 1, [index.elev, index.azim, index.xaxis, index.yaxis, index.zaxis])
        
        def last(index):
            """Va générer le graphique de la dernière génération.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            index.ind = len(generations) - 1
            return Graph.generateGraph(generations[index.ind], index.ind + 1, [index.elev, index.azim, index.xaxis, index.yaxis, index.zaxis])
        
        def speedSize(index):
            """Cette fonction va changer l'angle de vu pour voir les axes Vitesse et Taille.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            return Graph.generateGraph(generations[index.ind], index.ind + 1, [0, 90, index.xaxis, index.yaxis, index.zaxis])
        
        def sizeSense(index):
            """Cette fonction va changer l'angle de vu pour voir les axes Taille et Vision.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            return Graph.generateGraph(generations[index.ind], index.ind + 1, [0, 0, index.xaxis, index.yaxis, index.zaxis])
        
        def senseSpeed(index):
            """Cette fonction va changer l'angle de vu pour voir les axes Vision et Vitesse.

                    :param index: L'index de type `Index` qui permet de garder en mémoire la génération actuelle.
                    :type index: `Index`

                    :return: `Figure`: Permet de dessiner le graphique.
                            `Axes`: Permet de garder les données du graphique 3d en mémoire.
                    :rtype: `[Figure, Axes]`
            """

            return Graph.generateGraph(generations[index.ind], index.ind + 1, [-92, 0.44, index.xaxis, index.yaxis, index.zaxis])
    
def objectsToCoordinates(lulus):
    """Cette fonction sert à transformer une liste de `Lulu` en liste de coordonnées.

            :param lulus: Liste de `Lulu` à transformer.
            :type lulus: `Lulu`

            :return: Liste de coordonnées pour générer des graphiques.
            :rtype: [[[float],[float],[float]]]
    """

    gens = []
    
    speeds = []
    senses = []
    sizes = []

    for generation in lulus:
        speeds.clear()
        senses.clear()
        sizes.clear()
        for lulu in generation:
            speeds.append(round(lulu[0], 2))
            senses.append(round(lulu[1], 2))
            sizes.append(round(lulu[2] / 100, 2))
        gens.append([speeds.copy(), senses.copy(), sizes.copy()])
    return gens

generations = []
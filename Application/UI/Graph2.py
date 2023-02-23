import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import gc
import matplotlib
matplotlib.use('agg')

global ax
global fig
global ax_stats
ax = None
fig = None
ax_stats = None

def generateColors(speeds, senses, sizes, colors):
    """Cette fonction assigne une valeur RGB pour chaque points

    :param speeds: Liste contenant les valeurs de la vitesse
    :type speeds: [float]

    :param senses: Liste contenant les valeurs de la vision
    :type senses: [float]

    :param sizes: Liste contenant les valeurs de la taille
    :type sizes: [float]

    :param colors: Liste contenant les valeurs de la couleur (valeur de la couleur rgb)
    :type colors: [[float]]
    """
    
    colors.clear()
    for i in range(len(speeds)):
        colors.append([speeds[i]/(max(speeds) * 1.3), senses[i]/(max(senses) * 1.3), sizes[i]/(max(sizes) * 1.5)])

def calculateCoordinates(generation, speeds, senses, sizes):

    speeds.clear()
    senses.clear()
    sizes.clear()
    for lulu in generation:
        speeds.append(lulu.Speed)
        senses.append(lulu.Sense)
        sizes.append(lulu.Size)

def setAxesLabel(ax):
    """Assigne les noms aux axes du graphique 3d.

    :param ax: Objet `Axes` du graphique 3d.
    :type ax: `Axes`
    """

    ax.set_xlabel('Vitesse', color='blue', fontweight='semibold')
    ax.set_ylabel('Vision', color='green', fontweight='semibold')
    ax.set_zlabel('Taille', color='red', fontweight='semibold') 

def setAxesSize(ax, sx, sy, sz):
    """Assigne une grosseur aux axes du graphique 3d.

    :param ax: Objet `Axes` du graphique 3d.
    :type ax: `Axes`

    :param sx: Taille de l'axe X.
    :type sx: float

    :param sy: Taille de l'axe Y.
    :type sy: float

    :param sz: Taille de l'axe Z.
    :type sz: float
    """

    ax.set_xlim(sx)
    ax.set_ylim(sy)
    ax.set_zlim(sz)

def setStats(ax, generation):
    """Génère les statistiques de la génération actuelle.

    :param ax: Objet `Axes` du graphique 2d servant de boîte pour les statistiques.
    :type ax: `Axes`

    :param generation: Liste des coordonnées de la génération actuelle.
    :type generation: [[[float],[float],[float]]]
    """
    plt.close('all')

    ax.clear()
    speed = [0,0,1000000]
    sense = [0,0,1000000]
    size = [0,0,1000000]

    for ind in range(len(generation[0])):
        #Speed
        speed[0] += generation[0][ind]
        if (generation[0][ind] > speed[1]):
            speed[1] = round(generation[0][ind])
        if (generation[0][ind] < speed[2]):
            speed[2] = round(generation[0][ind])
        #Sense
        sense[0] += generation[1][ind]
        if (generation[1][ind] > sense[1]):
            sense[1] = round(generation[1][ind])
        if (generation[1][ind] < sense[2]):
            sense[2] = round(generation[1][ind])
        #Size
        size[0] += generation[2][ind]
        if (generation[2][ind] > size[1]):
            size[1] = round(generation[2][ind])
        if (generation[2][ind] < size[2]):
            size[2] = round(generation[2][ind])
    
    speed[0] = round(speed[0] / len(generation[0]))
    sense[0] = round(sense[0] / len(generation[1]))
    size[0] = round(size[0] / len(generation[2]))

    # Population
    ax.text(0.15, 0.95, 'Population ', fontsize=15, fontweight='bold')
    ax.text(0.34, 0.90, str(len(generation[0])), fontsize=15, color='darkorange', fontweight='semibold')
    # Speed
    ax.text(0.03, 0.77, 'Vitesse \nMoyenne: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.77, str(speed[0]), fontsize=15, color='blue', fontweight='semibold')
    ax.text(0.03, 0.68, 'Vitesse \nMaximum: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.68, str(speed[1]), fontsize=15, color='blue', fontweight='semibold')
    ax.text(0.03, 0.59, 'Vitesse \nMinimum: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.59, str(speed[2]), fontsize=15, color='blue', fontweight='semibold')
    # Vision
    ax.text(0.03, 0.49, 'Vision \nMoyenne: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.49, str(sense[0]), fontsize=15, color='green', fontweight='semibold')
    ax.text(0.03, 0.40, 'Vision \nMaximum: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.40, str(sense[1]), fontsize=15, color='green', fontweight='semibold')
    ax.text(0.03, 0.31, 'Vision \nMinimum: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.31, str(sense[2]), fontsize=15, color='green', fontweight='semibold')
    # Size
    ax.text(0.03, 0.21, 'Taille \nMoyenne: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.21, str(size[0]), fontsize=15, color='red', fontweight='semibold')
    ax.text(0.03, 0.12, 'Taille \nMaximum: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.12, str(size[1]), fontsize=15, color='red', fontweight='semibold')
    ax.text(0.03, 0.03, 'Taille \nMinimum: ', fontsize=15, fontweight='bold')
    ax.text(0.7, 0.03, str(size[2]), fontsize=15, color='red', fontweight='semibold')
    #Draw
    Button(ax, '')

class Lulu:
    def __init__(self, speed, sense, size):
        self.Speed = speed
        self.Sense = sense
        self.Size = size

def generateGraph(generation, currentGeneration, position):
    """Génère le graphique 3d et ses statistiques.

    :param generation: Liste des coordonnées de la génération actuelle.
    :type generation: `[[[float],[float],[float]]]`

    :param currentGeneration: Numéro de la génération actuelle.
    :type currentGeneration: int

    :param elev: Angle de vue du graphique 3d.
    :type elev: float

    :param azim: Angle de vue du graphique 3d.
    :type azim: float

    :return: Retourne une `Figure` et un `Axes` pour dessiner le graphique et ses statistiques.
    :rtype: `[Figure, Axes]`
    """
    plt.close('all')

    global fig
    global ax
    global ax_stats

    plt.clf()
    plt.close("all")
    
    gc.collect()
    
    fig = None
    if ax != None:
        ax.clear()
    ax = None
    ax_stats = None

    fig, ax = plt.subplots(figsize=(16, 9))
    plt.axis('off')
    ax = plt.axes(projection="3d")
    plt.subplots_adjust(left=0.25)
    ax.set_title('Génération ' + str(currentGeneration))
    ax.elev = position[0]
    ax.azim = position[1]
    fig.subplots_adjust(bottom=0.2)

    speeds = generation[0]
    senses = generation[1]
    sizes = generation[2]
    colors = []

    generateColors(speeds,senses,sizes,colors)

    setAxesSize(ax, position[2], position[3], position[4])
    setAxesLabel(ax)

    ax.scatter(speeds, senses, sizes, c=colors)

    # Stats
    ax_stats = plt.axes([0.005, 0.05, 0.23, 0.9])
    setStats(ax_stats, generation)

    return [fig, ax]

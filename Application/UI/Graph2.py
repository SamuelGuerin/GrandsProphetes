import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import threading

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

def generateColors(speeds, senses, sizes, colors):
    colors.clear()
    for i in range(len(speeds)):
        colors.append([speeds[i]/100, senses[i]/100, sizes[i]/100])

def calculateCoordinates(generation, speeds, senses, sizes):
    speeds.clear()
    senses.clear()
    sizes.clear()
    for lulu in generation:
        speeds.append(lulu.Speed)
        senses.append(lulu.Sense)
        sizes.append(lulu.Size)

def setAxesLabel(ax):
    ax.set_xlabel('Vitesse', color='blue', fontweight='semibold')
    ax.set_ylabel('Vision', color='green', fontweight='semibold')
    ax.set_zlabel('Taille', color='red', fontweight='semibold') 

def setAxesSize(ax):
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.set_zlim([0,100])

def setStats(ax, generation):
    ax.clear()
    speed = [0,0,1000000]
    sense = [0,0,1000000]
    size = [0,0,1000000]

    for lulu in generation:
        #Speed
        speed[0] += lulu.Speed
        if (lulu.Speed > speed[1]):
            speed[1] = round(lulu.Speed)
        if (lulu.Speed < speed[2]):
            speed[2] = round(lulu.Speed)
        #Sense
        sense[0] += lulu.Sense
        if (lulu.Sense > sense[1]):
            sense[1] = round(lulu.Sense)
        if (lulu.Sense < sense[2]):
            sense[2] = round(lulu.Sense)
        #Size
        size[0] += lulu.Size
        if (lulu.Size > size[1]):
            size[1] = round(lulu.Size)
        if (lulu.Size < size[2]):
            size[2] = round(lulu.Size)
    
    speed[0] = round(speed[0] / len(generation))
    sense[0] = round(sense[0] / len(generation))
    size[0] = round(size[0] / len(generation))

    # Population
    ax.text(0.03, 0.91, 'Population: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.91, str(len(generation)), fontsize=9, color='darkorange', fontweight='semibold')
    # Speed
    ax.text(0.03, 0.77, 'Vitesse \nMoyenne: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.77, str(speed[0]), fontsize=9, color='blue', fontweight='semibold')
    ax.text(0.03, 0.69, 'Vitesse \nMaximum: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.69, str(speed[1]), fontsize=9, color='blue', fontweight='semibold')
    ax.text(0.03, 0.61, 'Vitesse \nMinimum: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.61, str(speed[2]), fontsize=9, color='blue', fontweight='semibold')
    # Vision
    ax.text(0.03, 0.51, 'Vision \nMoyenne: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.51, str(sense[0]), fontsize=9, color='green', fontweight='semibold')
    ax.text(0.03, 0.43, 'Vision \nMaximum: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.43, str(sense[1]), fontsize=9, color='green', fontweight='semibold')
    ax.text(0.03, 0.35, 'Vision \nMinimum: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.35, str(sense[2]), fontsize=9, color='green', fontweight='semibold')
    # Size
    ax.text(0.03, 0.25, 'Taille \nMoyenne: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.25, str(size[0]), fontsize=9, color='red', fontweight='semibold')
    ax.text(0.03, 0.17, 'Taille \nMaximum: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.17, str(size[1]), fontsize=9, color='red', fontweight='semibold')
    ax.text(0.03, 0.09, 'Taille \nMinimum: ', fontsize=9, fontweight='bold')
    ax.text(0.6, 0.09, str(size[2]), fontsize=9, color='red', fontweight='semibold')
    #Draw
    Button(ax, '')
    plt.draw()

class Lulu:
    def __init__(self, speed, sense, size):
        self.Speed = speed
        self.Sense = sense
        self.Size = size

def generateGraph(generation, currentGeneration):
    fig, ax = plt.subplots(figsize=(16,9))
    plt.axis('off')
    ax = plt.axes(projection="3d")
    plt.subplots_adjust(left=0.25)
    ax.set_title('Génération ' + str(currentGeneration))
    setAxesSize(ax)
    fig.subplots_adjust(bottom=0.2)

    speeds = []
    senses = []
    sizes = []
    colors = []

    calculateCoordinates(generation, speeds, senses, sizes)
    generateColors(speeds,senses,sizes,colors)

    setAxesLabel(ax)
    ax.scatter(speeds, senses, sizes, c=colors ,cmap='viridis')

    # Stats
    ax_stats = plt.axes([0.005, 0.05, 0.23, 0.9])
    setStats(ax_stats, generation)

    plt.show()
    return fig

test = generateLulus()
generateGraph(test[0], 1)
    
    

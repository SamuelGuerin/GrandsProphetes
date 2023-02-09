import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def generateColors(speeds, senses, sizes, colors):
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
    ax.set_xlabel('Vitesse', color='blue', fontweight='semibold')
    ax.set_ylabel('Vision', color='green', fontweight='semibold')
    ax.set_zlabel('Taille', color='red', fontweight='semibold') 

def setAxesSize(ax, sx, sy, sz):
    ax.set_xlim([0,sx])
    ax.set_ylim([0,sy])
    ax.set_zlim([0,sz])

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
    ax.text(0.15, 0.95, 'Population ', fontsize=15, fontweight='bold')
    ax.text(0.34, 0.90, str(len(generation)), fontsize=15, color='darkorange', fontweight='semibold')
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
    plt.draw()

class Lulu:
    def __init__(self, speed, sense, size):
        self.Speed = speed
        self.Sense = sense
        self.Size = size

def generateGraph(generation, currentGeneration, elev, azim):
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.axis('off')
    ax = plt.axes(projection="3d")
    plt.subplots_adjust(left=0.25)
    ax.set_title('Génération ' + str(currentGeneration))
    ax.elev = elev
    ax.azim = azim
    fig.subplots_adjust(bottom=0.2)

    speeds = []
    senses = []
    sizes = []
    colors = []

    calculateCoordinates(generation, speeds, senses, sizes)
    generateColors(speeds,senses,sizes,colors)

    setAxesSize(ax, max(speeds) * 1.5, max(senses) * 1.5, max(sizes) * 1.5)
    setAxesLabel(ax)

    ax.scatter(speeds, senses, sizes, c=colors)

    # Stats
    ax_stats = plt.axes([0.005, 0.05, 0.23, 0.9])
    setStats(ax_stats, generation)

    #plt.show()
    return [fig, ax]

#test = generateLulus()
#generateGraph(test[0], 1)
    
    

import Models.Territory as Territory
import time
from manim import *
from manim.utils.file_ops import open_file as open_media_file
from Models.Lulu import Lulu
from Models.Food import Food

generationMoves = []
class VisualizeLulus(Scene):
    def construct(self):

        items = Territory.getMap()
        # SIZE = 1/5 du plus petit x ou y?
        SIZE=Territory.getSizeX()/5 if Territory.getSizeX() < Territory.getSizeY() else Territory.getSizeY()/5
        # CENTERX = /2
        CENTERX = Territory.getSizeX()/2
        # CENTERY = /2
        CENTERY = Territory.getSizeY()/2

        groupdots = VGroup()

        maxSize = max(lulu.size for lulu in Territory.getLulus())
        minSize = min(lulu.size for lulu in Territory.getLulus())
        rangeOfSizes = maxSize - minSize

        for position in items:
            item = items.get(position)
            if(type(item) == Lulu):
                if(item.isDone):
                    rangeOfColors = rangeOfSizes/6
                    if item.size <= minSize + (rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_A)
                    elif item.size <= minSize + 2*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_B)
                    elif item.size <= minSize + 3*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_C)
                    elif item.size <= minSize + 4*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_D)
                    else:
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_E)
                else:
                    rangeOfColors = rangeOfSizes/6
                    if item.size <= minSize + (rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_A)
                    elif item.size <= minSize + 2*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_B)
                    elif item.size <= minSize + 3*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_C)
                    elif item.size <= minSize + 4*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_D)
                    else:
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_E)
            elif(type(item) == Food):
                dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=GREEN)
            groupdots.add(dot)

        self.add(groupdots)

def renderAnimation():
    """Génère une image de l'état actuel du :class:`Territory`
    """
    scene = VisualizeLulus()
    scene.render()

def newMap(sizeX, sizeY, foodCount, lulusCount):
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount, 0, 0, 0, 0, 0, 0, 0, 0)

    renderAnimation()

def __run__(sizeX, sizeY, foodCount, lulusCount, speedVariation, senseVariation, sizeVariation, energy, nbGeneration, mutateChance):
    speed = 25 
    sense = 25
    size = 1000
    sims = time.time()
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount,
                        speed, sense, energy * 10000, size, mutateChance, speedVariation, senseVariation, sizeVariation)
    
    global generation
    for generation in range(nbGeneration):
        st = time.time()
        print("generation " + str(generation))
        print("nombre de lulu: " + str(Territory.getLulus().__len__()))
        Territory.moveAll()
        Territory.resetWorld()
        Territory.dayResultLulu()
        generationMoves.append(Territory.getMoves())
        
        if (Territory.getLulus().__len__() == 0):
            break

        
        et = time.time()
        elapsed = et - st
        
        print("temps generation " + str(generation) + ": " + str(elapsed))
    
    simf = time.time()
    sime = simf - sims
        
    print("temps simulation: " + str(sime))
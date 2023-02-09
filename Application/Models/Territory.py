import random
from Models.Position import Position
from Models.Lulu import Lulu
from Models.Food import Food
import time
from manim import *

__sizeX = None
__sizeY = None
__lulusCount = None
__foodCount = None
__lulus = []
__map = {}
__energy = None
__moves = []
__numberOfFood = 0
EATING_RATIO = 1.2


def createMap(sizeX, sizeY, foodCount, lulusCount, speed, sense, energy, size):
    global __sizeX
    global __sizeY
    global __foodCount
    global __lulusCount
    global __energy
    __sizeX = sizeX
    __sizeY = sizeY
    __foodCount = foodCount
    __lulusCount = lulusCount
    __energy = energy

    # Créer x lulus dans la map (La map va de 0 à maxX ou maxY)
    # Les mettre sur le côté
    for _ in range(__lulusCount):
        maxX = __sizeX
        maxY = __sizeY
        luluCreated = False

        # Choisir un side à 0 ou maxSide, puis un random de l'autre coordonnée (x ou y)
        while (not luluCreated and len(__lulus) < (2 * maxX + 2 * maxY) - 4):
            if (bool(random.getrandbits(1))):
                rx = random.choice([1, maxX])
                ry = random.randint(1, maxY)
                luluCreated = __CreateLulu(
                    rx, ry, speed, sense, size, energy, 0, False)
            else:
                ry = random.choice([1, maxY])
                rx = random.randint(1, maxX)
                luluCreated = __CreateLulu(
                    rx, ry, speed, sense, size, energy, 0, False)

    setFood()

# private
def __CreateLulu(rx, ry, speed, sense, size, energyRemaining, FoodCollected, isDone) -> bool:
    # Créer une lulu si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Lulu(rPos, speed, sense, size,
                           energyRemaining, FoodCollected, isDone)
        # Ajouter la lulu dans la liste de lulus
        __lulus.append(__map[rPos])
        return True
    return False


# private
def __CreateFood(rx, ry) -> bool:
    # Créer une food si la case est vide
    global __numberOfFood
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Food(rPos)
        __numberOfFood += 1
        return True
    return False

# public
def getItem(x, y):
    item = __map.get(Position(x, y))
    return item


def getMap():
    return __map


def getSizeX():
    return __sizeX


def getSizeY():
    return __sizeY


def __deleteItem(position):
    del __map[position]

# Vérifie s'il est possible de faire le mouvement demandé
# return true si le move est fait, sinon false
def tryMove(oldPosition, newPosition) -> bool:
    # Vérifier si le mouvement est dans la map
    if ((newPosition.x >= 1 and newPosition.x <= getSizeX()) and (newPosition.y >= 1 and newPosition.y <= getSizeY())):
        # Vérifier s'il n'y a pas une lulu plus grosse ou égale
        itemInNewPosition = getItem(newPosition.x, newPosition.y)
        if (itemInNewPosition == None):
            moveLulu(oldPosition, newPosition)
            return True
        elif (type(itemInNewPosition) == Food):
            moveLulu(oldPosition, newPosition)
            return True
        elif (itemInNewPosition.size < __map[oldPosition].size / EATING_RATIO):
            moveLulu(oldPosition, newPosition)
            return True
    return False

# Todo : Gérer l'énergie avec la formule
def moveLulu(oldPosition, newPosition):
    # S'il y avait qqch sur la nouvelle case, l'enlever et ajouter 1 de nourriture
    currentLulu = __map[oldPosition]
    if (getItem(newPosition.x, newPosition.y) != None):
        currentLulu.foodAmount += 1
        # ToDo : Valider que la liste lulus ne la contient plus
        if (type(__map[newPosition]) == Lulu):
            __lulus.remove(__map[newPosition])
        __deleteItem(newPosition)
    __addItem(newPosition, currentLulu)
    __deleteItem(oldPosition)


def __addItem(position, item):
    __map[position] = item
    if (type(item) == Lulu):
        item.position = position


def reproduceLulu(Lulu):
    # 50% Chance de mutation
    newSpeed = Lulu.speed
    newSense = Lulu.sense
    newSize = Lulu.size
    if (bool(random.getrandbits(1))):
        newSpeed = round(Lulu.speed * random.uniform(0.66, 1.33))
        newSense = round(Lulu.sense * random.uniform(0.66, 1.33))
        newSize = round(Lulu.size * random.uniform(0.66, 1.33))

    i = 1
    rx = 0
    ry = 0
    searchingPos = True
    # Faire spawn le nouveau Lulu à côté de l'ancien
    if (Lulu.position.x == 0 or Lulu.position.x == __sizeX):
        rx = Lulu.position.x
        while (searchingPos):
            if (Lulu.position.y + i < __sizeY and getItem(Lulu.position.x, Lulu.position.y + i) == None):
                ry = Lulu.position.y + i
                searchingPos = False
            elif (Lulu.position.y - i > 0 and getItem(Lulu.position.x, Lulu.position.y - i) == None):
                ry = Lulu.position.y - i
                searchingPos = False
            elif (Lulu.position.y + i > __sizeY or Lulu.position.y - i < 0):
                ry = Lulu.position.y
                searchingPos = False
            else:
                i += 1

    else:
        ry = Lulu.position.y
        while (searchingPos):
            if (Lulu.position.x + i < __sizeX and getItem(Lulu.position.x + i, Lulu.position.y) == None):
                rx = Lulu.position.x + i
                searchingPos = False
            elif (Lulu.position.x - i > 0 and getItem(Lulu.position.x - i, Lulu.position.y) == None):
                rx = Lulu.position.x - i
                searchingPos = False
            elif (Lulu.position.x + i > __sizeX or Lulu.position.x - i < 0):
                rx = Lulu.position.x
                searchingPos = False
            else:
                i += 1

    __CreateLulu(rx, ry, newSpeed, newSense, newSize, __energy,
                 0, False)


def moveAll():
    lulusToMove = __lulus.copy()
    while (lulusToMove.__len__() > 0):
        
        print("nombre de survivants: " + str(sum(lulu.foodAmount >= 1 for lulu in getLulus())))
        time.sleep(0.2)
        renderAnimation()
        
        random.shuffle(lulusToMove)
        for lulu in lulusToMove:
            if not (lulu.move()):
                lulusToMove.remove(lulu)


def dayResultLulu():
    for lulu in __lulus:
        if (lulu.foodAmount == 0):
            __deleteItem(lulu.position)
            __lulus.remove(lulu)
        elif (lulu.foodAmount > 1):
            reproduceLulu(lulu)

def addMove(move):
    __moves.append(move)

def getMoves():
    return __moves

def printMap():
    print(__map)

def getLulus():
    return __lulus

def setFood():
    maxX = __sizeX
    maxY = __sizeY
    
    # Ajouter de la nourriture partout sauf sur le côté
    for _ in range(__foodCount):
        foodCreated = False
        while (not foodCreated and __numberOfFood < ((__sizeX - 2) * (__sizeY - 2))):
            rx = random.randint(2, maxX - 1)
            ry = random.randint(2, maxY - 1)
            foodCreated = __CreateFood(rx, ry)
            
def resetWorld():
    __map.clear()
    setFood()
    for lulu in __lulus:
        lulu.isDone = False
        lulu.energy = __energy
        __addItem(lulu.position, lulu)
        lulu.resetPosition() # Plante

class VisualizeLulus(Scene):
    def construct(self):

        items = getMap()
        # SIZE = 1/5 du plus petit x ou y?
        SIZE=getSizeX()/5 if getSizeX() < getSizeY() else getSizeY()/5
        # CENTERX = /2
        CENTERX = getSizeX()/2
        # CENTERY = /2
        CENTERY = getSizeY()/2

        groupdots = VGroup()

        maxSize = max(lulu.size for lulu in getLulus())
        minSize = min(lulu.size for lulu in getLulus())
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
    scene = VisualizeLulus()
    scene.render()
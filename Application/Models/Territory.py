import random
from Models.Position import Position
from Models.Lulu import Lulu
from Models.Food import Food

__sizeX = None
__sizeY = None
__lulusCount = None
__foodCount = None
__lulus = []
__map = {}
__energy = None
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
                    rx, ry, speed, sense, size, energy, 0, True)
            else:
                ry = random.choice([1, maxY])
                rx = random.randint(1, maxX)
                luluCreated = __CreateLulu(
                    rx, ry, speed, sense, size, energy, 0, True)

    # Ajouter de la nourriture partout sauf sur le côté
    for _ in range(__foodCount):
        foodCreated = False
        while (not foodCreated and __numberOfFood < ((sizeX - 2) * (sizeY - 2))):
            rx = random.randint(2, maxX - 1)
            ry = random.randint(2, maxY - 1)
            foodCreated = __CreateFood(rx, ry)


# private
def __CreateLulu(rx, ry, speed, sense, size, energyRemaining, FoodCollected, isEnabled) -> bool:
    # Créer une lulu si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Lulu(rPos, speed, sense, size,
                           energyRemaining, FoodCollected, rPos, isEnabled)
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
    currentLulu.energy -= 1
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
    newSpeed, newSense, newSize
    if (bool(random.getrandbits(1))):
        newSpeed = round(Lulu.speed * random.uniform(0.66, 1.33))
        newSense = round(Lulu.sense * random.uniform(0.66, 1.33))
        newSize = round(Lulu.size * random.uniform(0.66, 1.33))
    else:
        newSpeed = Lulu.speed
        newSense = Lulu.sense
        newSize = Lulu.size

    i = 1
    rx, ry = 0
    searchingPos = True
    # Faire spawn le nouveau Lulu à côté de l'ancien
    if (Lulu.position.x == 0 or Lulu.position.x == __sizeX):
        rx = Lulu.position.x
        while (searchingPos):
            if (Lulu.position.y + i < __sizeY and getItem(Lulu.position.x, Lulu.position.y + i) != None):
                ry = Lulu.position.y + i
                searchingPos = False
            elif (Lulu.position.y - i > 0 and getItem(Lulu.position.x, Lulu.position.y - i) != None):
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
            if (Lulu.position.x + i < __sizeY and getItem(Lulu.position.x + i, Lulu.position.y) != None):
                rx = Lulu.position.x + i
                searchingPos = False
            elif (Lulu.position.x - i > 0 and getItem(Lulu.position.x - i, Lulu.position.y) != None):
                rx = Lulu.position.x - i
                searchingPos = False
            elif (Lulu.position.x + i > __sizeY or Lulu.position.x - i < 0):
                rx = Lulu.position.x
                searchingPos = False
            else:
                i += 1

    __CreateLulu(rx, ry, newSpeed, newSense, newSize, __energy,
                 0, True)


def moveAll():
    lulusToMove = []
    lulusToMove.append(__lulus.copy)
    while (lulusToMove.__len__() > 0):
        random.shuffle(lulusToMove)
        for lulu in lulusToMove:
            if not (lulu.move()):
                lulusToMove.remove(lulu)


def dayResultLulu():
    for lulu in __lulus:
        if (lulu.foodAmount == 0):
            __lulus.remove(lulu)
        elif (lulu.foodAmount == 1):
            lulu.resetPosition()
        elif (lulu.foodAmount > 1):
            reproduceLulu(lulu)

# getItemsInSense(x, y, sense)

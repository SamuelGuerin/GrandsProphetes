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

def createMap(sizeX, sizeY, foodCount, lulusCount):
    global __sizeX
    global __sizeY
    global __foodCount
    global __lulusCount
    __sizeX = sizeX
    __sizeY = sizeY
    __foodCount = foodCount
    __lulusCount = lulusCount

    # Créer x lulus dans la map (La map va de 0 à maxX ou maxY)
    # Les mettre sur le côté
    for _ in range(__lulusCount):
            maxX = __sizeX
            maxY = __sizeY
            luluCreated = False

            # Choisir un side à 0 ou maxSide, puis un random de l'autre coordonnée (x ou y)
            while not (luluCreated) :
                if(bool(random.getrandbits(1))):
                    rx = random.choice([0, maxX])
                    ry = random.randint(0, maxY)
                    luluCreated = __CreateLulu(rx, ry, 2, 2, 2, 2, 2, 2, 2)
                else :
                    ry = random.choice([0, maxY])
                    rx = random.randint(0, maxX)
                    luluCreated = __CreateLulu(rx, ry, 2, 2, 2, 2, 2, 2, 2)

    # Ajouter de la nourriture partout sauf sur le côté
    for _ in range(__foodCount):
        foodCreated = False
        while not (foodCreated) :
            rx = random.randint(1, maxX - 1)
            ry = random.randint(1, maxY - 1)
            foodCreated = __CreateFood(rx, ry)

# private
def __CreateLulu(rx, ry, speed, sense, energyRemaining, FoodCollected, force, lastPostion, isEnabled) -> bool:
    # Créer une lulu si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Lulu(rPos, speed, sense, energyRemaining, FoodCollected, force, lastPostion, isEnabled)
        # Ajouter la lulu dans la liste de lulus
        __lulus.append(__map[rPos])
        return True
    return False

# private
def __CreateFood(rx, ry) -> bool:
    # Créer une food si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Food()
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

def __addItem(position, item):
    __map[position] = item
    if (type(item) == Lulu):
        item.position = position

def __deleteItem(position):
    del __map[position]

def moveLulu(oldPosition, newPosition):
    __addItem(newPosition, __map[oldPosition])
    __deleteItem(oldPosition)






# getItemsInSense(x, y, sense)
# reproduceLulu()
# dayResultLulu()
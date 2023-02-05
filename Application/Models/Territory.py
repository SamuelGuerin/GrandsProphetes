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
        __map[rPos] = Lulu(speed, sense, energyRemaining, FoodCollected, force, lastPostion, isEnabled)
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

def reproduceLulu(Lulu):
    #50% Chance de mutation
    newSpeed,newSense,newSize
    if(bool(random.getrandbits(1))):
        newSpeed = round(Lulu.speed * random.uniform(0.66,1.33))
        newSense = round(Lulu.sense * random.uniform(0.66,1.33))
        newSize = round(Lulu.size * random.uniform(0.66,1.33))
    else:
        newSpeed = Lulu.speed
        newSense = Lulu.sense
        newSize = Lulu.size

    i = 1
    rx,ry = 0
    searchingPos = True
    # Faire spawn le nouveau Lulu à côté de l'ancien
    if (Lulu.position.x == 0 or Lulu.position.x == __sizeX):
        rx = Lulu.position.x
        while (searchingPos):
            if(Lulu.position.y + i < __sizeY and getItem(Lulu.position.x, Lulu.position.y + i) != None):
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
            if(Lulu.position.x + i < __sizeY and getItem(Lulu.position.x + i, Lulu.position.y) != None):
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
    
    __CreateLulu(rx,ry,newSpeed,newSense,Lulu.energy,0,newSize,Position(rx,ry),False)
            
                





# getItemsInSense(x, y, sense)
# reproduceLulu()
def dayResultLulu():
    for lulu in __lulus:
        if (lulu.foodAmount == 0):
            __lulus.remove(lulu)
        elif (lulu.foodAmount == 1):
            lulu.resetPosition()
        elif (lulu.foodAmount > 1):
            reproduceLulu(lulu) 
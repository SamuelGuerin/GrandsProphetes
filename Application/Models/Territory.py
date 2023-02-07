"""Territory (territoire) agit comme un singleton, il s'agit d'une instance de la carte (map)
où les Lulus et la nourriture seront placés aléatoirement

| Territory contient les paramètres nécessaire à la génération de la carte:

================    ================================================================================================================
Nom du paramètre    Définition
================    ================================================================================================================
__sizeX             Taille de la carte sur l'axe des X
__sizeY             Taille de la carte sur l'axe des Y
__lulusCount        Le nombre de Lulus total
__foodCount         Le nombre de nourriture total
__lulus             Liste contenant toutes les Lulus
__map               Dictionnaire contenant les Lulus et la nourriture à chaque position de la carte
__numberOfFood      Nombre de nourriture qui ont été créée jusqu'à présent
EATING_RATIO        Valeur constante pour définir le ratio de grandeur a avoir pour manger une Lulu ou être mangé par une autre Lulu
STARTING_ENERGY     Valeur constante pour définir l'énergie de départ pour chaque Lulu
================    ================================================================================================================

| Offre aussi plusieurs méthodes utiles accessibles dans les autres classes:

=====================       =================================================================================================================================================
Méthode                     Action
=====================       =================================================================================================================================================      
:meth:`createMap`           Crée une carte (map) avec les paramètres donnés (__sizeX, sizeY, __foodCount, __lulusCount)
:meth:`__CreateLulu`        Crée une Lulu avec les paramètres donnés (rx, ry, speed, sense, size, energyRemaining, FoodCollected, isDone)
:meth:`__CreateFood`        Ajoute une nourriture sur la carte (map) à la position donnée en paramètres (rx, ry)
:meth:`__addItem`           Ajoute un item (Lulu ou nourriture) sur la carte à la :class:`Position` donnée en paramètres (item, :class:`Position`)
:meth:`__deleteItem`        Retire un item (Lulu ou nourriture) sur la carte à la :class:`Position` donnée en paramètres (item, :class:`Position`)
:meth:`getItem`             Obtient un item (Lulu ou nourriture) sur la carte à la :class:`Position` donnée en paramètres (item, :class:`Position`)
:meth:`getMap`              Retourne la carte (map)
:meth:`getSizeX`            Retourne la taille de l'axe des X de la carte (__sizeX)
:meth:`getSizeY`            Retourne la taille de l'axe des Y de la carte (__sizeY)
:meth:`getLulus`            Retourne la liste contenant toutes les Lulus
:meth:`printMap`            Affiche tous les items de la carte avec leur :class:`Position` dans la console (outil de débogage)
:meth:`tryMove`             Vérifie si la Lulu peut se déplacer d'un point A à un point B en faisant toutes les validations et confirmations nécessaires, retourne un booléen
:meth:`moveLulu`            Effectue le mouvement précédemment testé par la méthode :meth:`tryMove`
=====================       =================================================================================================================================================    

:return: N/A
:rtype: Module
"""

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
__numberOfFood = 0

EATING_RATIO = 1.2
STARTINGENERGY = 1000000

def createMap(sizeX, sizeY, foodCount, lulusCount):
    """Crée (instancie) une carte (map) avec une taille X et Y ainsi qu'un nombre donné de nourriture et de Lulus

    :param sizeX: Taille de la carte sur l'axe des X
    :type sizeX: int
    :param sizeY: Taille de la carte sur l'axe des Y
    :type sizeY: int
    :param foodCount: Nombre de nourriture total
    :type foodCount: int
    :param lulusCount: Nombre de Lulus total
    :type lulusCount: int
    """

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
            while (not luluCreated and len(__lulus) < (2 * maxX + 2 * maxY) - 4):
                if(bool(random.getrandbits(1))):
                    rx = random.choice([1, maxX])
                    ry = random.randint(1, maxY)
                    luluCreated = __CreateLulu(rx, ry, random.randint(1,50), random.randint(1,20), random.randint(100,500), STARTINGENERGY, 0, False)
                else :
                    ry = random.choice([1, maxY])
                    rx = random.randint(1, maxX)
                    luluCreated = __CreateLulu(rx, ry, random.randint(1,8), random.randint(1,20), random.randint(100,500), STARTINGENERGY, 0, False)

    # Ajouter de la nourriture partout sauf sur le côté
    for _ in range(__foodCount):
        foodCreated = False
        while ( not foodCreated and __numberOfFood < ((sizeX - 2) * (sizeY - 2))) :
            rx = random.randint(2, maxX - 1)
            ry = random.randint(2, maxY - 1)
            foodCreated = __CreateFood(rx, ry)

# private
def __CreateLulu(rx, ry, speed, sense, size, energyRemaining, FoodCollected, isDone) -> bool:
    # Créer une lulu si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Lulu(rPos, speed, sense, size, energyRemaining, FoodCollected, rPos, isDone)
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

def __addItem(position, item):
    __map[position] = item
    if (type(item) == Lulu):
        item.position = position

def __deleteItem(position):
    del __map[position]

# Vérifie s'il est possible de faire le mouvement demandé
# return true si le move est fait, sinon false
def tryMove(oldPosition, newPosition) -> bool:
    # Vérifier si le mouvement est dans la map
    if((newPosition.x >= 1 and newPosition.x <= getSizeX()) and (newPosition.y >= 1 and newPosition.y <= getSizeY())):
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

def printMap():
    print(__map)

def getLulus():
    return __lulus
"""Territory (territoire) agit comme un singleton, il s'agit d'une instance de la carte (map)
où les Lulus et la nourriture seront placés aléatoirement

| Territory contient les paramètres nécessaire à la génération de la carte:

================    ================================================================================================================
Nom du paramètre    Définition
================    ================================================================================================================
psizeX             Taille de la carte sur l'axe des X
psizeY             Taille de la carte sur l'axe des Y
plulusCount        Le nombre de Lulus total
pfoodCount         Le nombre de nourriture total
plulus             Liste contenant toutes les Lulus
pmap               Dictionnaire contenant les Lulus et la nourriture à chaque position de la carte
pnumberOfFood      Nombre de nourriture qui ont été créée jusqu'à présent
EATING_RATIO        Valeur constante pour définir le ratio de grandeur a avoir pour manger une Lulu ou être mangé par une autre Lulu
STARTING_ENERGY     Valeur constante pour définir l'énergie de départ pour chaque Lulu
================    ================================================================================================================

| Offre aussi plusieurs méthodes utiles accessibles dans les autres classes:

=====================       =================================================================================================================================================
Méthode                     Action
=====================       =================================================================================================================================================
:meth:`createMap`           Crée une carte (map) avec les paramètres donnés (sizeX, sizeY, foodCount, lulusCount)
:meth:`CreateLulu`        Crée une Lulu avec les paramètres donnés (rx, ry, speed, sense, size, energyRemaining, FoodCollected, isDone)
:meth:`CreateFood`        Ajoute une nourriture sur la carte (map) à la position donnée en paramètres (rx, ry)
:meth:`addItem`           Ajoute un item (Lulu ou nourriture) sur la carte à la :class:`Position` donnée en paramètres (item, :class:`Position`)
:meth:`deleteItem`        Retire un item (Lulu ou nourriture) sur la carte à la :class:`Position` donnée en paramètres (item, :class:`Position`)
:meth:`getItem`             Obtient un item (Lulu ou nourriture) sur la carte à la :class:`Position` donnée en paramètres (item, :class:`Position`)
:meth:`getMap`              Retourne la carte (map)
:meth:`getSizeX`            Retourne la taille de l'axe des X de la carte (sizeX)
:meth:`getSizeY`            Retourne la taille de l'axe des Y de la carte (sizeY)
:meth:`getLulus`            Retourne la liste contenant toutes les Lulus
:meth:`printMap`            Affiche tous les items de la carte avec leur :class:`Position` dans la console (outil de débogage)
:meth:`tryMove`             Vérifie si la Lulu peut se déplacer d'un point A à un point B en faisant toutes les validations et confirmations nécessaires, retourne un booléen
:meth:`moveLulu`            Effectue le mouvement précédemment testé par la méthode :meth:`tryMove`
=====================       =================================================================================================================================================

:return: N/A
:rtype: Module
"""

import random
from Position import Position
from Lulu import Lulu
from Food import Food
import time
#from manim import *

psizeX = None
psizeY = None
plulusCount = None
pfoodCount = None
plulus = []
pmap = {}
penergy = None
pnumberOfFood = 0
EATING_RATIO = 1.2


def createMap(sizeX, sizeY, foodCount, lulusCount, speed, sense, energy, size, mutateChance, speedVariation, senseVariation, sizeVariation):
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
    global psizeX
    global psizeY
    global pfoodCount
    global plulusCount
    global penergy
    global pmutateChance
    global pspeedVariation
    global psenseVariation
    global psizeVariation
    psizeX = sizeX
    psizeY = sizeY
    pfoodCount = foodCount
    plulusCount = lulusCount
    penergy = energy
    pmutateChance = mutateChance
    pspeedVariation = speedVariation /100
    psenseVariation = senseVariation /100
    psizeVariation = sizeVariation /100

    clearMap()

    # Créer x lulus dans la map (La map va de 0 à maxX ou maxY)
    # Les mettre sur le côté
    for _ in range(lulusCount):
        maxX = sizeX
        maxY = sizeY
        luluCreated = False

        # Choisir un side à 0 ou maxSide, puis un random de l'autre coordonnée (x ou y)
        while (not luluCreated and len(plulus) < (2 * maxX + 2 * maxY) - 4):
            if (bool(random.getrandbits(1))):
                rx = random.choice([1, maxX])
                ry = random.randint(1, maxY)
                luluCreated = CreateLulu(
                    rx, ry, speed, sense, size, energy, 0, False)
            else:
                ry = random.choice([1, maxY])
                rx = random.randint(1, maxX)
                luluCreated = CreateLulu(
                    rx, ry, speed, sense, size, energy, 0, False)

    setFood()

    for lulu in plulus:
        lulu.isNewBorn = False

def clearMap():
    """Supprime les données des listes de Lulus et map
	"""
    global plulus
    global pmap
    global pnumberOfFood
    plulus = []
    pmap = {}
    pnumberOfFood = 0

def CreateLulu(rx, ry, speed, sense, size, energyRemaining, FoodCollected, isDone) -> bool:
    """Crée une Lulu et la place sur les bords de la carte selon une position donnée et l'instancie avec des paramètres de base

    :param rx: Emplacement sur l'axe des X
    :type rx: int
    :param ry: Emplacement sur l'axe des Y
    :type ry: int
    :param speed: Vitesse de la :class:`Lulu`
    :type speed: int
    :param sense: Vision de la :class:`Lulu` (Portée)
    :type sense: int
    :param size: Taille de la :class:`Lulu` (Détermine sa force pour pouvoir manger ou se faire manger)
    :type size: int
    :param energyRemaining: L'énergie de la :class:`Lulu`, si l'énergie restante n'est pas assez élevée, la :class:`Lulu` ne peut plus se déplacer
    :type energyRemaining: int
    :param FoodCollected: Nombre de nourriture (:class:`Food`) déjà consommée
    :type FoodCollected: int
    :param isDone: Détermine si la :class:`Lulu` n'a plus d'énergie, qu'elle a donc fini sa journée
    :type isDone: bool
    :return: Retourne un booléen confirmant si la :class:`Lulu` a bien été ajoutée ou non
    :rtype: bool
    """

    # from Models.Position import Position
    # from Models.Lulu import Lulu
    
    # Créer une lulu si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        pmap[rPos] = Lulu(rPos, speed, sense, size,
                           energyRemaining, FoodCollected, isDone)
        # Ajouter la lulu dans la liste de lulus
        plulus.append(pmap[rPos])
        return True
    return False


# private
def CreateFood(rx, ry) -> bool:
    """Ajoute une nourriture sur la carte (map) à la position donnée en paramètres (rx, ry)

    :param rx: Emplacement sur l'axe des X où la nourriture (:class:`Food`) sera ajoutée
    :type rx: int
    :param ry: Emplacement sur l'axe des Y où la nourriture (:class:`Food`) sera ajoutée
    :type ry: int
    :return: Retourne un booléen confirmant si la nourriture (:class:`Food`) a bien été ajoutée ou non
    :rtype: bool
    """

    # from Models.Position import Position
    # from Models.Food import Food

    # Créer une food si la case est vide
    global pnumberOfFood
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        pmap[rPos] = Food(rPos)
        pnumberOfFood += 1
        return True
    return False

# public


def getItem(x, y):
    """Obtiens un item (:class:`Lulu` ou  nourriture (:class:`Food`)) dans le dictionnaire map (carte) selon sa :class:`Position` et retourne l'item trouvé

    :param x: Emplacement sur l'axe des X
    :type x: int
    :param y: Emplacement sur l'axe des Y
    :type y: int
    :return: Retourne un item (:class:`Lulu` ou  nourriture (:class:`Food`))
    :rtype: :class:`Position`
    """

    # from Models.Position import Position

    item = pmap.get(Position(x, y))
    return item


def getMap():
    """Retourne la map (carte) y permettant l'accès depuis d'autres classes du projet

    :return: Retourne l'objet map
    :rtype: dictionnary
    """
    return pmap


def getSizeX():
    """Retourne la taille de l'axe des X de la carte (map)

    :return: Retourne sizeX
    :rtype: int
    """
    return psizeX


def getSizeY():
    """Retourne la taille de l'axe des Y de la carte (map)

    :return: Retourne sizeY
    :rtype: int
    """
    return psizeY


def addItem(position, item):
    """Ajoute un item (valeur) (:class:`Lulu` ou  nourriture (:class:`Food`)) dans le dictionnaire map à une :class:`Position` donnée (clé)

    :param position: :class:`Position` à laquelle l'item (:class:`Lulu` ou  nourriture (:class:`Food`)) sera placé dans l'objet map (carte)
    :type position: :class:`Position`
    :param item: L'item (:class:`Lulu` ou  nourriture (:class:`Food`)) qui sera placé dans le dictionnaire map
    :type item: (:class:`Lulu` ou  nourriture (:class:`Food`))
    """

    # from Models.Lulu import Lulu

    pmap[position] = item
    if (type(item) == Lulu):
        item.position = position


def deleteItem(position):
    """Retire un item (valeur) (:class:`Lulu` ou  nourriture (:class:`Food`)) dans le dictionnaire map à une :class:`Position` donnée (clé)

    :param position: :class:`Position` à laquelle l'item (:class:`Lulu` ou  nourriture (:class:`Food`)) sera retiré de l'objet map (carte)
    :type position: :class:`Position`
    """
    del pmap[position]

# Vérifie s'il est possible de faire le mouvement demandé
# return true si le move est fait, sinon false


def tryMove(oldPosition, newPosition) -> bool:
    """Vérifie si la :class:`Lulu` peut se déplacer d'une :class:`Position` A à une :class:`Position` B en faisant toutes les validations et confirmations nécessaires

    :param oldPosition: L'ancienne :class:`Position` de la Lulu
    :type oldPosition: :class:`Position`
    :param newPosition: La nouvelle :class:`Position` de la Lulu
    :type newPosition: :class:`Position`
    :return: Retourne un booléen confirmant si la Lulu peut être déplacée ou non
    :rtype: bool
    """

    # from Models.Food import Food

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
        elif (itemInNewPosition.size < pmap[oldPosition].size / EATING_RATIO):
            moveLulu(oldPosition, newPosition)
            return True
    return False

# Todo : Gérer l'énergie avec la formule


def moveLulu(oldPosition, newPosition):
    """Déplace la :class:`Lulu` d'une :class:`Position` A à une :class:`Position` B

    :param oldPosition: L'ancienne :class:`Position` de la :class:`Lulu`
    :type oldPosition: :class:`Position`
    :param newPosition: La nouvelle :class:`Position` de la :class:`Lulu`
    :type newPosition: :class:`Position`
    """

    # from Models.Lulu import Lulu

    # S'il y avait qqch sur la nouvelle case, l'enlever et ajouter 1 de nourriture
    currentLulu = pmap[oldPosition]
    if (getItem(newPosition.x, newPosition.y) != None):
        currentLulu.foodAmount += 1
        # ToDo : Valider que la liste lulus ne la contient plus
        if (type(getItem(newPosition.x, newPosition.y)) == Lulu):
            plulus.remove(pmap[newPosition])
        deleteItem(newPosition)
    addItem(newPosition, currentLulu)
    deleteItem(oldPosition)


def reproduceLulu(Lulu):

    # from Models.Lulu import Lulu

    newSpeed = Lulu.speed
    newSense = Lulu.sense
    newSize = Lulu.size
    if (random.randint(1, 100) < pmutateChance):
        newSpeed = round(Lulu.speed * random.uniform(1 - pspeedVariation, 1 + pspeedVariation))
        newSense = round(Lulu.sense * random.uniform(1 - psenseVariation, 1 + psenseVariation))
        newSize = round(Lulu.size * random.uniform(1 - psizeVariation, 1 + psizeVariation))
        
    if (newSpeed < 1):
        newSpeed = 1
    if (newSense < 1):
        newSense = 1
    if (newSize < 1):
        newSize = 1

    i = 1
    rx = 0
    ry = 0
    searchingPos = True
    # Faire spawn le nouveau Lulu à côté de l'ancien
    if (Lulu.position.x == 0 or Lulu.position.x == psizeX):
        rx = Lulu.position.x
        while (searchingPos):
            if (Lulu.position.y + i < psizeY and getItem(Lulu.position.x, Lulu.position.y + i) == None):
                ry = Lulu.position.y + i
                searchingPos = False
            elif (Lulu.position.y - i > 0 and getItem(Lulu.position.x, Lulu.position.y - i) == None):
                ry = Lulu.position.y - i
                searchingPos = False
            elif (Lulu.position.y + i > psizeY or Lulu.position.y - i < 0):
                ry = Lulu.position.y
                searchingPos = False
            else:
                i += 1

    else:
        ry = Lulu.position.y
        while (searchingPos):
            if (Lulu.position.x + i < psizeX and getItem(Lulu.position.x + i, Lulu.position.y) == None):
                rx = Lulu.position.x + i
                searchingPos = False
            elif (Lulu.position.x - i > 0 and getItem(Lulu.position.x - i, Lulu.position.y) == None):
                rx = Lulu.position.x - i
                searchingPos = False
            elif (Lulu.position.x + i > psizeX or Lulu.position.x - i < 0):
                rx = Lulu.position.x
                searchingPos = False
            else:
                i += 1

    CreateLulu(rx, ry, newSpeed, newSense, newSize, penergy,
                 0, False)


def getLuluMap():

    # from Models.Lulu import Lulu

    count = 0
    for item in pmap.values():
        if (type(item) == Lulu):
            count += 1

    return count


def moveAll():

    # from Models.Lulu import Lulu

    lulusToMove = plulus.copy()
    while (lulusToMove.__len__() > 0):

        lulusToMove = plulus.copy()        
        # time.sleep(0.2)
        # renderAnimation()

        random.shuffle(lulusToMove)
        for lulu in lulusToMove[:]:
            if (getItem(lulu.position.x, lulu.position.y) == lulu):
                if not (lulu.move()):
                    lulusToMove.remove(lulu)
                # time.sleep(0.2)
                # renderAnimation()
            else:
                lulusToMove.remove(lulu)
        


def dayResultLulu():
    for lulu in plulus[:]:
        if (lulu.foodAmount == 0 and not lulu.isNewBorn):
            deleteItem(lulu.position)
            plulus.remove(lulu)
        elif (lulu.foodAmount > 1):
            reproduceLulu(lulu)

        lulu.foodAmount = 0
        lulu.isNewBorn = False


def printMap():
    """Affiche tous les items de la carte avec leur :class:`Position` dans la console (outil de débogage) 
    """
    print(pmap)


def getLulus():
    """Retourne la liste contenant toutes les Lulus

    :return: Liste de toutes les Lulus
    :rtype: Liste
    """
    return plulus


def setFood():
    maxX = psizeX
    maxY = psizeY
    pnumberOfFood = 0 # ?

    # Ajouter de la nourriture partout sauf sur le côté
    for _ in range(pfoodCount):
        foodCreated = False
        while (not foodCreated and pnumberOfFood < ((psizeX - 2) * (psizeY - 2))):
            rx = random.randint(2, maxX - 1)
            ry = random.randint(2, maxY - 1)
            foodCreated = CreateFood(rx, ry)


def resetWorld():
    pmap.clear()
    setFood()
    for lulu in plulus[:]:
        lulu.isDone = False
        lulu.energy = penergy
        addItem(lulu.position, lulu)
        
    for lulu in plulus[:]:
        lulu.resetPosition()


# class VisualizeLulus(Scene):
#     def construct(self):

#         items = getMap()
#         # SIZE = 1/5 du plus petit x ou y?
#         SIZE = getSizeX()/5 if getSizeX() < getSizeY() else getSizeY()/5
#         # CENTERX = /2
#         CENTERX = getSizeX()/2
#         # CENTERY = /2
#         CENTERY = getSizeY()/2

#         groupdots = VGroup()

#         maxSize = max(lulu.size for lulu in getLulus())
#         minSize = min(lulu.size for lulu in getLulus())
#         rangeOfSizes = maxSize - minSize

#         for position in items:
#             item = items.get(position)
#             if (type(item) == Lulu):
#                 if (item.isDone):
#                     rangeOfColors = rangeOfSizes/6
#                     if item.size <= minSize + (rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=RED_A)
#                     elif item.size <= minSize + 2*(rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=RED_B)
#                     elif item.size <= minSize + 3*(rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=RED_C)
#                     elif item.size <= minSize + 4*(rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=RED_D)
#                     else:
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=RED_E)
#                 else:
#                     rangeOfColors = rangeOfSizes/6
#                     if item.size <= minSize + (rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=BLUE_A)
#                     elif item.size <= minSize + 2*(rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=BLUE_B)
#                     elif item.size <= minSize + 3*(rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=BLUE_C)
#                     elif item.size <= minSize + 4*(rangeOfColors):
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=BLUE_D)
#                     else:
#                         dot = Dot([(position.x - CENTERX)/SIZE,
#                                   (position.y - CENTERY)/SIZE, 0], color=BLUE_E)
#             elif (type(item) == Food):
#                 dot = Dot([(position.x - CENTERX)/SIZE,
#                           (position.y - CENTERY)/SIZE, 0], color=GREEN)
#             groupdots.add(dot)

#         self.add(groupdots)


# def renderAnimation():
#     scene = VisualizeLulus()
#     scene.render()

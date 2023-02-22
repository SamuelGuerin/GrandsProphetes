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
import time
from manim import *

import pathlib
import sys
workingDirectory = pathlib.Path().resolve()
sys.path.append(str(workingDirectory) + '\Application')
import SimulationManager as Simulation

__sizeX = None
__sizeY = None
__lulusCount = None
__foodCount = None
__energy = None
__lulus = []
__map = {}
__moves = []
__numberOfFood = 0
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
    global __sizeX
    global __sizeY
    global __foodCount
    global __lulusCount
    global __energy
    global __mutateChance
    global __speedVariation
    global __senseVariation
    global __sizeVariation

    __sizeX = sizeX
    __sizeY = sizeY
    __foodCount = foodCount
    __lulusCount = lulusCount
    __energy = energy
    __mutateChance = mutateChance
    __speedVariation = speedVariation / 100
    __senseVariation = senseVariation / 100
    __sizeVariation = sizeVariation / 100

    clearMap()
    
    # Créer X nombre de Lulus dans la map (La map va de 0 à maxX ou maxY)
    # Les mettre sur le côté
    for _ in range(__lulusCount):
        maxX = __sizeX
        maxY = __sizeY
        luluCreated = False

        # Choisir des coordonnées aléatoire pour faire apparaître les Lulus tout le tour du périmètre
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

    for lulu in __lulus:
        lulu.isNewBorn = False


def clearMap():
    """Supprime les données des listes de Lulus et map
	"""
    global __lulus
    global __map
    global __numberOfFood
    __lulus = []
    __map = {}
    __numberOfFood = 0


def __CreateLulu(rx, ry, speed, sense, size, energyRemaining, FoodCollected, isDone) -> bool:
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
    # Créer une lulu si la case est vide
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Lulu(rPos, speed, sense, size,
                           energyRemaining, FoodCollected, isDone)
        # Ajouter la lulu dans la liste de lulus
        __lulus.append(__map[rPos])
        return True
    return False


def __CreateFood(rx, ry) -> bool:
    """Ajoute une nourriture sur la carte (map) à la position donnée en paramètres (rx, ry)

    :param rx: Emplacement sur l'axe des X où la nourriture (:class:`Food`) sera ajoutée
    :type rx: int
    :param ry: Emplacement sur l'axe des Y où la nourriture (:class:`Food`) sera ajoutée
    :type ry: int
    :return: Retourne un booléen confirmant si la nourriture (:class:`Food`) a bien été ajoutée ou non
    :rtype: bool
    """
    # Créer une food si la case est vide
    global __numberOfFood
    if (getItem(rx, ry) == None):
        rPos = Position(rx, ry)
        __map[rPos] = Food(rPos)
        __numberOfFood += 1
        return True
    return False


def getItem(x, y):
    """Obtiens un item (:class:`Lulu` ou  nourriture (:class:`Food`)) dans le dictionnaire __map (carte) selon sa :class:`Position` et retourne l'item trouvé

    :param x: Emplacement sur l'axe des X
    :type x: int
    :param y: Emplacement sur l'axe des Y
    :type y: int
    :return: Retourne un item (:class:`Lulu` ou  nourriture (:class:`Food`))
    :rtype: :class:`Position`
    """
    item = __map.get(Position(x, y))
    return item


def getMap():
    """Retourne la map (carte) y permettant l'accès depuis d'autres classes du projet

    :return: Retourne l'objet __map
    :rtype: dictionnary
    """
    return __map


def getSizeX():
    """Retourne la taille de l'axe des X de la carte (map)

    :return: Retourne __sizeX
    :rtype: int
    """
    return __sizeX


def getSizeY():
    """Retourne la taille de l'axe des Y de la carte (map)

    :return: Retourne __sizeY
    :rtype: int
    """
    return __sizeY


def __addItem(position, item):
    """Ajoute un item (valeur) (:class:`Lulu` ou  nourriture (:class:`Food`)) dans le dictionnaire __map à une :class:`Position` donnée (clé)

    :param position: :class:`Position` à laquelle l'item (:class:`Lulu` ou  nourriture (:class:`Food`)) sera placé dans l'objet __map (carte)
    :type position: :class:`Position`
    :param item: L'item (:class:`Lulu` ou  nourriture (:class:`Food`)) qui sera placé dans le dictionnaire __map
    :type item: (:class:`Lulu` ou  nourriture (:class:`Food`))
    """
    __map[position] = item
    if (type(item) == Lulu):
        item.position = position


def __deleteItem(position):
    """Retire un item (valeur) (:class:`Lulu` ou  nourriture (:class:`Food`)) dans le dictionnaire __map à une :class:`Position` donnée (clé)

    :param position: :class:`Position` à laquelle l'item (:class:`Lulu` ou  nourriture (:class:`Food`)) sera retiré de l'objet __map (carte)
    :type position: :class:`Position`
    """

    del __map[position]


def tryMove(oldPosition, newPosition) -> bool:
    """Vérifie si la :class:`Lulu` peut se déplacer d'une :class:`Position` A à une :class:`Position` B en faisant toutes les validations et confirmations nécessaires

    :param oldPosition: L'ancienne :class:`Position` de la Lulu
    :type oldPosition: :class:`Position`
    :param newPosition: La nouvelle :class:`Position` de la Lulu
    :type newPosition: :class:`Position`
    :return: Retourne un booléen confirmant si la Lulu peut être déplacée ou non
    :rtype: bool
    """
    # Vérifier si la nouvelle position est dans la map
    if ((newPosition.x >= 1 and newPosition.x <= getSizeX()) and (newPosition.y >= 1 and newPosition.y <= getSizeY())):
        # Vérifier le contenu de la case à la nouvelle position
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


def moveLulu(oldPosition, newPosition):
    """Déplace la :class:`Lulu` d'une :class:`Position` A à une :class:`Position` B

    :param oldPosition: L'ancienne :class:`Position` de la :class:`Lulu`
    :type oldPosition: :class:`Position`
    :param newPosition: La nouvelle :class:`Position` de la :class:`Lulu`
    :type newPosition: :class:`Position`
    """
    # S'il y avait quelque chose sur la nouvelle case, l'enlever et ajouter 1 de nourriture (foodAmount)
    currentLulu = __map[oldPosition]
    test = getItem(newPosition.x, newPosition.y)
    if (test != None):
        currentLulu.foodAmount += 1
        # ToDo : Valider que la liste lulus ne la contient plus
        if (type(test) == Lulu):
            if test in currentLulu.lulusInRange:
                currentLulu.lulusInRange.remove(test)
            __lulus.remove(__map[newPosition])
        else :
            currentLulu.foodInRange.remove(test)
        __deleteItem(newPosition)
    __addItem(newPosition, currentLulu)
    __deleteItem(oldPosition)


def reproduceLulu(Lulu):
    """Algorithme permettant à la lulu passée en paramètre de se reproduire.
    Fait muté la nouvelle lulu selon un pourcentage de chance et selon les
    variations passer dans le formulaire.

	:param Lulu: Lulu a reproduire
	:type Lulu: Lulu
	"""
    newSpeed = Lulu.speed
    newSense = Lulu.sense
    newSize = Lulu.size

    if (random.randint(1, 100) < __mutateChance):
        newSpeed = round(Lulu.speed * random.uniform(1 - __speedVariation, 1 + __speedVariation))
    if (random.randint(1, 100) < __mutateChance):
        newSense = round(Lulu.sense * random.uniform(1 - __senseVariation, 1 + __senseVariation))
    if (random.randint(1, 100) < __mutateChance):
        newSize = round(Lulu.size * random.uniform(1 - __sizeVariation, 1 + __sizeVariation))
        
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

    # Faire apparaître la nouvelle Lulu à côté de son parent
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


def getLuluMap():
    """Calcul le nombre de lulus présents dans la map

	:return: Quantité de lulus
	:rtype: int
	"""
    count = 0
    for item in __map.values():
        if (type(item) == Lulu):
            count += 1

    return count


def moveAll():
    """Algorithme qui permet à chaque lulu d'effectuer un mouvement à tour de rôle
	"""
    lulusToMove = __lulus.copy()

    while (lulusToMove.__len__() > 0):
        lulusToMove = __lulus.copy()   

        if(Simulation.check):
            break     

        random.shuffle(lulusToMove)
        for lulu in lulusToMove[:]:
            if(Simulation.check):
                break
            if (getItem(lulu.position.x, lulu.position.y) == lulu):
                if not (lulu.move()):
                    lulusToMove.remove(lulu)
            else:
                lulusToMove.remove(lulu)
        

def dayResultLulu():
    """Vérifie la quantité de nourriture que possède chaque lulu et décide si elle se reproduit, survit, ou meurt
	"""
    for lulu in __lulus[:]:
        if (lulu.foodAmount == 0 and not lulu.isNewBorn):
            __deleteItem(lulu.position)
            __lulus.remove(lulu)
        elif (lulu.foodAmount > 1):
            reproduceLulu(lulu)

        lulu.foodAmount = 0
        lulu.isNewBorn = False


def addMove(move):
    """Ajoute le mouvement effectué à la liste des mouvements

	:param move: Objet contenant le déplacement effectué
	:type move: Move
	"""
    __moves.append(move)


def getMoves():
    """Retourne la liste des mouvements effectués

	:return: Retourne la liste des mouvements effectués
	:rtype: list
	"""
    return __moves


def printMap():
    """Affiche tous les items de la carte avec leur :class:`Position` dans la console (outil de débogage) 
    """
    print(__map)


def getLulus():
    """Retourne la liste contenant toutes les Lulus

    :return: Liste de toutes les Lulus
    :rtype: Liste
    """
    return __lulus


def setFood():
    """Permet de mettre la nourriture de façon aléatoire dans la map
	"""
    maxX = __sizeX
    maxY = __sizeY

    # Ajouter de la nourriture partout sauf sur le périmètre de la map
    for _ in range(__foodCount):
        foodCreated = False
        while (not foodCreated and __numberOfFood < ((__sizeX - 2) * (__sizeY - 2))):
            rx = random.randint(2, maxX - 1)
            ry = random.randint(2, maxY - 1)
            foodCreated = __CreateFood(rx, ry)


def resetWorld():
    """Réinitialise la nourriture restante dans le monde.
    Réinitialise l'énergie et la nourriture des lulus.
    Réinitialise la position des lulus sur les côtés.
	"""
    __map.clear()

    global __numberOfFood
    __numberOfFood = 0
    setFood()
    
    for lulu in __lulus[:]:
        lulu.isDone = False
        lulu.energy = __energy
        __addItem(lulu.position, lulu)
        
    for lulu in __lulus[:]:
        lulu.resetPosition()

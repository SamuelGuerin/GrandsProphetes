"""Territory (territoire) agit comme un singleton, il s'agit d'une instance de la carte (map)
   où les Lulus et la nourriture seront placés aléatoirement

   Territory contient les paramètres nécessaire à la génération de la carte:
   ====================  ====================
   Nom du paramètre      Définition
   ====================  ====================
   __sizeX               Taille de la carte sur l'axe des X
   __sizeY               Taille de la carte sur l'axe des Y
   __lulusCount          Le nombre de Lulus total
   __foodCount           Le nombre de nourriture total
   __lulus               Liste contenant toutes les Lulus
   __map                 Dictionnaire contenant les Lulus et la nourriture à chaque position de la carte
   __numberOfFood        Nombre de nourriture qui ont été créée jusqu'à présent
   EATING_RATIO          Valeur constante pour définir le ratio de grandeur a avoir pour manger une Lulu ou être mangé par une autre Lulu
   STARTING_ENERGY       Valeur constante pour définir l'énergie de départ pour chaque Lulu


   Offre aussi plusieurs méthodes utiles accessibles dans les autres classes:
   ====================          ====================
   Méthodes                      Actions             
   ====================          ====================
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
STARTING_ENERGY = 1000000


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
                    luluCreated = __CreateLulu(rx, ry, random.randint(1,50), random.randint(1,20), random.randint(100,500), STARTING_ENERGY, 0, False)
                else :
                    ry = random.choice([1, maxY])
                    rx = random.randint(1, maxX)
                    luluCreated = __CreateLulu(rx, ry, random.randint(1,8), random.randint(1,20), random.randint(100,500), STARTING_ENERGY, 0, False)

    # Ajouter de la nourriture partout sauf sur le côté
    for _ in range(__foodCount):
        foodCreated = False
        while ( not foodCreated and __numberOfFood < ((sizeX - 2) * (sizeY - 2))) :
            rx = random.randint(2, maxX - 1)
            ry = random.randint(2, maxY - 1)
            foodCreated = __CreateFood(rx, ry)

# private
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
        __map[rPos] = Lulu(rPos, speed, sense, size, energyRemaining, FoodCollected, rPos, isDone)
        # Ajouter la lulu dans la liste de lulus
        __lulus.append(__map[rPos])
        return True
    return False

# private
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

# public
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
    """Déplace la :class:`Lulu` d'une :class:`Position` A à une :class:`Position` B

    :param oldPosition: L'ancienne :class:`Position` de la :class:`Lulu`
    :type oldPosition: :class:`Position`
    :param newPosition: La nouvelle :class:`Position` de la :class:`Lulu`
    :type newPosition: :class:`Position`
    """
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
    """Affiche tous les items de la carte avec leur :class:`Position` dans la console (outil de débogage) 
    """
    print(__map)

def getLulus():
    """Retourne la liste contenant toutes les Lulus

    :return: Liste de toutes les Lulus
    :rtype: Liste
    """
    return __lulus
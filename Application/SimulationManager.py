import Models.Territory as Territory
from Models.Lulu import Lulu
from Models.Food import Food
from Models.Saves import Save

global generation
generation = 0
generationMoves = []
generationsSave = Save()


def __run__(sizeX, sizeY, foodCount, lulusCount, speedVariation, senseVariation, sizeVariation, energy, nbGeneration, mutateChance):
    """ Appel la méthode createMap() et lance la simulation en exécutant les différentes 

	:param sizeX: Taille de la carte sur l'axe des X
    :type sizeX: int
    :param sizeY: Taille de la carte sur l'axe des Y
    :type sizeY: int
    :param foodCount: Nombre de nourriture total
    :type foodCount: int
    :param lulusCount: Nombre de Lulus total
    :type lulusCount: int
    :param speedVariation: Variation de la vitesse des lulus à la reproduction
	:type speedVariation: int
	:param senseVariation: Variation de la vision des lulus à la reproduction
	:type senseVariation: int
 	:param sizeVariation: Variation de la grosseur des lulus à la reproduction
	:type sizeVariation: int
	:param energy: Énergie des lulus à chaque début de génération
	:type energy: int
	:param nbGeneration: Nombre de générations que la simulation va produire
	:type nbGeneration: int
	:param mutateChance: Pourcentage de chance que la lulu mute lors de sa naissance
	:type mutateChance: int
	""" 
 
    speed = 25 
    sense = 25
    size = 1000
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount,
                        speed, sense, energy * 10000, size, mutateChance, speedVariation, senseVariation, sizeVariation)

    global check
    check  = False
    global generation
    global generationsSave
    generationsSave = Save(sizeX,sizeY,foodCount, lulusCount,energy,speedVariation,senseVariation,sizeVariation,mutateChance,nbGeneration, generations=[])

    for generation in range(nbGeneration):
        generationsSave.generations.append(Territory.getLulus().copy())
        Territory.moveAll()
        Territory.resetWorld()
        Territory.dayResultLulu()
        generationMoves.append(Territory.getMoves())

        if(check):
            break
        
        if (Territory.getLulus().__len__() == 0):
            break


def getGenerationsSave():
    return generationsSave

def setGenerationSave(data):
    global generationsSave
    generationsSave = data

import Models.Territory as Territory

# À enlever -> pour test
import random

generationMoves = []

def __run__(sizeX, sizeY, foodCount, lulusCount, speed, sense, size, energy, nbGeneration):
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount,
                        speed, sense, energy, size)

    for generation in range(nbGeneration):

        Territory.moveAll()
        Territory.resetWorld()
        Territory.dayResultLulu()
        generationMoves.append(Territory.getMoves())

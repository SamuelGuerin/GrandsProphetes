import Models.Territory as Territory

# À enlever -> pour test
import random


def __run__(sizeX, sizeY, foodCount, lulusCount, speed, sense, size, energy, nbGeneration):
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount,
                        speed, sense, energy,  random.randint(100,200)) # Remplacer random par size

    for generation in range(nbGeneration):

        Territory.moveAll()
        Territory.dayResultLulu()

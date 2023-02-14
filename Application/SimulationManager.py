import Models.Territory as Territory
import time

# À enlever -> pour test
import random


def __run__(sizeX, sizeY, foodCount, lulusCount, speedVariation, senseVariation, sizeVariation, energy, nbGeneration, mutateChance):
    speed = 25 
    sense = 25
    size = 1000
    sims = time.time()
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount,
                        speed, sense, energy, size, mutateChance, speedVariation, senseVariation, sizeVariation)

    for generation in range(nbGeneration):
        st = time.time()
        print("generation " + str(generation))
        print("nombre de lulu: " + str(Territory.getLulus().__len__()))
        Territory.moveAll()
        Territory.resetWorld()
        Territory.dayResultLulu()
        
        if (Territory.getLulus().__len__() == 0):
            break

        
        et = time.time()
        elapsed = et - st
        
        print("temps generation " + str(generation) + ": " + str(elapsed))
    
    simf = time.time()
    sime = simf - sims
        
    print("temps simulation: " + str(sime))

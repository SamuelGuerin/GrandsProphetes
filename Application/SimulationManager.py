import Models.Territory as Territory


def __run__(sizeX, sizeY, foodCount, lulusCount, speed, sense, size, energy, nbGeneration):
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount,
                        speed, sense, energy, 0, size)

    for generation in range(nbGeneration):

        Territory.moveAll()
        Territory.dayResultLulu()

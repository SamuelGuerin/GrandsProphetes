import Models.Territory as Territory

def __run__(sizeX, sizeY, foodCount, lulusCount, speed, sense, size, energy):
    global __energy
    __energy = energy
    
    Territory.createMap(sizeX, sizeY, foodCount, lulusCount, speed, sense, energy, 0, size)
    
    Territory.moveAll()
    
    Territory.dayResultLulu()
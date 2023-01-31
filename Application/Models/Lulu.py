import Models.Territory as Territory
from Models.Position import Position

class Lulu:
    def __init__(self,position,speed = 0,sense = 0,size = 0,energy = 0,foodAmount = 0,lastPos = None, isDone = False):
        self.position = position
        self.speed = speed
        self.sense = sense
        self.size = size
        self.energy = energy
        self.foodAmount = foodAmount
        self.lastPos = lastPos
        self.isDone = isDone

    def __repr__(self) -> str:
        return "Lulu"

    def resetPosition(self):
        sizeX = Territory.getSizeX()
        sizeY = Territory.getSizeY()
        halfSizeX = sizeX / 2
        halfSizeY = sizeY / 2
        if(self.position.x <= halfSizeX and self.position.y <= halfSizeY): # vérifier si centre de la map?
            if(self.position.x > self.position.y):
                Territory.moveLulu(self.position, Position(self.position.x, self.position.y - 1)) # va vers y=min
            else:
                Territory.moveLulu(self.position, Position(self.position.x - 1, self.position.y)) # va vers x=min
        elif(self.position.x <= halfSizeX and self.position.y > halfSizeY):
            if((sizeY - self.position.y) < self.position.x):
                Territory.moveLulu(self.position, Position(self.position.x, self.position.y + 1)) # va vers y=max
            else:
                Territory.moveLulu(self.position, Position(self.position.x - 1, self.position.y)) # vs vers x=min
        elif(self.position.x > halfSizeX and self.position.y <= halfSizeY):
            if((sizeX - self.position.x) < self.position.y):
                Territory.moveLulu(self.position, Position(self.position.x + 1, self.position.y)) # va vers x=max
            else:
                Territory.moveLulu(self.position, Position(self.position.x, self.position.y - 1)) # va vers y=min
        elif(self.position.x > halfSizeX and self.position.y > halfSizeY):
            if(self.position.x > self.position.y):
                Territory.moveLulu(self.position, Position(self.position.x + 1, self.position.y)) # va vers x=max
            else:
                Territory.moveLulu(self.position, Position(self.position.x, self.position.y + 1)) # vs vers y=max
            





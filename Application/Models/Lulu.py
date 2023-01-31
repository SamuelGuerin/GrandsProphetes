import Models.Territory as Territory
import random
from Models.Position import Position
from Models.Food import Food

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


    #1  Analyser les items autour avec le sense et les garder en mémoire (dictionnaire)
                #a Lulu?
                    # - Ennemi ou Proie? Sense, direction (random si pas de bouffe/ennemi) si oui --> bouge direction opposé -> inverser les x,y (3x,2y devient -3x, -2y)
                #b Bouffe?   
            #2  foodAmount (est-ce qu'il en a 2)
            #4. Quantité Énergie

    # Return true si le Lulu peut encore bouger (énergie > 0) sinon false
    def move(self) -> bool:
        map = Territory.getMap()
        foodInRange = []
        lulusInRange = []
        self.__getItems(foodInRange, lulusInRange)
        targetPosition = None

        if(len(lulusInRange) > 0):
            if(len(lulusInRange) == 1):
                targetPosition = lulusInRange[0].position
            else:
                targetPosition = self.getClosestEnemy(lulusInRange)
        if (targetPosition == None and len(foodInRange) > 0):
            if(len(foodInRange) == 1):
                targetPosition = foodInRange[0].position
            else:
                targetPosition = self.getClosestFood(foodInRange)
        if(targetPosition == None and len(lulusInRange) > 0):
            if(len(lulusInRange) == 1):
                targetPosition = lulusInRange[0].position
            else:
                targetPosition = self.getClosestPrey(lulusInRange)
        if(targetPosition == None):
            targetPosition = Position(random.randint(0, Territory.getSizeX()), random.randint(0, Territory.getSizeY()))

        i = 1
        
        
    def getClosestEnemy(self, items): # Retourne la position de l'ennemi le plus proche
        position = None
        closestDistance = 0
        sizeToBeEnemy = self.size * Territory.EATING_RATIO
        for i in items:
            if(i.size > sizeToBeEnemy):
                currentDistance = abs(self.position.x - i.position.x) + abs(self.position.y - i.position.y)
                if(position == None):
                    position = i.position
                    distance = currentDistance
                elif(currentDistance < closestDistance):
                    position = i.position
                    closestDistance = currentDistance
            return Position(i.position.x, i.position.y)
        return None
    
    def getClosestPrey(self, items): # Retourne la position de la proie la plus proche
        position = None
        closestDistance = 0
        sizeToBePrey = self.size / Territory.EATING_RATIO
        for i in items:
            if(i.size < sizeToBePrey):
                currentDistance = abs(self.position.x - i.position.x) + abs(self.position.y - i.position.y)
                if(position == None):
                    position = i.position
                    distance = currentDistance
                elif(currentDistance < closestDistance):
                    position = i.position
                    closestDistance = currentDistance
            return Position(i.position.x, i.position.y)
        return None

    def getClosestFood(self, items): # Retourne la position de la nourriture le plus proche
        position = None
        closestDistance = 0
        for i in items:
            currentDistance = abs(self.position.x - i.position.x) + abs(self.position.y - i.position.y)
            if(position == None):
                position = i.position
                distance = currentDistance
            elif(currentDistance < closestDistance):
                position = i.position
                closestDistance = currentDistance
            return Position(i.position.x, i.position.y)
        return None
                
    def __getItems(self, foodInRange, lulusInRange):
        map = Territory.getMap()
        minX = self.position.x - self.sense
        maxX = self.position.x + self.sense
        minY = self.position.y - self.sense
        maxY = self.position.y + self.sense
        
        for x in range(minX, maxX):
            for y in range(minY, maxY):
                if not (self.position.x == x and self.position.y == y):
                    item = Territory.getItem(x,y)
                    if(type(item) == Food):
                        foodInRange.append(item)
                    elif(type(item) == Lulu):
                        lulusInRange.append(item)


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
            





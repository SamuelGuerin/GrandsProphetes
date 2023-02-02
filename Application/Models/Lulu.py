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
        return ("Lulu" + str(self.position))


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
        targetFound = False

        if(len(lulusInRange) > 0):
            targetPosition, targetFound = self.getClosestEnemy(lulusInRange)
        if (not targetFound and len(foodInRange) > 0):
            if(len(foodInRange) == 1):
                targetPosition = foodInRange[0].position
                targetFound = True
            else:
                targetPosition, targetFound = self.getClosestFood(foodInRange)
        if(not targetFound and len(lulusInRange) > 0):
            targetPosition, targetFound = self.getClosestPrey(lulusInRange)
        if(not targetFound):
            targetPosition = Position(random.randint(1, Territory.getSizeX()), random.randint(1, Territory.getSizeY()))
        i = 1
        
    def getClosestEnemy(self, items): # Retourne la position de l'ennemi le plus proche
        position = None
        closestDistance = None
        sizeToBeEnemy = self.size * Territory.EATING_RATIO
        enemyFound = False
        for i in items:
            if(i.size > sizeToBeEnemy):
                currentDistance = max(abs(self.position.x - i.position.x), abs(self.position.y - i.position.y))
                if(not enemyFound):
                    enemyFound = True
                    position = i.position
                    closestDistance = currentDistance
                elif(currentDistance < closestDistance):
                    position = i.position
                    closestDistance = currentDistance
        if (enemyFound):
            # Retourner comme target l'opposé de l'enemi
            return Position(self.position.x + (self.position.x - position.x), self.position.y + (self.position.y - position.y)), True
        else:
            return None
    
    def getClosestPrey(self, items): # Retourne la position de la proie la plus proche
        position = None
        closestDistance = None
        sizeToBePrey = self.size / Territory.EATING_RATIO
        preyFound = False
        for i in items:
            if(i.size < sizeToBePrey):
                currentDistance = max(abs(self.position.x - i.position.x), abs(self.position.y - i.position.y))
                if(not preyFound):
                    preyFound = True
                    position = i.position
                    closestDistance = currentDistance
                elif(currentDistance < closestDistance):
                    position = i.position
                    closestDistance = currentDistance
        return position, preyFound

    def getClosestFood(self, items): # Retourne la position de la nourriture la plus proche
        position = None
        closestDistance = None
        foodFound = False
        for i in items:
            currentDistance = max(abs(self.position.x - i.position.x), abs(self.position.y - i.position.y))
            if(not foodFound):
                foodFound = True
                position = i.position
                closestDistance = currentDistance
            elif(currentDistance < closestDistance):
                position = i.position
                closestDistance = currentDistance
        return position, foodFound
                
    def __getItems(self, foodInRange, lulusInRange):
        map = Territory.getMap()
        minX = self.position.x - self.sense
        maxX = self.position.x + self.sense
        minY = self.position.y - self.sense
        maxY = self.position.y + self.sense
        
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if not (self.position.x == x and self.position.y == y):
                    item = Territory.getItem(x,y)
                    if(type(item) == Food):
                        foodInRange.append(item)
                    elif(type(item) == Lulu):
                        lulusInRange.append(item)

    # Si la lulu a ses deux nourritures, elle se dirige vers le côté
    def moveToInitialPosition(self):
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
    
    # Téléporte la lulu sur le côté au début d'une round
    def resetPosition(self):
        i = 3





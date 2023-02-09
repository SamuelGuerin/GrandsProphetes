import Models.Territory as Territory
import random
from Models.Position import Position
from Models.Food import Food

class Lulu:
    def __init__(self, position, speed = 0,sense = 0,size = 0,energy = 0,foodAmount = 0,lastPos = None, isDone = False):
        self.position = position
        self.speed = speed
        self.sense = sense
        self.size = size
        self.energy = energy
        self.foodAmount = foodAmount
        self.lastPos = lastPos
        self.isDone = isDone
        self.randomTargetPosition = self.newRandomPosition()

    def __repr__(self) -> str:
        return ("Lulu")

    def move(self) -> bool:
        foodInRange = []
        lulusInRange = []
        energyCost = ((self.size/100) ** 3) * (self.speed ** 2) + self.sense;
        speedLeft = self.speed

        while(speedLeft > 0 and self.energy >= energyCost):
            foodInRange.clear()
            lulusInRange.clear()
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
                if(self.isCloseToTargetPosition()):
                    targetPosition = self.newRandomPosition()
                    self.randomTargetPosition = targetPosition
                else:
                    targetPosition = self.randomTargetPosition
                self.goToTargetPosition(targetPosition)
            else:
                self.goToTargetPosition(targetPosition)
            self.energy -= energyCost;
            speedLeft -= 1;

        if(self.energy < energyCost):
            self.isDone = True
            return False
        else:
            return True

    # move est callé pour un lulu une fois / vitesse écoulée
    # 1- Déterminer un point dans le sense (si il y en a un)
    # 2- Aller au point directement jusqu'à écouler sa speed
    # 3- S'il reste de la speed après avoir atteint son point, il va refaire le scan
    # 4- S'il ne détecte rien, il va vers 1 point random et refait son scan à chaque point

    def isCloseToTargetPosition(self) -> bool:
        currentDistance = max(abs(self.position.x - self.randomTargetPosition.x), abs(self.position.y - self.randomTargetPosition.y))
        randomSense = ((Territory.getSizeX() + Territory.getSizeY())/ 2 / 20)
        randomSense = 1 if randomSense < 1 else randomSense
        return True if currentDistance <= randomSense else False
        

    def goToTargetPosition(self, targetPosition) -> bool:
        xDiff = targetPosition.x - self.position.x
        yDiff = targetPosition.y - self.position.y
        xMove = self.getMoveFromDiff(xDiff)
        yMove = self.getMoveFromDiff(yDiff)

        nextPos = Position(self.position.x + xMove, self.position.y + yMove)
        # Tenter le chemin idéal, sinon tenter les 2 autres sur le côté
        if(not Territory.tryMove(self.position, nextPos)):
            if(xMove == 0): # ligne verticale
                if(not Territory.tryMove(self.position, Position(nextPos.x - 1, nextPos.y))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x + 1, nextPos.y))):
                        # random
                        self.goToTargetPosition(self.newRandomPosition())
            elif(yMove == 0): # ligne horizontale
                if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y - 1))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y + 1))):
                        # random
                        self.goToTargetPosition(self.newRandomPosition())
            else: # diagonnale
                if(not Territory.tryMove(self.position, Position(nextPos.x - xMove, nextPos.y))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y - yMove))):
                        # random
                        self.goToTargetPosition(self.newRandomPosition())
    
    def newRandomPosition(self) -> Position:
        # 1 - point random sur la map (2 à maxX-1), 2 à maxY-1
        randomPosition = Position((random.randint(2, Territory.getSizeX())), random.randint(2, Territory.getSizeY()))
        return randomPosition
        # return le point

    def getMoveFromDiff(self, diff):
        if diff > 0:
            return 1
        elif diff < 0:
            return -1
        return 0

    def getClosestEnemy(self, items): # Retourne la position de l'ennemi le plus proche
        position = None
        closestDistance = None
        sizeToBeEnemy = self.size * Territory.EATING_RATIO
        enemyFound = False
        for i in items:
            if(i.size > sizeToBeEnemy and not i.isDone):
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
            return None, False
    
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
    
    # Téléporte la lulu sur le côté au début d'une round
    def resetPosition(self):
        #self.moveToInitialPosition(True)
        sizeX = Territory.getSizeX()
        sizeY = Territory.getSizeY()
        minSizeXY = 1
        halfSizeX = sizeX / 2
        halfSizeY = sizeY / 2

        item = self
        searchRangeX = 0
        searchRangeY = 0

        if(self.position.x <= halfSizeX and self.position.y <= halfSizeY): # vérifier si centre de la map?
            if(self.position.x > self.position.y):
                while(type(item) == Lulu and (self.position.x + searchRangeX) <= sizeX):
                    item = Territory.getItem(self.position.x + searchRangeX, minSizeXY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                searchRangeX = 0
                while(type(item) == Lulu and (self.position.x - searchRangeX) <= minSizeXY):
                    item = Territory.getItem(self.position.x - searchRangeX, minSizeXY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                Territory.moveLulu(self.position, Position(self.position.x + searchRangeX, minSizeXY)) # va vers y=min
            else:
                while(type(item) == Lulu and (self.position.y + searchRangeY) <= sizeY):
                    item = Territory.getItem(minSizeXY, self.position.y + searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                searchRangeY = 0
                while(type(item) == Lulu and (self.position.y - searchRangeY) >= minSizeXY):
                    item = Territory.getItem(minSizeXY, self.position.y - searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                Territory.moveLulu(self.position, Position(minSizeXY, self.position.y + searchRangeY)) # va vers x=min
        elif(self.position.x <= halfSizeX and self.position.y > halfSizeY):
            if((sizeY - self.position.y) < self.position.x):
                while(type(item) == Lulu and (self.position.x + searchRangeX) <= sizeX):
                    item = Territory.getItem(self.position.x + searchRangeX, sizeY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                searchRangeX = 0
                while(type(item) == Lulu and (self.position.x - searchRangeX) >= minSizeXY):
                    item = Territory.getItem(self.position.x - searchRangeX, sizeY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                Territory.moveLulu(self.position, Position(self.position.x, sizeY)) # va vers y=max
            else:
                while(type(item) == Lulu and (self.position.y + searchRangeY) <= sizeY):
                    item = Territory.getItem(minSizeXY, self.position.y + searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                searchRangeY = 0
                while(type(item) == Lulu and (self.position.y - searchRangeY) >= minSizeXY):
                    item = Territory.getItem(minSizeXY, self.position.y - searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                Territory.moveLulu(self.position, Position(minSizeXY, self.position.y)) # va vers x=min
        elif(self.position.x > halfSizeX and self.position.y <= halfSizeY):
            if((sizeX - self.position.x) < self.position.y):
                while(type(item) == Lulu and (self.position.y + searchRangeY) <= sizeY):
                    item = Territory.getItem(sizeX, self.position.y + searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                searchRangeY = 0
                while(type(item) == Lulu and (self.position.y - searchRangeY) >= minSizeXY):
                    item = Territory.getItem(sizeX, self.position.y - searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                Territory.moveLulu(self.position, Position(sizeX, self.position.y)) # va vers x=max
            else:
                while(type(item) == Lulu and (self.position.x + searchRangeX) <= sizeX):
                    item = Territory.getItem(self.position.x + searchRangeX, minSizeXY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                searchRangeX = 0
                while(type(item) == Lulu and (self.position.x - searchRangeX) <= minSizeXY):
                    item = Territory.getItem(self.position.x - searchRangeX, minSizeXY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                Territory.moveLulu(self.position, Position(self.position.x, minSizeXY)) # va vers y=min
        elif(self.position.x > halfSizeX and self.position.y > halfSizeY):
            if(self.position.x > self.position.y):
                while(type(item) == Lulu and (self.position.y + searchRangeY) <= sizeY):
                    item = Territory.getItem(sizeX, self.position.y + searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                searchRangeY = 0
                while(type(item) == Lulu and (self.position.y - searchRangeY) >= minSizeXY):
                    item = Territory.getItem(sizeX, self.position.y - searchRangeY)
                    if(type(item) == Lulu):
                        searchRangeY += 1
                Territory.moveLulu(self.position, Position(sizeX, self.position.y)) # va vers x=max
            else:
                while(type(item) == Lulu and (self.position.x + searchRangeX) <= sizeX):
                    item = Territory.getItem(self.position.x + searchRangeX, sizeY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                searchRangeX = 0
                while(type(item) == Lulu and (self.position.x - searchRangeX) >= minSizeXY):
                    item = Territory.getItem(self.position.x - searchRangeX, sizeY)
                    if(type(item) == Lulu):
                        searchRangeX += 1
                Territory.moveLulu(self.position, Position(self.position.x, sizeY)) # va vers y=max
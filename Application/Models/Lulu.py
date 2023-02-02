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
        
        while(self.foodAmount < 2 and self.energy > 0):
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
                self.randomMove()
            else:
                self.goToTargetPosition(targetPosition)

    # move est callé pour un lulu une fois / vitesse écoulée
    # 1- Déterminer un point dans le sense (si il y en a un)
    # 2- Aller au point directement jusqu'à écouler sa speed
    # 3- S'il reste de la speed après avoir atteint son point, il va refaire le scan
    # 4- S'il ne détecte rien, il va vers 1 point random et refait son scan à chaque point
        
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
                        self.randomMove()
            elif(yMove == 0): # ligne horizontale
                if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y - 1))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y + 1))):
                        # random
                        self.randomMove()
            else: # diagonnale
                if(not Territory.tryMove(self.position, Position(nextPos.x - xMove, nextPos.y))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y - yMove))):
                        # random
                        self.randomMove()
                
        # if (Territory.getItem(nextPos.x, nextPos.y) == None):
        #     return Territory.tryMove(self, nextPos)
        # # tenter une autre path pour aller à l'objectif
        # elif(Territory.getItem(nextPos.x, nextPos.y) == None):

        # elif():
        # return False

    # dernier recours d'un lulu : fait un move random
    def randomMove(self):
        map = Territory.getMap()
        minX = self.position.x - 1
        maxX = self.position.x + 1
        minY = self.position.y - 1
        maxY = self.position.y + 1
        
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if not (self.position.x == x and self.position.y == y):
                    item = Territory.getItem(x,y)
                    if(item == None):
                        Territory.moveLulu(self.position, Position(x, y))

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

    # ToDo : Changer le 1 pour la speed du lulu
    # ToDo : Si peut pas bouger, va qqpart random
    # Si la lulu a ses deux nourritures, elle se dirige vers le côté
    def moveToInitialPosition(self):
        sizeX = Territory.getSizeX()
        sizeY = Territory.getSizeY()
        halfSizeX = sizeX / 2
        halfSizeY = sizeY / 2
        if(self.position.x <= halfSizeX and self.position.y <= halfSizeY): # vérifier si centre de la map?
            if(self.position.x > self.position.y):
                Territory.tryMove(self.position, Position(self.position.x, self.position.y - 1)) # va vers y=min
            else:
                Territory.tryMove(self.position, Position(self.position.x - 1, self.position.y)) # va vers x=min
        elif(self.position.x <= halfSizeX and self.position.y > halfSizeY):
            if((sizeY - self.position.y) < self.position.x):
                Territory.tryMove(self.position, Position(self.position.x, self.position.y + 1)) # va vers y=max
            else:
                Territory.tryMove(self.position, Position(self.position.x - 1, self.position.y)) # vs vers x=min
        elif(self.position.x > halfSizeX and self.position.y <= halfSizeY):
            if((sizeX - self.position.x) < self.position.y):
                Territory.tryMove(self.position, Position(self.position.x + 1, self.position.y)) # va vers x=max
            else:
                Territory.tryMove(self.position, Position(self.position.x, self.position.y - 1)) # va vers y=min
        elif(self.position.x > halfSizeX and self.position.y > halfSizeY):
            if(self.position.x > self.position.y):
                Territory.tryMove(self.position, Position(self.position.x + 1, self.position.y)) # va vers x=max
            else:
                Territory.tryMove(self.position, Position(self.position.x, self.position.y + 1)) # vs vers y=max
    
    # Téléporte la lulu sur le côté au début d'une round
    def resetPosition(self):
        i = 3





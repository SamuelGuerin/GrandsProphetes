import Models.Territory as Territory
import random
from Models.Position import Position
from Models.Food import Food
from Models.Move import Move

class Lulu:
    """Classe contenant toutes les informations propre à une :class:`Lulu`

        :param position: :class:`Position` sur l'axe des X et Y de la :class:`Lulu` dans la carte (map)
        :type position: :class:`Position`
        :param speed: Vitesse de la :class:`Lulu`, relatif au nombre de cases que la :class:`Lulu` va parcourir pendant son tour 
        :type speed: int
        :param sense: Vision de la :class:`Lulu`, définit la portée en nombre de cases dans laquelle la :class:`Lulu` peut apercevoir d'autres :class:`Lulu` ou de la nourriture (:class:`Food`)
        :type sense: int
        :param size: Taille de la :class:`Lulu`, définit sa force pour calculer si la :class:`Lulu` peut manger une :class:`Lulu` ou se faire manger par une autre :class:`Lulu`
        :type size: int
        :param energy: Énergie de la :class:`Lulu`, permet à la :class:`Lulu` de se déplacer tant qu'elle a assez d'énergie, l'énergie se dépense à chaque mouvement occasionné par la :class:`Lulu`
        :type energy: int
        :param foodAmount: Nombre de nourriture (:class:`Food`) consommée par la :class:`Lulu` 
        :type foodAmount: int
        :param isDone: Détermine si la :class:`Lulu` est inactive et immobile, ce paramètre est égal à "True" quand la :class:`Lulu` n'a plus assez d'énergie pour se déplacer
        :type isDone: bool
    """
    def __init__(self, position, speed = 0,sense = 0,size = 0,energy = 0,foodAmount = 0, isDone = False):
        
        self.position = position
        self.speed = speed
        self.sense = sense
        self.size = size
        self.energy = energy
        self.foodAmount = foodAmount
        self.isDone = isDone
        self.started = False
        self.newTurn = True
        self.isNewBorn = True
        self.randomTargetPosition = self.newRandomPosition()
        self.foodInRange = []
        self.lulusInRange = []
        self.lastPosition = position

    def __repr__(self) -> str:
        return ("Lulu")

    def move(self) -> bool:
        """Algorithme qui détermine comment la :class:`Lulu` se déplacera dépendemment de ce qui est présent dans sa vision

        :return: Retourne un booléen déterminant s'il reste assez d'énergie à la :class:`Lulu` pour effectuer un mouvement
        :rtype: bool
        """
        energyCost = ((self.size/100) ** 3) * (self.speed ** 2) + self.sense
        speedLeft = self.speed
        startPt = self.position
        self.newTurn = True

        while(speedLeft > 0 and self.energy >= energyCost):
            self.getItems()
            targetPosition = None
            targetFound = False

            if(len(self.lulusInRange) > 0):
                targetPosition, targetFound = self.getClosestEnemy(self.lulusInRange)
            if (not targetFound and len(self.foodInRange) > 0):
                if(len(self.foodInRange) == 1):
                    targetPosition = self.foodInRange[0].position
                    targetFound = True
                else:
                    targetPosition, targetFound = self.getClosestFood(self.foodInRange)
            if(not targetFound and len(self.lulusInRange) > 0):
                targetPosition, targetFound = self.getClosestPrey(self.lulusInRange)
            if(not targetFound):
                if(self.isCloseToTargetPosition()):
                    targetPosition = self.newRandomPosition()
                    self.randomTargetPosition = targetPosition
                else:
                    targetPosition = self.randomTargetPosition
                self.lastPosition = self.position
                self.goToTargetPosition(targetPosition)
            else:
                self.lastPosition = self.position
                self.goToTargetPosition(targetPosition)
            self.energy -= energyCost
            speedLeft -= 1
        
        endPt = self.position
        Territory.addMove(Move(self.speed, self.sense, self.size, startPt, endPt))

        self.started = True
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
        """Vérifie si la :class:`Lulu` est près de la position ciblée, la distance déterminant si la :class:`Lulu` est près ou non est équivalent à une distance de 5% du :class:`Territory` total

        :return: Retourne un booléen déterminant si la :class:`Lulu` est près ou non de la position ciblée 
        :rtype: bool
        """
        currentDistance = max(abs(self.position.x - self.randomTargetPosition.x), abs(self.position.y - self.randomTargetPosition.y))
        randomSense = ((Territory.getSizeX() + Territory.getSizeY())/ 2 / 20)
        randomSense = 1 if randomSense < 1 else randomSense
        return True if currentDistance <= randomSense else False
        

    def goToTargetPosition(self, targetPosition):
        """Déplace la :class:`Lulu` en direction de la position ciblée 

        :param targetPosition: :class:`Position` ciblée par la :class:`Lulu`
        :type targetPosition: :class:`Position
        """
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
                        # ne bouge pas et trouve nouvelle cible random
                        self.randomTargetPosition = self.newRandomPosition()
            elif(yMove == 0): # ligne horizontale
                if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y - 1))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y + 1))):
                        # ne bouge pas et trouve nouvelle cible random
                        self.randomTargetPosition = self.newRandomPosition()
            else: # diagonnale
                if(not Territory.tryMove(self.position, Position(nextPos.x - xMove, nextPos.y))):
                    if(not Territory.tryMove(self.position, Position(nextPos.x, nextPos.y - yMove))):
                        # ne bouge pas et trouve nouvelle cible random
                        self.randomTargetPosition = self.newRandomPosition()
    
    def newRandomPosition(self) -> Position:
        """Détermine une nouvelle :class:`Position` aléatoire dans la carte (map) qui deviendra la nouvelle :class:`Position` ciblée de la :class:`Lulu`

        :return: Retourne la nouvelle :class:`Position` aléatoire
        :rtype: :class:`Position`
        """
        # 1 - point random sur la map (2 à maxX-1), 2 à maxY-1
        randomPosition = Position((random.randint(2, Territory.getSizeX())), random.randint(2, Territory.getSizeY()))
        return randomPosition
        # return le point

    def getMoveFromDiff(self, diff):
        """Détermine dans quelle direction la :class:`Lulu` doit se déplacer sur un certain axe de la carte (map) 

        :param diff: Écart entre deux coordonnées selon un axe
        :type diff: int
        :return: Retourne un entier positif ou négatif déterminant dans quelle direction la :class:`Lulu` doit se déplacer
        :rtype: int
        """
        if diff > 0:
            return 1
        elif diff < 0:
            return -1
        return 0

    def getClosestEnemy(self, items):
        """Retourne la position de la :class:`Lulu` au moins 1.2 fois plus grande la plus proche dans la liste fournie

        :param items: Toutes les :class:`Lulu` à vérifier
        :type items: list
        :return: La :class:`Position` de la :class:`Lulu` la plus proche
        :rtype: :class:`Position`
        """
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
    
    def getClosestPrey(self, items):
        """Retourne la position de la :class:`Lulu` au moins 1.2 fois plus petite la plus proche dans la liste fournie

        :param items: Toutes les :class:`Lulu` à vérifier
        :type items: list
        :return: La :class:`Position` de la :class:`Lulu` la plus proche
        :rtype: :class:`Position`
        """
        position = None
        closestDistance = None
        sizeToBePrey = self.size / Territory.EATING_RATIO
        preyFound = False
        for i in items:
            if(i.size < sizeToBePrey and i.started):
                currentDistance = max(abs(self.position.x - i.position.x), abs(self.position.y - i.position.y))
                if(not preyFound):
                    preyFound = True
                    position = i.position
                    closestDistance = currentDistance
                elif(currentDistance < closestDistance):
                    position = i.position
                    closestDistance = currentDistance
        return position, preyFound

    def getClosestFood(self, items):
        """Retourne la position de la :class:`Food` le plus proche dans la liste fournie

        :param items: Tous les :class:`Food` à vérifier
        :type items: list
        :return: La :class:`Position` de la :class:`Food` la plus proche
        :rtype: :class:`Position`
        """
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
                
    def getItems(self):
        """Recherche les :class:`Food` et les :class:`Lulu` qui sont dans sa vision (sense)

        :param foodInRange: contient toutes les nourritures dans la vision (sense) de la :class:`Lulu`
        :type foodInRange: list
        :param lulusInRange: contient toutes les nourritures dans la vision (sense) de la :class:`Lulu`
        :type lulusInRange: list
        """

        map = Territory.getMap()
        # 1 - Supprimer les anciennes cases
        #   1 - trouver les anciennes cases (lastPos et sense)
        #   2 - Itération dans les listes inRange -> si Pos == anciennes cases -> del
        #   3 - Supprimer les items ou of range
        # 2- Ajouter les nouvelles
        #   1 - trouver les nouvelles cases (lastPos et sense)
        #   2 - Itération dans les listes inRange -> si Pos == nouvelles cases -> del
        #   3 - Ajouter les items out of range

        if not self.newTurn: 
            oldVisionX = self.sense
            oldVisionY = self.sense

            # diagonnale
            if (self.lastPosition.x != self.position.x and self.lastPosition.y != self.position.y):
                if (self.position.x > self.lastPosition.x):
                    oldVisionX *= -1

                if (self.position.y > self.lastPosition.y):
                    oldVisionY *= -1

                # check pour delete
                xToDelete = self.lastPosition.x + oldVisionX
                yToDelete = self.lastPosition.y + oldVisionY
                foodToDelete = [food for food in self.foodInRange if food.position.x == xToDelete or food.position.y == yToDelete]
                lulusToDelete = [lulu for lulu in self.lulusInRange if lulu.position.x == xToDelete or lulu.position.y == yToDelete]
                # foodToDelete = filter(lambda f: f.position.x == xToDelete or f.position.y == yToDelete, self.foodInRange)
                for food in foodToDelete[:]:
                    self.foodInRange.remove(food)

                for lulu in lulusToDelete[:]:
                    self.lulusInRange.remove(lulu)

                # check pour add
                xToAdd = self.position.x - oldVisionX
                yToAdd = self.position.y - oldVisionY

                for x in range(self.position.x - self.sense, self.position.x + self.sense + 1):
                    item = Territory.getItem(x,yToAdd)
                    if(type(item) == Food):
                        self.foodInRange.append(item)
                    elif(type(item) == Lulu):
                        self.lulusInRange.append(item)

                for y in range(self.position.y - self.sense, self.position.y + self.sense + 1):
                    item = Territory.getItem(xToAdd,y)
                    if(type(item) == Food):
                        self.foodInRange.append(item)
                    elif(type(item) == Lulu):
                        self.lulusInRange.append(item)

            # linéaire
            else:
                if (self.lastPosition.y != self.position.y):
                    if (self.position.y > self.lastPosition.y):
                        oldVisionY *= -1

                    # check
                    yToDelete = self.lastPosition.y + oldVisionY
                    foodToDelete = [food for food in self.foodInRange if food.position.y == yToDelete]
                    lulusToDelete = [lulu for lulu in self.lulusInRange if lulu.position.y == yToDelete]
                    for food in foodToDelete[:]:
                        self.foodInRange.remove(food)

                    for lulu in lulusToDelete[:]:
                        self.lulusInRange.remove(lulu)
                
                    # check pour add
                    yToAdd = self.position.y - oldVisionY

                    for x in range(self.position.x - self.sense, self.position.x + self.sense + 1):
                        item = Territory.getItem(x,yToAdd)
                        if(type(item) == Food):
                            self.foodInRange.append(item)
                        elif(type(item) == Lulu):
                            self.lulusInRange.append(item)

                elif (self.lastPosition.x != self.position.x):
                    if (self.position.x > self.lastPosition.x):
                        oldVisionX *= -1
                    #check
                    xToDelete = self.lastPosition.x + oldVisionX
                    foodToDelete = [food for food in self.foodInRange if food.position.x == xToDelete]
                    lulusToDelete = [lulu for lulu in self.lulusInRange if lulu.position.x == xToDelete]
                    for food in foodToDelete[:]:
                        self.foodInRange.remove(food)

                    for lulu in lulusToDelete[:]:
                        self.lulusInRange.remove(lulu)

                    # check pour add
                    xToAdd = self.position.x - oldVisionX

                    for y in range(self.position.y - self.sense, self.position.y + self.sense + 1):
                        item = Territory.getItem(xToAdd,y)
                        if(type(item) == Food):
                            self.foodInRange.append(item)
                        elif(type(item) == Lulu):
                            self.lulusInRange.append(item)

        # Remplir la liste 1 x au complet si nouveau tour
        else:
            self.newTurn = False
            self.foodInRange = []
            self.lulusInRange = []
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
                            self.foodInRange.append(item)
                        elif(type(item) == Lulu):
                            self.lulusInRange.append(item)
    
    # Téléporte la lulu sur le côté au début d'une round
    def resetPosition(self):
        """Téléporte une :class:`Lulu` sur le côté de la carte (map) à la fin d'une génération, pour la préparer à la reproduction
        """
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
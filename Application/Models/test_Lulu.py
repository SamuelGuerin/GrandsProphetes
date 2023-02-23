import unittest
import numpy as np
import time
import random

import sys
import pathlib

#workingDir = pathlib.Path().resolve()
#sys.path.append('../Application/')
#sys.path.insert(0, str(workingDir) + '\Application\\')

import Territory
from Lulu import Lulu 
from Position import Position
from Food import Food

distanceCloseToTarget = 1

X = 100
Y = 100
numberOfFood = 0
numberOfLulus = 0
speed = 1
sense = 1
energy = 0
size = 100
mutateChance = 0.3

Territory.createMap(X,Y,numberOfFood,numberOfLulus,speed,sense,energy,size,mutateChance,mutateChance,mutateChance,mutateChance) # 25x25, 10 Food, 10 Lulus, etc...
#Territory.createMap(100,100,0,0,1,1,0,100,0.3,0.3,0.3,0.3)

foodInRange = []
lulusInRange = []

class TestMove(unittest.TestCase):
    # def test_move_priority_enemy(self):
    #     lulu1 = Lulu(Position(2,2), 1, 1, 100, 3, 0, False) # Juste à côté de lulu2 (qui est un ennemi)
    #     lulu2 = Lulu(Position(1,1), 1, 2, 120, 4, 0, False) # Juste à côté de lulu1 (qui est une proie)
    #     #food1 = Food(Position(1,2))
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(lulu2.position, lulu2)
    #     #Territory.__map[food1.position] = food1
    #     Territory.plulus.append(lulu1)
    #     Territory.plulus.append(lulu2)
    #     lulu1.move()
    #     self.assertEqual(lulu1.position, Position(3,3))

    # def test_move_priority_food(self):
    #     lulu1 = Lulu(Position(2,6), 1, 1, 100, 3, 0, False) # Juste à côté de lulu2 (ennemi)
    #     lulu2 = Lulu(Position(1,5), 1, 2, 120, 4, 0, False) # Juste à côté de lulu1 (proie)
    #     food1 = Food(Position(1,6))
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(lulu2.position, lulu2)
    #     Territory.addItem(food1.position, food1)
    #     Territory.plulus.append(lulu1)
    #     Territory.plulus.append(lulu2)

    #     lulu2.move()
    #     self.assertEqual(lulu1.position, Position(1,2))

    # def test_move_priority_prey(self):
    #     lulu1 = Lulu(Position(1,11), 1, 1, 100, 3, 0, False) # Juste à côté de lulu2 (qui est un ennemi)
    #     lulu2 = Lulu(Position(1,10), 1, 2, 120, 4, 0, False) # Juste à côté de lulu1 (qui est une proie)
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(lulu2.position, lulu2)
    #     Territory.plulus.append(lulu1)
    #     Territory.plulus.append(lulu2)
        
    #     lulu2.move()
    #     self.assertEqual(lulu2.position, Position(1,11))

    # def test_move_energy_cost(self):
    #     lulu1 = Lulu(Position(1,20), 1, 1, 100, 3, 0, False)
    #     food1 = Food(Position(2,20))
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(food1.position, food1)
    #     Territory.plulus.append(lulu1)
    #     energyCost = ((lulu1.size/100) ** 3) * (lulu1.speed ** 2) + lulu1.sense

    #     self.assertTrue(lulu1.move()) # À vérifier le comportement de move, s'il faut seulement faire un assertFalse
    #     self.assertLess(lulu1.energy, energyCost)
    #     #self.assertFalse(lulu1.move())

    # def test_move_is_done(self): 
    # # Même test que celui du energyCost sauf qu'on vérifie si la lulu.isDone = False avant de bouger et si lulu.isDone = True après avoir bougé
    #     lulu1 = Lulu(Position(1,30), 1, 1, 100, 3, 0, False)
    #     food1 = Food(Position(2,30))
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(food1.position, food1)
    #     Territory.plulus.append(lulu1)
    #     energyCost = ((lulu1.size/100) ** 3) * (lulu1.speed ** 2) + lulu1.sense;

    #     self.assertFalse(lulu1.isDone)
    #     self.assertTrue(lulu1.move()) # À vérifier le comportement de move, s'il faut seulement faire un assertFalse
    #     self.assertLess(lulu1.energy, energyCost)
    #     self.assertTrue(lulu1.isDone)
        #self.assertFalse(lulu1.move())

    def test_getMovefromDiff(self):
        # Teste si on retourne un entier positif ou négatif déterminant dans quelle direction la Lulu doit se déplacer sur les axes X et Y
        lulu1 = Lulu(Position(1,40), 1, 1, 100, 3, 0, False)
        self.assertEqual(lulu1.getMoveFromDiff(5), 1)
        self.assertEqual(lulu1.getMoveFromDiff(-5), -1)
        self.assertEqual(lulu1.getMoveFromDiff(0), 0)

#class TestPriorityMovement(unittest.TestCase):
    # def test_get_closest_enemy(self):
    #     luluPrey1 = Lulu(Position(12,30), 1, 1, 100, 3, 0, False) # La proie
    #     luluEnemy1 = Lulu(Position(10,30), 1, 2, 120, 4, 0, False) # ennemi 1 (plus près)
    #     luluEnemy2 = Lulu(Position(18,30), 1, 2, 120, 4, 0, False) # ennemi 2 (plus loin)
    #     Territory.addItem(luluPrey1.position, luluPrey1)
    #     Territory.addItem(luluEnemy1.position, luluEnemy1)
    #     Territory.addItem(luluEnemy2.position, luluEnemy2)
    #     Territory.plulus.append(luluPrey1)
    #     Territory.plulus.append(luluEnemy1)
    #     Territory.plulus.append(luluEnemy2)

    #     luluPrey1.move()
    #     self.assertEqual(luluPrey1.position, Position(13,30)) # 1 case plus loin sur l'axe des X pour s'enfuir de l'ennemi 1

    # def test_get_closest_food(self):
    #     lulu1 = Lulu(Position(30,30), 1, 1, 100, 3, 0, False)
    #     food1 = Food(Position(31,30))
    #     food2 = Food(Position(30,35))

    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(food1.position, food1)
    #     Territory.addItem(food2.position, food2)
    #     Territory.plulus.append(lulu1)

    #     lulu1.move()
    #     self.assertEqual(lulu1.position, Position(31,30))
    #     self.assertEqual(lulu1.foodAmount == 1)

    # def test_get_closest_prey(self):
    #     luluEnemy1 = Lulu(Position(12,50), 1, 2, 120, 4, 0, False) # L'ennemi
    #     luluPrey1 = Lulu(Position(10,50), 1, 1, 100, 3, 0, False) # proie 1 (plus près)
    #     luluPrey2 = Lulu(Position(18,50), 1, 1, 100, 3, 0, False) # proie 2 (plus loin)
    #     Territory.addItem(luluEnemy1.position, luluEnemy1)
    #     Territory.addItem(luluPrey1.position, luluPrey1)
    #     Territory.addItem(luluPrey2.position, luluPrey2)
    #     Territory.plulus.append(luluEnemy1)
    #     Territory.plulus.append(luluPrey1)
    #     Territory.plulus.append(luluPrey2)

    #     luluEnemy1.move()
    #     self.assertEqual(luluEnemy1.position, Position(11,50)) # 1 case plus loin sur l'axe des X pour s'approcher de la proie 1

class TestTargetPosition(unittest.TestCase):
    def test_newRandomPosition(self):
        # Teste si la nouvelle position cible aléatoire est différente de l'ancienne/la position cible actuelle
        lulu1 = Lulu(Position(50,50), 1, 1, 100, 3, 0, False)
        oldPos = lulu1.randomTargetPosition
        newPos = lulu1.newRandomPosition()
        self.assertNotEqual(oldPos, newPos)

    def test_closeToTargetPosition(self):
        # Teste si la Lulu est près de la position cible
        lulu1 = Lulu(Position(60,50), 1, 1, 100, 3, 0, False)
        lulu1.randomTargetPosition = Position(61,50)
        self.assertTrue(lulu1.isCloseToTargetPosition())
    
    # def test_goToTargetPosition(self):
    #     # Tests if the Lulu is getting closer to the target position
    #     lulu1 = Lulu(Position(70,50), 1, 1, 100, 3, 0, False)
    #     targetPosition = lulu1.randomTargetPosition
    #     oldDistance = max(abs(lulu1.position.x - targetPosition.x), abs(lulu1.position.y - targetPosition.y))
    #     # Attendre 1 tour/1 move
    #     lulu1.move()
    #     currentDistance = max(abs(lulu1.position.x - targetPosition.x), abs(lulu1.position.y - targetPosition.y))
    #     self.assertLess(currentDistance, oldDistance)

# class TestItems(unittest.TestCase): # Tester avec un territoire 3x3, 1 food et X lulus
#     def test_getItems(self): # foodInRange, lulusInRange - en paramètres
#         lulu1 = Lulu(Position(80,50), 1, 3, 100, 3, 0, False)
#         lulu2 = Lulu(Position(79,50), 1, 1, 100, 3, 0, False)
#         lulu3 = Lulu(Position(81,50), 1, 1, 100, 3, 0, False)
#         food1 = Food(Position(80,51))
#         lulu1.getItems(foodInRange, lulusInRange)
#         self.assertTrue(len(foodInRange) == 1 and len(lulusInRange) == 2)

# class TestPosition(unittest.TestCase):
#     def test_reset_position(self):
#         # Quadrant 1
#         lulu11 = Lulu(Position(95,75), 1, 1, 100, 3, 0, False)
#         lulu12 = Lulu(Position(94,75), 1, 1, 100, 3, 0, False)
#         lulu21 = Lulu(Position(75,95), 1, 1, 100, 3, 0, False)
#         lulu22 = Lulu(Position(75,94), 1, 1, 100, 3, 0, False)
#         # Quadrant 2
#         lulu31 = Lulu(Position(5,75), 1, 1, 100, 3, 0, False)
#         lulu32 = Lulu(Position(6,75), 1, 1, 100, 3, 0, False)
#         lulu41 = Lulu(Position(25,95), 1, 1, 100, 3, 0, False)
#         lulu42 = Lulu(Position(25,94), 1, 1, 100, 3, 0, False)
#         # Quadrant 3
#         lulu51 = Lulu(Position(5,25), 1, 1, 100, 3, 0, False)
#         lulu52 = Lulu(Position(6,25), 1, 1, 100, 3, 0, False)
#         lulu61 = Lulu(Position(25,5), 1, 1, 100, 3, 0, False)
#         lulu62 = Lulu(Position(25,6), 1, 1, 100, 3, 0, False)
#         # Quadrant 4
#         lulu71 = Lulu(Position(95,25), 1, 1, 100, 3, 0, False)
#         lulu72 = Lulu(Position(94,25), 1, 1, 100, 3, 0, False)
#         lulu81 = Lulu(Position(75,5), 1, 1, 100, 3, 0, False)
#         lulu82 = Lulu(Position(75,6), 1, 1, 100, 3, 0, False)

#         lulu11.resetPosition()
#         lulu12.resetPosition()
#         lulu21.resetPosition()
#         lulu22.resetPosition()
#         lulu31.resetPosition()
#         lulu32.resetPosition()
#         lulu41.resetPosition()
#         lulu42.resetPosition()
#         lulu51.resetPosition()
#         lulu52.resetPosition()
#         lulu61.resetPosition()
#         lulu62.resetPosition()
#         lulu71.resetPosition()
#         lulu72.resetPosition()
#         lulu81.resetPosition()
#         lulu82.resetPosition()

#         self.assertEqual(lulu11.position, Position(100,75))
#         self.assertEqual(lulu12.position, Position(100,76))
#         self.assertEqual(lulu21.position, Position(75,100))
#         self.assertEqual(lulu22.position, Position(76,100))

#         self.assertEqual(lulu31.position, Position(0,75))
#         self.assertEqual(lulu32.position, Position(0,76))
#         self.assertEqual(lulu41.position, Position(25,100))
#         self.assertEqual(lulu42.position, Position(26,100))

#         self.assertEqual(lulu51.position, Position(0,25))
#         self.assertEqual(lulu52.position, Position(0,26))
#         self.assertEqual(lulu61.position, Position(25,0))
#         self.assertEqual(lulu62.position, Position(26,0))

#         self.assertEqual(lulu71.position, Position(100,25))
#         self.assertEqual(lulu72.position, Position(100,26))
#         self.assertEqual(lulu81.position, Position(75,0))
#         self.assertEqual(lulu82.position, Position(76,0))

if __name__ == '__main__':
    unittest.main() 
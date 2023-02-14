import unittest
import numpy as np
import time
import random

import sys
import pathlib

workingDir = pathlib.Path().resolve()
sys.path.insert(0, str(workingDir) + '\Application')

from Application.Models import Territory
from Application.Models import Lulu
from Application.Models import Food
from Application.Models import Position

# from Models.Lulu import Lulu
# from Models.Position import Position
# from Models.Food import Food
# import Models.Territory as Territory

X = 25
Y = 25
numberOfFood = 10
numberOfLulus = 10
speed = 1
sense = 1
energy = 3
size = 100
mutateChance = 0.3
Territory.createMap(X,Y,numberOfFood,numberOfLulus,speed,sense,energy,size,mutateChance) # 25x25, 10 Food, 10 Lulus, etc...

#Clear la map des Lulus et de Food entre chaque Test????? **************

class TestCreateMap(unittest.TestCase):
    def test_max_X_Y(self):
        # Teste si les limites de la map ont bien été générées en X et en Y
        testX = Territory.__sizeX
        testY = Territory.__sizeY
        self.assertTrue(X == testX and Y == testY)

    def test_number_of_food(self):
        testFood = Territory.__foodCount
        self.assertEqual(numberOfFood, testFood)

    def test_number_of_lulu(self):
        testLulu = Territory.__lulusCount
        self.assertEqual(numberOfLulus, testLulu)

    def test_lulu_attributes(self):
        lulusTest = Territory.getLulus()
        counter = 0
        for l in lulusTest:
            if(l.speed == speed and l.sense == sense and l.energy == energy and l.size == size and l.mutateChance == mutateChance):
                counter += 1
        self.assertEqual(counter, numberOfLulus)

class TestCreateLulu(unittest.TestCase):
    def test_lulu_created_empty(self):
        created = Territory.__CreateLulu(5,5,speed, sense, size, energy, 0, False)
        self.assertTrue(created)

    def test_lulu_not_created(self): 
        # Est-ce que les tests sont enchaînés un à la suite de l'autre ou est-ce que les tests doivent être indépendants des autres? -> va changer la manière d'approcher le test
        created = Territory.__CreateLulu(5,5,speed, sense, size, energy, 0, False)
        self.assertFalse(created)

    def test_lulu_added_to_list(self):
        len1 = len(Territory.getLulus())
        created = Territory.__CreateLulu(6,5,speed, sense, size, energy, 0, False)
        len2 = len(Territory.getLulus())
        self.assertGreater(len2, len1)
        #self.assertEqual(lulu, Territory.getLulus()[len2 - 1])

class TestCreateFood(unittest.TestCase):
    def test_food_created_empty(self):
        oldCounter = Territory.__foodCount
        created = Territory.CreateFood(10,10)
        self.assertTrue(created)
        newCounter = Territory.__foodCount
        self.assertGreater(newCounter, oldCounter)

    def test_food_not_created(self):
        # Est-ce qu'on a le droit d'utiliser d'autres méthodes? exemple: getItem?????? ça serait très utile
        # Est-ce que les tests sont enchaînés un à la suite de l'autre ou est-ce que les tests doivent être indépendants des autres? -> va changer la manière d'approcher le test
        created = Territory.CreateFood(10,10)
        self.assertFalse(created)

class TestMap(unittest.TestCase):
    def test_get_map(self):
        map = Territory.getMap()
        self.assertNotEqual(map, None)

    def test_get_sizeX(self):
        testX = Territory.getSizeX()
        testY = Territory.getSizeY()
        self.assertTrue(X == testX and Y == testY)

class TestItem(unittest.TestCase):
    def test_add_item(self):
        lulu = Lulu(20,20,speed,sense,size,energy,0,False)
        Territory.__addItem(lulu.position, lulu)
        map = Territory.getMap()
        self.assertEqual(lulu, map[lulu.position])

    def test_delete_item(self):
        lulu = Lulu(20,20,speed,sense,size,energy,0,False)
        Territory.__addItem(lulu.position, lulu)
        luluDictionnary = Territory.getItem(lulu.position)
        Territory.__deleteItem(luluDictionnary.position)
        self.assertEqual(luluDictionnary, Territory.getMap()[luluDictionnary.position]) # Va peut-être crash



    






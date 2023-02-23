import unittest
import numpy as np
import time
import random

# import sys
# import pathlib

# workingDir = pathlib.Path().resolve()
# sys.path.append(str(workingDir) + '\Application')
#sys.path.append('../Application/')
#sys.path.append('Application/')

# Tests commentés avec problème: 291, 313, 147, 69, 102

import Territory
from Lulu import Lulu 
from Position import Position
from Food import Food

X = 100
Y = 100
numberOfFood = 10
numberOfLulus = 10
speed = 1
sense = 1
energy = 3
size = 100
mutateChance = 0.3

Territory.createMap(X,Y,numberOfFood,numberOfLulus,speed,sense,energy,size,mutateChance,mutateChance,mutateChance,mutateChance) # 25x25, 10 Food, 10 Lulus, etc...
oldLulusList = Territory.getLulus().copy()
Territory.moveAll()
Territory.resetWorld()
Territory.dayResultLulu()

class TestCreateMap(unittest.TestCase):

    # def test_lulu_attributes(self):
    #     #Territory.createMap(X,Y,numberOfFood,numberOfLulus,speed,sense,energy,size,mutateChance,mutateChance,mutateChance,mutateChance) # 25x25, 10 Food, 10 Lulus, etc...
        
    #     lulusTest = Territory.getLulus().copy()
    #     counter = 0
    #     for l in lulusTest:
    #         if(l.speed == speed and l.sense == sense and l.energy == energy and l.size == size):
    #             counter += 1
    #     self.assertEqual(counter, numberOfLulus)

    def test_max_X_Y(self):        
        # Teste si les limites de la map ont bien été générées en X et en Y
        testX = Territory.psizeX
        testY = Territory.psizeY
        self.assertTrue(X == testX and Y == testY)

    def test_number_of_food(self):  
        # Teste que le nombre de nourriture a bien été passé en paramètres et est utilisé dans la création de la map      
        testFood = Territory.pfoodCount
        self.assertEqual(numberOfFood, testFood)

    def test_number_of_lulu(self): 
         # Teste que le nombre de Lulus a bien été passé en paramètres et est utilisé dans la création de la map      
        testLulu = Territory.plulusCount
        self.assertEqual(numberOfLulus, testLulu)

    

class TestCreateLulu(unittest.TestCase):
    def test_lulu_created_empty(self):
        # Teste qu'une Lulu a été créée et ajoutée dans une case vide
        created = Territory.CreateLulu(5,5,speed, sense, size, energy, 0, False)
        self.assertTrue(created)

    def test_lulu_not_created(self): 
        # Teste qu'une Lulu ne se crée pas quand on tente de l'ajouter dans une case déjà occupée 
        # (dans ce cas-ci il s'agit de l'autre Lulu déjà créée en (5,5) dans le test précédent)
        created = Territory.CreateLulu(5,5,speed, sense, size, energy, 0, False)
        self.assertFalse(created)

    def test_lulu_added_to_list(self):
        # Teste qu'une Lulu nouvellement créée est bel et bien ajoutée à la liste actuelle de Lulus
        len1 = len(Territory.getLulus())
        created = Territory.CreateLulu(6,5,speed, sense, size, energy, 0, False)
        len2 = len(Territory.getLulus())
        self.assertGreater(len2, len1)
        #self.assertEqual(lulu, Territory.getLulus()[len2 - 1])

class TestCreateFood(unittest.TestCase):
    def test_food_created_empty(self):
        # Teste qu'une Nourriture (Food) a été créée et ajoutée dans une case vide
        oldCounter = Territory.pnumberOfFood
        created = Territory.CreateFood(10,10)
        self.assertTrue(created)
        newCounter = Territory.pnumberOfFood
        self.assertGreater(newCounter, oldCounter)

    def test_food_not_created(self):
        # Teste qu'une nourriture (Food) ne se crée pas quand on tente de l'ajouter dans une case déjà occupée 
        # (dans ce cas-ci il s'agit de la nourriture déjà créée en (10,10) dans le test précédent)
        created = Territory.CreateFood(10,10)
        self.assertFalse(created) # Retourne false car on a déjà une food à 10,10 et donc la food n'a pas été créée

class TestGet(unittest.TestCase):
    def test_get_map1(self):
        # Teste que la méthode get_map retourne bel et bien la map du territoire
        map = Territory.getMap()
        self.assertNotEqual(map, None)

    # Version #2 du test
    def test_get_map2(self):
        lulu1 = Lulu(Position(80,40), 3, 3, 145, 5, 0, False)
        Territory.addItem(lulu1.position, lulu1)
        Territory.plulus.append(lulu1)
        map = Territory.getMap()
        self.assertEqual(map[lulu1.position], lulu1)

    # Version #3 du test
    def test_get_map3(self):
        map = Territory.getMap()
        self.assertEqual(map, Territory.pmap)

    def test_get_sizeX_and_sizeY(self):
        # Teste qu'on retourne bel et bien les valeurs en taille X et Y du territoire précédemment
        # passés en paramètres lors de la génération du territoire, X et Y sont les variables
        # globales au début du fichier de test utilisés dans la création du territoire (lignes 21, 22 et 31)
        testX = Territory.getSizeX()
        testY = Territory.getSizeY()
        self.assertTrue(X == testX and Y == testY)

    def test_get_lulus(self):  
        # Teste que la méthode get_lulus retourne bel et bien la liste de Lulus actuellement présentes dans la map (dictionnaire (Territoire))      
        lulusList = Territory.getLulus()
        self.assertEqual(lulusList, Territory.plulus)

    
    # def test_get_lulu_map(self):
    #     luluCount = Territory.getLuluMap()
    #     self.assertTrue(luluCount >= numberOfLulus)

# class TestPrint(unittest.TestCase):
#     def test_print_map(self):

class TestItem(unittest.TestCase):
    def test_get_item(self):
        # Teste le retour de la méthode get_item
        lulusTest = Territory.getLulus()
        lulu = lulusTest[0]
        posItem1 = Position(lulu.position.x, lulu.position.y)

        item1 = Territory.getItem(posItem1.x, posItem1.y)
        item2 = Territory.getItem(random.randint(1, Territory.getSizeX()), random.randint(1, Territory.getSizeY()))
        item3 = Territory.getItem(random.randint(1, Territory.getSizeX()), random.randint(1, Territory.getSizeY()))

        self.assertEqual(type(item1), Lulu)
        self.assertTrue(item2 == None or type(item2) == Lulu or type(item2) == Food)
        self.assertTrue(item3 == None or type(item3) == Lulu or type(item3) == Food)

    def test_add_item(self):
        # Teste qu'on ajoute bien un item dans la map (dictionnaire (Territoire)) en comparant la position avant et après l'ajout
        lulu = Lulu(Position(20,20),speed,sense,size,energy,0,False)
        Territory.addItem(lulu.position, lulu)
        map = Territory.getMap()
        self.assertEqual(lulu, map[lulu.position])

    def test_delete_item(self):
        # Teste qu'on retire bien un item de la map (dictionnaire (Territoire)) en comparant la position avant et après la suppression
        lulu = Lulu(Position(20,20),speed,sense,size,energy,0,False)
        Territory.addItem(lulu.position, lulu)
        luluDictionnary = Territory.getItem(lulu.position.x, lulu.position.y)
        Territory.deleteItem(luluDictionnary.position)
        self.assertNotEqual(type(luluDictionnary), type(Territory.getMap().get(luluDictionnary.position))) 

class TestTryMove(unittest.TestCase):
    def test_outside_of_map(self):
        # Teste qu'une Lulu ne peut pas se déplacer en dehors des limites du Territoire (sous 0 en axe des X et Y et au-dessus du maxX et maxY)
        lulu1 = Lulu(Position(100,100), 1, 1, 100, 3, 0, False)
        lulu1.randomTargetPosition = Position(101,101)
        Territory.addItem(lulu1.position, lulu1)
        Territory.plulus.append(lulu1)
        self.assertFalse(Territory.tryMove(lulu1.position, lulu1.randomTargetPosition))

    def test_not_eatable_lulu(self):
        # Teste qu'une Lulu pas assez grande en taille pour en manger une autre essaie de se déplacer à la position de celle-ci
        # (retourne False car il est impossible pour 2 Lulus d'être sur la même case puisque lulu1 n'est pas assez forte pour manger lulu2)
        lulu1 = Lulu(Position(60,60), 1, 1, 100, 3, 0, False)
        lulu2 = Lulu(Position(61,60), 1, 1, 100, 3, 0, False) 
        Territory.addItem(lulu1.position, lulu1)
        Territory.addItem(lulu2.position, lulu2)
        Territory.plulus.append(lulu1)
        Territory.plulus.append(lulu2)
        self.assertFalse(Territory.tryMove(lulu1.position, lulu2.position))

    # def test_eat_food(self):
    #     lulu1 = Lulu(Position(40,40), 1, 1, 100, 3, 0, False)
    #     food1 = Food(Position(40,41))
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(food1.position, food1)
    #     Territory.plulus.append(lulu1)
    #     self.assertTrue(Territory.tryMove(lulu1.position, food1.position))

    # def test_eat_lulu_prey(self):
    #     lulu1 = Lulu(Position(50,70), 1, 1, 90, 3, 0, False) # proie
    #     lulu2 = Lulu(Position(50,71), 1, 2, 120, 6, 0, False) # ennemi
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.addItem(lulu2.position, lulu2)
    #     Territory.plulus.append(lulu1)
    #     Territory.plulus.append(lulu2)
    #     self.assertTrue(Territory.tryMove(lulu2.position, lulu1.position))

class TestMoveLulu(unittest.TestCase):
    def test_move_lulu(self):
        # Teste le changement de position d'une Lulu dans la map (dictionnaire (Territoire))
        lulu1 = Lulu(Position(50,80), 1, 2, 120, 6, 0, False) 
        lulu2 = Lulu(Position(50,81), 1, 1, 100, 3, 0, False) 
        oldFoodAmount = lulu1.foodAmount

        Territory.addItem(lulu1.position, lulu1)
        Territory.addItem(lulu2.position, lulu2)
        Territory.plulus.append(lulu1)
        Territory.plulus.append(lulu2)
        oldlulu1position = lulu1.position
        Territory.moveLulu(lulu1.position, lulu2.position)
        lulusList = Territory.getLulus()
        self.assertEqual(Territory.getMap().get(oldlulu1position), None) # Vérifie que l'ancienne position est maintenant vide
        self.assertEqual(Territory.getMap()[lulu2.position], lulu1) # Vérifie si la Lulu1 est maintenant à la nouvelle position
        self.assertGreater(Territory.getMap()[lulu2.position].foodAmount, oldFoodAmount) # Vérifie si foodAmount s'est incrémenté
        self.assertNotEqual(lulusList[len(lulusList) - 1], lulu2) # Vérifie si la lulu mangée a été retirée de la liste

        #self.assertNotEqual(Territory.getMap()[lulu1.position], Territory.getMap()[lulu2.position])
        #self.assertEqual(type(Territory.getMap()[lulu2.position]), Lulu) # Vérifie si une Lulu se trouve à la nouvelle position

class TestMoveAll(unittest.TestCase):
    def test_move_all(self):
        # Teste si toutes les Lulus ont bougé, si oui, les listes ne seront pas égales
        Territory.moveAll()
        lulusList2 = Territory.getLulus()
        self.assertNotEqual(oldLulusList, lulusList2)

class TestFood(unittest.TestCase):
    # Vérifie toute les cases du périmètres pour s'assurer qu'il n'y a pas de nourriture
    def test_set_food(self):
        Territory.setFood()
        for x in range(1, X + 1):
            self.assertNotEqual(type(Territory.getItem(x,1)), Food)
            self.assertNotEqual(type(Territory.getItem(x,Y)), Food)
        for y in range(1, Y + 1):
            self.assertNotEqual(type(Territory.getItem(1,y)), Food)
            self.assertNotEqual(type(Territory.getItem(X,y)), Food)

class TestDayResultLulu(unittest.TestCase):
    def test_delete_not_survived(self):
        # Enregistre les positions des Lulus qui ne survivent pas la journée qui doivent être supprimées,
        # appelle la méthode puis vérifie que ces lulus ont bien disparues en comparant les positions
        # de toutes les Lulus restantes avec celles des Lulus à supprimer
        oldLulusList = Territory.getLulus()
        lulusToDelete = []
        for l in oldLulusList:
            if(l.foodAmount == 0 and not l.isNewBorn):
                lulusToDelete.append(l.position)

        Territory.dayResultLulu()
        newLulusList = Territory.getLulus()

        i = 0
        values = range(len(lulusToDelete))

        for l in newLulusList:
            for j in values:
                self.assertNotEqual(l.position, lulusToDelete[j])
            

    def test_reset_params_default(self):
        # Teste si les paramètres foodAmount et isNewBorn des Lulus sont réinitialisés à leurs valeurs par défaut après une génération
        lulusList = Territory.getLulus()
        for l in lulusList:
            self.assertTrue(l.foodAmount == 0 and l.isNewBorn == False)
        
class TestResetWorld(unittest.TestCase):
    # def test_reset_food(self): 

    #     #Territory.createMap(X,Y,numberOfFood,numberOfLulus,speed,sense,energy,size,mutateChance,mutateChance,mutateChance,mutateChance) # 25x25, 10 Food, 10 Lulus, etc...
    #     Territory.moveAll()
    #     Territory.resetWorld()
    #     Territory.dayResultLulu()
    #     self.assertEqual(Territory.pnumberOfFood, numberOfFood)

    def test_reset_params_default(self):
        # Teste si les paramètres isDone et energy des Lulus sont réinitialisés à leurs valeurs par défaut
        Territory.moveAll()
        Territory.resetWorld()
        Territory.dayResultLulu()
        lulusList = Territory.getLulus()
        for l in lulusList:
            self.assertTrue(l.isDone == False and l.energy == energy)

class TestReproduceLulu(unittest.TestCase): 
    # def test_list_lulu_incremented(self):
    #     #Territory.createMap(X,Y,numberOfFood,numberOfLulus,speed,sense,energy,size,mutateChance,mutateChance,mutateChance,mutateChance) # 25x25, 10 Food, 10 Lulus, etc...
    #     # oldLulusList = Territory.getLulus()
    
    #     for l in Territory.plulus:
    #         if(l.foodAmount > 1):
    #             Territory.reproduceLulu(l)
    #     newLulusList = Territory.getLulus()
    #     self.assertGreater(len(newLulusList), len(oldLulusList))

    # def test_parent_replaced_by_newborn(self):
    #     lulu1 = Lulu(Position(80,Y), 10, 5, 150, 6, 0, False)
    #     Territory.addItem(lulu1.position, lulu1)
    #     Territory.pLulus.append(lulu1)
    #     for x in range(1, X + 1):
    #         if(type(Territory.getItem(x,Y)) == Lulu):
    #             if(x == X): # Si la ligne est pleine, la reproduction devrait causer un remplacement du parent par le nouveau-né
    #                 Territory.reproduceLulu(lulu1)
    #                 self.assertNotEqual(Territory.getMap()[lulu1.position], lulu1)
    
    def test_lulu_added_to_perimeter(self):
        # Teste le nombre de Lulu par axe, confirme si la Lulu nouvea-né a été ajoutée ou si un parent
        # a été remplacé dépendemment du compteur
        lulu1 = Lulu(Position(X,80), 1, 1, 100, 3, 0, False)
        Territory.addItem(lulu1.position, lulu1)
        Territory.plulus.append(lulu1)
        oldLuluCount = 0
        newLuluCount = 0
        for y in range(1, Y + 1):
            if(type(Territory.getItem(X,y)) == Lulu):
                oldLuluCount += 1
        if(oldLuluCount < Y):
            Territory.reproduceLulu(lulu1)
            for y in range(1, Y + 1):
                if(type(Territory.getItem(X,y)) == Lulu):
                    newLuluCount += 1
            self.assertGreater(newLuluCount, oldLuluCount)
        else:
            self.assertEqual(oldLuluCount, newLuluCount)

if __name__ == '__main__':
    unittest.main()


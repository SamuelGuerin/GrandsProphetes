import unittest
from Application.Models import Territory
from Application.Models import Lulu
from Application.Models import Food
from Application.Models import Position
import numpy as np
import time



Territory.createMap(3,3,0,2) #  3x3, 0 nourriture, 2 Lulus
distanceCloseToTarget = 2

# Utiliser self ou Lulu? *

class TestPriorityMovement(unittest.TestCase):
    def test_enemy(self):
        # Tests the order of priority when an enemy is in the Lulu's sense field.
        self.assertEqual()

class TestTargetPosition(unittest.TestCase):
    def test_newRandomPosition(self):
        # Tests if the new random position is different than current Target Position
        self.assertNotEqual(self.randomTargetPosition, self.newRandomPosition(self))

    def test_closeToTargetPosition(self): # Il faudrait coder un territoire 3x3 -> 1 seule target position possible -> forcément retourne True
        # Tests if the Lulu is close to the target position
        self.assertTrue(self.isCloseToTargetPosition(self)) # *
    
    def test_goToTargetPosition(self):
        # Tests if the Lulu is getting closer to the target position
        targetPosition = self.randomTargetPosition
        position = self.position
        oldDistance = max(abs(position.x - targetPosition.x), abs(position.y - targetPosition.y))
        # Attendre 1 tour/1 move
        currentDistance = max(abs(position.x - targetPosition.x), abs(position.y - targetPosition.y))
        self.assertLessEqual(currentDistance, oldDistance)

        
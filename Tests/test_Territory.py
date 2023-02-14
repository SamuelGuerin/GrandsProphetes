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


class TestNumberOfItems(unittest.TestCase):
    def test_numberOfLulus(self):
        # Tests the order of priority when an enemy is in the Lulu's sense field.
        self.assertEqual()
    def test_numberOfFood(self):
        # Tests the order of priority when an enemy is in the Lulu's sense field.
        self.assertEqual()
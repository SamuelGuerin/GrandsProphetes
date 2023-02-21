import unittest

import customtkinter as ct
from PIL import Image
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from Application.UI import Graph2 as Graph
from Application.UI import FormGraph as fg

class TestPositiveNumber(unittest.TestCase):
    def test_positiveValue(self):
        # Tests the value entered in the form to see if it's positive
        self.assertEqual()


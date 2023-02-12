import unittest

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import threading

from Application.UI import Form


class TestGraphAngleDisplay(unittest.TestCase):
    def test_differentGeneration(self):
        # Tests the angle of display of the graph after changing the displayed generation
        self.assertEqual()
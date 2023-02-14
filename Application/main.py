from manim import *
from manim.utils.file_ops import open_file as open_media_file
import SimulationManager as Simulation
import Models.Territory as Territory
from Models.Lulu import Lulu
from Models.Food import Food
from Models.Position import Position
import time
import random

class VisualizeLulus(Scene):
    def construct(self):

        items = Territory.getMap()
        # SIZE = 1/5 du plus petit x ou y?
        SIZE=Territory.getSizeX()/5 if Territory.getSizeX() < Territory.getSizeY() else Territory.getSizeY()/5
        # CENTERX = /2
        CENTERX = Territory.getSizeX()/2
        # CENTERY = /2
        CENTERY = Territory.getSizeY()/2

        groupdots = VGroup()

        maxSize = max(lulu.size for lulu in Territory.getLulus())
        minSize = min(lulu.size for lulu in Territory.getLulus())
        rangeOfSizes = maxSize - minSize

        for position in items:
            item = items.get(position)
            if(type(item) == Lulu):
                if(item.isDone):
                    rangeOfColors = rangeOfSizes/6
                    if item.size <= minSize + (rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_A)
                    elif item.size <= minSize + 2*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_B)
                    elif item.size <= minSize + 3*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_C)
                    elif item.size <= minSize + 4*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_D)
                    else:
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED_E)
                else:
                    rangeOfColors = rangeOfSizes/6
                    if item.size <= minSize + (rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_A)
                    elif item.size <= minSize + 2*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_B)
                    elif item.size <= minSize + 3*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_C)
                    elif item.size <= minSize + 4*(rangeOfColors):
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_D)
                    else:
                        dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=BLUE_E)
            elif(type(item) == Food):
                dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=GREEN)
            groupdots.add(dot)

        self.add(groupdots)

def renderAnimation():
    """Génère une image de l'état actuel du :class:`Territory`
    """
    scene = VisualizeLulus()
    scene.render()

if __name__ == '__main__':
    Simulation.__run__(100, 100, 50, 10, 25, 25, 10, 1000, 10000)
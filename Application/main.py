import numpy as np
#from manim import *
#from manim.utils.file_ops import open_file as open_media_file
import Models.Territory as Territory
from Models.Lulu import Lulu
from Models.Food import Food
from Models.Position import Position
import time
import random

# class VisualizeLulus(Scene):
#     def construct(self):

#         items = Territory.getMap()
#         # SIZE = 1/5 du plus petit x ou y?
#         SIZE=Territory.getSizeX()/5 if Territory.getSizeX() < Territory.getSizeY() else Territory.getSizeY()/5
#         # CENTERX = /2
#         CENTERX = Territory.getSizeX()/2
#         # CENTERY = /2
#         CENTERY = Territory.getSizeY()/2

#         groupdots = VGroup()

#         for position in items:
#             if(type(items.get(position)) == Lulu):
#                 dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=RED)
#             elif(type(items.get(position)) == Food):
#                 dot = Dot([(position.x - CENTERX)/SIZE, (position.y - CENTERY)/SIZE, 0], color=GREEN)
#             groupdots.add(dot)

#         self.add(groupdots)

if __name__ == '__main__':
    t0 = time.time()
    Territory.createMap(10, 10, 0, 2)
    t1 = time.time()
    total = t1-t0
    print(str(total) + " secondes")

    for l in Territory.__lulus:
        Territory.moveLulu(l.position, Position(random.randint(2,9),random.randint(2,9)))

    for l in Territory.__lulus:
        print(l.position)
        l.resetPosition()
        print(l.position)


    #print(Territory.getMap())
    #scene = VisualizeLulus()
    #scene.render()
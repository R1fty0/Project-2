"""
    Testing Spawner in Isolation
"""

import pygame
import os
import random

# SquarePNG = pygame.image.load(os.path.join("Assets", "Square.png"))

# Width and Height of the Window
WindowWidth, WindowHeight = 1000, 800

List = []


def Method(Amount):
    CurrentAmount = 0
    while CurrentAmount != Amount:
        CurrentAmount = CurrentAmount + 1
        # List.append(SquarePNG)
        print("There is " + str(len(List)) + " picture(s) in this list")
        ObjectSpawnX = random.randrange(WindowWidth) * -1
        ObjectSpawnY = random.randrange(WindowHeight) * -1
        print("X Spawn: " + str(ObjectSpawnX))
        print("Y Spawn: " + str(ObjectSpawnY))



print(15 + 5 + 15 + 15 + 15 + 15 + 15 + 15 + 30)





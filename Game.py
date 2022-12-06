# Imports
import os
import pygame

# Refresh Rate of Program
FPS = 60

# Dimensions of Game Window
Width, Height = 960, 960

# Brown Square - Used as a tile on the board
BrownSquare = pygame.image.load(os.path.join("Assets", "BrownSquare.png"))

# Orange Square - Used as a tile on the board
OrangeSquare = pygame.image.load(os.path.join("Assets", "OrangeSquare.png"))

# Green Checker Piece

GreenChecker = pygame.image.load(os.path.join("Assets", "GreenChecker.png"))

# Blue Checker Piece
BlueChecker = pygame.image.load(os.path.join("Assets", "BlueChecker.png"))

# Arrays that contain all the pieces of the game.
# 16 Checker Pieces of each colour. 32 Board Pieces for each color.
BrownSquarePieces = [BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare,
                     BrownSquare, BrownSquare, BrownSquare, BrownSquare]

OrangeSquarePieces = [OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare,
                      OrangeSquare, OrangeSquare, OrangeSquare, OrangeSquare]

GreenCheckerPieces = [GreenChecker, GreenChecker, GreenChecker, GreenChecker,
                      GreenChecker, GreenChecker, GreenChecker, GreenChecker,
                      GreenChecker, GreenChecker, GreenChecker, GreenChecker,
                      GreenChecker, GreenChecker, GreenChecker, GreenChecker,]


BlueCheckerPieces = [BlueChecker, BlueChecker, BlueChecker, BlueChecker,
                     BlueChecker, BlueChecker, BlueChecker, BlueChecker,
                     BlueChecker, BlueChecker, BlueChecker, BlueChecker,
                     BlueChecker, BlueChecker, BlueChecker, BlueChecker]


# Creates Window and Name of the Game
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Checkers")

def Draw():


    # Updates the Screen with the changes made by this function.
    pygame.display.update()


# All Game Logic is called here...
def Update():
    # Clock that maintains FPS
    clock = pygame.time.Clock()
    # If this boolean is true, then the program runs.
    run = True
    while run:
        clock.tick(FPS)
        # Terminates Program if the User Closes the Application
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                Draw()


# Calls Update Method - similar to Unity's Update Method
if __name__ == "__Game__":
    Update()

# Imports
import pygame
import os

"""
    Game Window Variables
"""

# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 1000, 800

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window
# Window Name
pygame.display.set_caption("SquareSpace")

"""
    Colours Used (In RGB Format)
"""
# Colors - Color Palette: https://coolors.co/694a38-a61c3c-5b9279-3a6ea5-e9d2c0
Coffee = (105, 74, 56)
VividBurgundy = (166, 28, 60)
IlluminatingEmerald = (91, 146, 121)
QueenBlue = (58, 110, 165)
ChampagnePink = (233, 210, 192)

"""
    Image Imports - Imported from Assets Folder
"""



"""
    Player Stats
"""
PlayerSpeed = 10
PlayerSpawnX = WindowWidth/1.47
PlayerSpawnY = WindowHeight/1.47

"""
    Player Movement States
"""
CanMoveLeft = True
CanMoveRight = True

"""
    Spawner Variables
"""


"""
    Visuals
"""


def Graphics(Player):  # All Visuals are "drawn" here.
    Window.fill(ChampagnePink)  # Background Color

    # Window.blit(PlayerPNG, (Player.x, Player.y))  # Draws Player Picture at current position of Player Object

    pygame.display.update()  # Updates the Screen


"""
    Player Movement
"""


def Movement(Player):
    GetKeyDown = pygame.key.get_pressed()  # Basically "Input.GetKeyDown"

    if GetKeyDown[pygame.K_a] and CanMoveLeft:  # Moves Player to the Left
        Player.x -= PlayerSpeed
        print("A Key Down, Moving Left")

    elif GetKeyDown[pygame.K_d] and CanMoveRight:   # Moves Player to the Right
        Player.x += PlayerSpeed
        print("D Key Down, Moving Right")


"""
    Collision Detection - Boundaries
"""


def CollisionDetection(Player):
    # Global Variables
    global CanMoveLeft
    global CanMoveRight

    # Checks if Player Has Hit the Left Side of the Window
    if Player.left <= 0:
        CanMoveLeft = False
    elif Player.left >= 0:
        CanMoveLeft = True
    # Checks if Player Has Hit the Right Side of the Window
    if Player.right >= WindowWidth:
        CanMoveRight = False
    elif Player.right <= WindowWidth:
        CanMoveRight = True


"""
    Main Game Loop
"""


def Run():  # Basically the Unity Update Method - all code runs here (Main Game Loop).

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    # Creates and spawns a Game Object that represents the player - in Pygame it is known as a "Rect" (Rectangle)
    Player = pygame.Rect(PlayerSpawnX, PlayerSpawnY, PX, PY)

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Game Loop - code runs here
        GameClock.tick(FPS)  # Runs the Game at the Desired FPS
        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False
        CollisionDetection(Player)  # Collision Detection
        Movement(Player)  # Movement
        Graphics(Player)  # Visuals

    pygame.quit()  # Quits program


"""
    Program Starts Here
"""
if __name__ == "__main__":  # Program Starts Here
    Run()

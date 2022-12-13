# Imports
import os
import pygame

"""
Current Problems:
- When Mouse Button Is Pressed, Game Piece (X or O) is drawn, but is removed when mouse button is released...

"""

# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 800, 800

# White Color - the main colour for the background
White = (255, 255, 255)  # this is an RGB value, it does not work with any other type of color system apparently

# Images - Loads them from Assets File Folder.
X = pygame.image.load(os.path.join("../Assets", "X.png"))  # 64 x 64
O = pygame.image.load(os.path.join("../Assets", "O.png"))  # 64 x 64
Board = pygame.image.load(os.path.join("../Assets", "Board.png"))  # 685 x 685


# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window
# Window Name
pygame.display.set_caption("Not Tic Tac Toe...")


# IsClicked = False  # True if the Left Mouse Button is Pressed ( NOT IN USE)

# Turns - Which Player has their turn
PlayerA = True
PlayerB = False

"""
    Functions Below, Variables Above...
"""


def Graphics(MousePosition, IsKeyDown):  # All Images seen on screen are "drawn" here.
    Window.fill(White)  # Background Color
    Window.blit(Board, (WindowWidth/13, WindowHeight/13))  # Board

    if IsKeyDown:
        Window.blit(X, MousePosition)  # Draws an X at the Mouse Position if the Mouse Button is Pressed.

    pygame.display.update()  # Updates the Screen


def Run():  # Basically the Unity Update Method - all code runs here.

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Game Loop - code runs here
        GameClock.tick(FPS)  # Runs the Game at the Desired FPS

        MousePosition = pygame.mouse.get_pos()  # Current Mouse Position
        IsClicked = pygame.mouse.get_pressed()[0]  # True if the Left Mouse Button is Pressed

        Graphics(MousePosition, IsClicked)  # Visuals on Screen
        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False

    pygame.quit()  # Quits program


if __name__ == "__main__":  # Program Starts Here
    Run()

# Imports
import pygame
import os

"""
    Game Window Variables
"""

# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 512, 512

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window
# Window Name
pygame.display.set_caption("OnTarget")

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
    Image Imports - From Assets Folder
"""
# Player 1
Player1PNG = pygame.image.load(os.path.join("Assets", "Player1.png"))  # 128 x 128
P1X, P1Y = 24, 24  # X and Y Dimensions

# Player 2
Player2PNG = pygame.image.load(os.path.join("Assets", "Player2.png"))  # 128 x 128
P2X, P2Y = 24, 24  # X and Y Dimensions

# Ball
BallPNG = pygame.image.load(os.path.join("Assets", "Ball.png"))  # 64 x 64
BX, BY = 48, 48  # X and Y Dimensions

"""
    Spawn Locations - Fix these by making them modular
"""

Player1SpawnX = 250
Player1SpawnY = 30

Player2SpawnX = 250
Player2SpawnY = 400

BallSpawnX = WindowWidth/2
BallSpawnY = WindowHeight/2

# Player Speed
PlayerSpeed = 10


"""
    Movement States
"""
CanMoveLeft = True
CanMoveRight = True


"""
    Collision Detection
"""

def CollisionDetection(Player1):
    # Global Variables
    global CanMoveLeft
    global CanMoveRight

    # Checks if Player Has Hit the Left Side of the Window
    if Player1.left <= 0:
        CanMoveLeft = False
    elif Player1.left >= 0:
        CanMoveLeft = True
    # Checks if Player Has Hit the Right Side of the Window
    if Player1.right >= WindowWidth:
        CanMoveRight = False
    elif Player1.right <= WindowWidth:
        CanMoveRight = True

"""
    Movement
"""

def Movement(Player1, Player2):

    # Player 1 Movement Code
    GetKeyDown = pygame.key.get_pressed()  # Basically "Input.GetKeyDown"

    if GetKeyDown[pygame.K_a] and CanMoveLeft:  # Moves Player to the Left
        Player1.x -= PlayerSpeed

    elif GetKeyDown[pygame.K_d] and CanMoveRight:   # Moves Player to the Right
        Player1.x += PlayerSpeed

    # Player 2 Movement Code Below
    if GetKeyDown[pygame.K_LEFT] and CanMoveLeft:  # Moves Player to the Left using the Left Arrow Key
        Player2.x -= PlayerSpeed

    elif GetKeyDown[pygame.K_RIGHT] and CanMoveRight:   # Moves Player to the Right
        Player2.x += PlayerSpeed



"""
    Graphics
"""


def Graphics(Player1, Player2, Ball):  # All Visuals are "drawn" here.
    Window.fill(ChampagnePink)  # Background Color

    Window.blit(Player1PNG, (Player1.x, Player1.y))  # Draws Player Picture at current position of Player Object
    Window.blit(Player2PNG, (Player2.x, Player2.y))  # Draws Player Picture at current position of Player Object

    Window.blit(BallPNG, (Ball.x, Ball.y))  # Draws Ball

    pygame.display.update()  # Updates the Screen


"""
    Main Game Loop
"""


def Run():  # Basically the Unity Update Method - all code runs here (Main Game Loop).

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    Player1 = pygame.Rect(Player1SpawnX, Player1SpawnY, P1X, P1Y)  # Player 1 Game Object

    Player2 = pygame.Rect(Player2SpawnX, Player2SpawnY, P2X, P2Y)  # Player 2 Game Object

    Ball = pygame.Rect(BallSpawnX, BallSpawnY, BX, BY)  # Ball

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Game Loop
        GameClock.tick(FPS)  # Game Runs at this FPS
        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False
        Movement(Player1, Player2)
        CollisionDetection(Player1)
        Graphics(Player1, Player2, Ball)

    pygame.quit()  # Quits program


"""
    Main Menu
"""


def MainMenu():
    #TitleFont = pygame.font.SysFont("Century", 40, False, False)
    run = True
    while run:
        Window.fill(QueenBlue)
        #TitleLabel = TitleFont.render("Press any mouse button to begin...", 1, Coffee)
        #Window.blit(TitleLabel, (WindowWidth/2 - TitleLabel.get_width()/2, WindowHeight/2 - TitleLabel.get_height()/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Run()


"""
    Program Starts Here
"""
if __name__ == "__main__":  # Program Starts Here
    MainMenu()



# Imports
import pygame
import os
pygame.font.init()

"""
    Game Window Variables
"""

# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 500, 500

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window
# Window Name
pygame.display.set_caption("Soccer_Game")


"""
    Classes
"""
class GameObject:
    def __init__(self, image):
        self.image = image

    def GetImage(self):
        return self.image
class MidLine:
    def __init__(self, image):
        self.image = image
class Ball:
    def __init__(self, image):
        self.image = image

class Goal:
    def __init__(self, side, image):
        self.side = side  # 1 = Player 1, 2 = Player 2
        self.image = image


class Color:
    def __init__(self, color):  # Constructor
        self.color = color  # Tuple containing Color RGB Values

    def GetColor(self):
        return self.color

class Player:  # Player 1 is Red, Player 2 is Blue
    def __init__(self, name, image, spawnX, spawnY, speed, upKey, downKey, leftKey, rightKey):
        self.name = name
        self.image = image
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.speed = speed
        self.upKey = upKey
        self.downKey = downKey
        self.leftKey = leftKey
        self.rightKey = rightKey

    CanMoveUp = True
    CanMoveDown = True
    CanMoveLeft = True
    CanMoveRight = True

    # def GoalCollisionDetection(self, Player_Rect, Goal_Rect):
        # Checks if Player has hit the Goal Post
    def WindowCollisionDetection(self, Player_Rect):

        # Checks if Player has hit the Top of the Window
        if Player_Rect.top <= 0:
            self.CanMoveUp = False
        elif Player_Rect.top >= 0:
            self.CanMoveUp = True

        # Checks if Player has hit the Bottom of the Window
        if Player_Rect.bottom >= WindowHeight:
            self.CanMoveDown = False
        elif Player_Rect.bottom <= WindowHeight:
            self.CanMoveDown = True

        # Checks if Player has hit Left side of Window
        if Player_Rect.left <= 0:
            self.CanMoveLeft = False
        elif Player_Rect.left >= 0:
            self.CanMoveLeft = True

        # Checks if Player Has Hit the Right Side of the Window
        if Player_Rect.right >= WindowWidth:
            self.CanMoveRight = False
        elif Player_Rect.right <= WindowWidth:
            self.CanMoveRight = True

    def Movement(self, Player_Rect):
        GetKeyDown = pygame.key.get_pressed()  # Basically "Input.GetKeyDown" from Unity

        if GetKeyDown[self.upKey] and self.CanMoveUp:  # Moves Player Forward
            Player_Rect.y -= self.speed

        if GetKeyDown[self.downKey] and self.CanMoveDown:  # Moves Player Backwards
            Player_Rect.y += self.speed

        if GetKeyDown[self.rightKey] and self.CanMoveRight:  # Moves Player to the Right
            Player_Rect.x += self.speed

        if GetKeyDown[self.leftKey] and self.CanMoveLeft:  # Moves Player to the Left
            Player_Rect.x -= self.speed

    def MovementAndCollisionDetection(self, Player_Rect, Goal_Rect):
       #  self.GoalCollisionDetection(Player_Rect, Goal_Rect)  # Goal Collision Detection
        self.WindowCollisionDetection(Player_Rect)  # Window Collision Detection
        self.Movement(Player_Rect)  # Player Movement


Player1 = Player("Player1", pygame.image.load(os.path.join("../Assets", "Player1.png")), WindowWidth / 2.2, WindowHeight / 8.3,
                 10, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

Player2 = Player("Player2", pygame.image.load(os.path.join("../Assets", "Player2.png")), WindowWidth / 2.2, WindowHeight / 1.35,
                 10, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

Goal1 = Goal(1, pygame.image.load(os.path.join("../Assets", "Goal1.png")))
Goal2 = Goal(2, pygame.image.load(os.path.join("../Assets", "Goal2.png")))

Ball = Ball(pygame.image.load(os.path.join("../Assets", "Ball.png")))

"""
    Mid Line
"""

MidLine = MidLine(pygame.image.load(os.path.join("../Assets", "MidLine.png")))

"""
    Colours 
"""
# Colors - Color Palette: https://coolors.co/694a38-a61c3c-5b9279-3a6ea5-e9d2c0
Coffee = Color((105, 74, 56))
GrassGreen = Color((124, 252, 0))
White = Color((255, 255, 255))
QueenBlue = Color((58, 110, 165))


BX, BY = 48, 48  # X and Y Dimensions

"""
    Spawn Locations - Fix these by making them modular
"""

BallSpawnX = WindowWidth/2
BallSpawnY = WindowHeight/2


"""
    UI
"""


def UI():
    Font = pygame.font.SysFont("Century Schoolbook", 15, True, False)  # Create Font
    FontLabelA = Font.render("Score: 0", False, 1, GrassGreen.GetColor())  # Create Message
    Window.blit(FontLabelA, (0, 0))  # Draw Message at Coordinates

    FontLabelB = Font.render("Score: 0", False, 1, GrassGreen.GetColor())  # Create Message
    Window.blit(FontLabelB, (0, WindowHeight - FontLabelA.get_height()))  # Draw Message at Coordinates


"""
    Graphics
"""


def Graphics(listOfGameObjects):  # All Visuals are "drawn" here.
    Window.fill(GrassGreen.GetColor())  # Background Color

    for Rect in listOfGameObjects:
        Window.blit(Rect.image, (Rect.x, Rect.y))

    UI()  # User Interface

    # Window.blit(BallPNG, (Ball_Rect.x, Ball_Rect.y))  # Draws Ball

    pygame.display.update()  # Updates the Screen


"""
    Main Game Loop
"""


def Run():  # Basically the Unity Update Method - all code runs here (Main Game Loop).
    GameObjects = []

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    Player1_Rect = pygame.Rect(Player1.spawnX, Player1.spawnY, Player1.image.get_width(), Player1.image.get_height())
    GameObjects.append(Player1_Rect)
    Player2_Rect = pygame.Rect(Player2.spawnX, Player2.spawnY, Player2.image.get_width(), Player2.image.get_height())
    GameObjects.append(Player2_Rect)
    Goal1_Rect = pygame.Rect(WindowWidth/2.65, WindowHeight/6 * -1, Goal1.image.get_width(), Goal1.image.get_height())
    GameObjects.append(Goal1_Rect)
    Goal2_Rect = pygame.Rect(WindowWidth/2.65, WindowHeight/1.14, Goal2.image.get_width(), Goal2.image.get_height())
    GameObjects.append(Goal2_Rect)
    Ball_Rect = pygame.Rect(WindowWidth/2.15, WindowHeight/2.15, Ball.image.get_width(), Ball.image.get_height())
    GameObjects.append(Ball_Rect)
    MidLine_Rect = pygame.Rect(0, WindowHeight/2.15, MidLine.image.get_width(), MidLine.image.get_height())
    GameObjects.append(MidLine_Rect)

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Game Loop
        GameClock.tick(FPS)  # Game Runs at this FPS
        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False
        Graphics(GameObjects)

        Player1.MovementAndCollisionDetection(Player1_Rect, Goal1_Rect)
        Player2.MovementAndCollisionDetection(Player2_Rect, Goal2_Rect)

    pygame.quit()  # Quits program


"""
    Main Menu
"""


def MainMenu():
    TitleFont = pygame.font.SysFont("Century", 20, False, False)
    run = True
    while run:
        Window.fill(QueenBlue.GetColor())
        TitleLabel = TitleFont.render("Press any mouse button to begin...", False, 1, White.GetColor())
        Window.blit(TitleLabel, (WindowWidth/2 - TitleLabel.get_width()/2, WindowHeight/2 - TitleLabel.get_height()/2))
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

import pygame
import os

pygame.font.init()

"""
    Window Variables
"""

# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 400, 400

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window

# Window Name
pygame.display.set_caption("Rebound")

"""
    Classes
"""


class Ball:
    def __init__(self, image):
        self.image = image

    BallXSpeed = 2
    BallYSpeed = 2

    def Move(self, Ball_Rect):
        Ball_Rect.x += self.BallXSpeed
        Ball_Rect.y += self.BallYSpeed

class MidLine:
    def __init__(self, image):
        self.image = image


class Color:
    def __init__(self, color):  # Constructor
        self.color = color  # Tuple containing Color RGB Values

    def GetColor(self):
        return self.color


class Player:
    def __init__(self, image, spawnX, spawnY,upKey, downKey, speed):
        self.image = image
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.upKey = upKey
        self.downKey = downKey
        self.speed = speed

    CanMoveUp = True
    CanMoveDown = True

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

    def Movement(self, Player_Rect):
        GetKeyDown = pygame.key.get_pressed()  # Basically "Input.GetKeyDown" from Unity

        if GetKeyDown[self.upKey] and self.CanMoveUp:  # Moves Player Up
            Player_Rect.y -= self.speed

        if GetKeyDown[self.downKey] and self.CanMoveDown:  # Moves Player Down
            Player_Rect.y += self.speed

    def PlayerBehaviors(self, Player_Rect):
        self.Movement(Player_Rect)
        self.WindowCollisionDetection(Player_Rect)


"""
    Class Instantiations
"""

Sliver = Color((192, 192, 192))
White = Color((255, 255, 255))

Player1 = Player(pygame.image.load(os.path.join("Assets", "Player1.png")),
                 WindowWidth / 40, WindowHeight / 2.6, pygame.K_w, pygame.K_s, 5)

Player2 = Player(pygame.image.load(os.path.join("Assets", "Player2.png")),
                 WindowWidth / 1.0526, WindowHeight / 2.6, pygame.K_UP, pygame.K_DOWN, 5)

MidLine = MidLine(pygame.image.load(os.path.join("Assets", "MiddleLine.png")))

Ball = Ball(pygame.image.load(os.path.join("Assets", "Ball.png")))
"""
    Graphics
"""


def Graphics(Player1_Rect, Player2_Rect, MidLine_Rect, Ball_Rect):  # All Visuals are "drawn" here.
    Window.fill(Sliver.GetColor())  # Background Color

    Window.blit(Player1.image, (Player1_Rect.x, Player1_Rect.y))   # Draw Player 1
    Window.blit(Player2.image, (Player2_Rect.x, Player2_Rect.y))  # Draw Player 2
    Window.blit(MidLine.image, (MidLine_Rect.x, MidLine_Rect.y))  # Draw Midline
    Window.blit(Ball.image, (Ball_Rect.x, Ball_Rect.y))

    pygame.display.update()  # Updates the Screen


"""
    Main Game Loop
"""


def Run():  # Basically the Unity Update Method - all code runs here.

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    IsGameRunning = True  # If this boolean is true, then the program runs.

    Player1_Rect = pygame.Rect(Player1.spawnX, Player1.spawnY, Player1.image.get_width(), Player1.image.get_height())

    Player2_Rect = pygame.Rect(Player2.spawnX, Player2.spawnY, Player2.image.get_width(), Player2.image.get_height())

    MidLine_Rect = pygame.Rect(WindowWidth/2 - MidLine.image.get_width(), 0,  MidLine.image.get_width(), MidLine.image.get_height())

    Ball_Rect = pygame.Rect(WindowWidth/2 - Ball.image.get_width(), WindowHeight/2 - Ball.image.get_height(), Ball.image.get_width(), Ball.image.get_height())

    while IsGameRunning:  # Main Game Loop - code runs here
        GameClock.tick(FPS)  # Runs the Game at the Desired FPS

        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False

        Graphics(Player1_Rect, Player2_Rect, MidLine_Rect, Ball_Rect)

        Player1.PlayerBehaviors(Player1_Rect)
        Player2.PlayerBehaviors(Player2_Rect)
        Ball.Move(Ball_Rect)

    pygame.quit()  # Quits program


"""
    Main Menu
"""


def MainMenu():
    TitleFont = pygame.font.SysFont("Century", 20, False, False)
    run = True
    while run:
        Window.fill(Sliver.GetColor())
        TitleLabel = TitleFont.render("Press any mouse button to begin...", False, 1, Sliver.GetColor())
        Window.blit(TitleLabel,
                    (WindowWidth / 2 - TitleLabel.get_width() / 2, WindowHeight / 2 - TitleLabel.get_height() / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Game is running")
                Run()


"""
    Program Starts Here
"""
if __name__ == "__main__":  # Program Starts Here
    MainMenu()

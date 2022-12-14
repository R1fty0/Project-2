import pygame
import os
import random
# import time
pygame.font.init()  # Constructor for Fonts in Pygame

"""
    Window Variables
"""

# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 800, 800  # You can this to whatever resolution you would like, but make sure that the WindowHeight is smaller than the WindowWidth, as things otherwise do not scale well.

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window

# Window Name
pygame.display.set_caption("Rebound")

"""
    Classes
"""


"""
    ScoreBoard Class
"""

EndGame = False  # Ends the Game and loads the End Screen


class Scoreboard:
    def __init__(self, Player1Score, Player2Score, MaxScore, ScoreboardFont):  # Constructor
        self.Player1Score = Player1Score
        self.Player2Score = Player2Score
        self.MaxScore = MaxScore
        self.ScoreBoardFont = ScoreboardFont

    Player1ScoreText = "Text"  # Player 1's Score
    Player2ScoreText = "Text"  # Player 2's Score
    PlayerThatWon = 0  # Which Player won the match

    def GetPlayerThatWon(self):  # Getter
        return self.PlayerThatWon  # Returns the Player that won the match

    def UpdateScore(self):  # Updates the Score for Both Players
        self.Player1ScoreText = self.ScoreBoardFont.render(str(self.Player1Score), True, White.GetColor(), Sliver.GetColor())
        self.Player2ScoreText = self.ScoreBoardFont.render(str(self.Player2Score), True, White.GetColor(), Sliver.GetColor())

    def DrawScore(self):  # Visually updates the Score on Screen for Both Players
        Window.blit(self.Player1ScoreText, (WindowWidth/4, WindowHeight/8))
        Window.blit(self.Player2ScoreText, (WindowWidth/1.33, WindowHeight / 8))

    def ScoreKeeping(self):  # Calls both Score Management methods
        self.UpdateScore()
        self.DrawScore()

    def AddScore(self, PlayerThatScored):  # Adds a point to a player's score depending on the player that scored the point
        if PlayerThatScored == 1:
            self.Player1Score = self.Player1Score + 1
            print(str(self.Player1Score) + " point(s)")

        if PlayerThatScored == 2:
            self.Player2Score = self.Player2Score + 1
            print(str(self.Player2Score) + " point(s)")

    def MonitorScore(self):  # Checks to see if either Player has hit the maximum amount of points, and ends the game if one of them did.
        global EndGame

        if self.Player1Score >= self.MaxScore:
            self.ResetScore()
            self.PlayerThatWon = 1
            EndGame = True

        if self.Player2Score >= self.MaxScore:
            self.ResetScore()
            self.PlayerThatWon = 2
            EndGame = True

    def ResetScore(self):  # Resets the Scores of Both Players
        self.Player1Score = 0
        self.Player2Score = 0


"""
    Image Class
"""


class Image:  # Since All Sprites are Images, this helps to make images more accessible for each game object. Also enables each image to be scaled based on an X and Y divisor
    def __init__(self, image, imageXSizeDivisor, imageYSizeDivisor):  # Constructor
        self.image = image
        # Divisors are based on the game's base resolution = 400 x 400
        self.imageXSizeDivisor = imageXSizeDivisor
        self.imageYSizeDivisor = imageYSizeDivisor

    def GetImage(self):  # Returns Each Image
        return self.image

    def ScaleImage(self):  # Scales Each Image
        self.image = pygame.transform.scale(self.image, (WindowWidth/self.imageXSizeDivisor, WindowHeight/self.imageYSizeDivisor))


"""
    Ball Class
"""


class Ball(Image):
    def __init__(self, image, spawnX, spawnY, imageXSizeDivisor, imageYSizeDivisor):  # Constructor
        super().__init__(image, imageXSizeDivisor, imageYSizeDivisor)
        self.image = image
        self.spawnX = spawnX
        self.spawnY = spawnY

    xSpeed = 0  # Ball's Speed along the X-Axis
    ySpeed = 0  # Ball's Speed along the Y-Axis

    def SetStartSpeedAndDirection(self):
        Direction = random.randrange(1, 8)  # Determines a random starting direction and speed of the ball

        if Direction <= 4:
            DirectionMultiplier = 1
        else:
            DirectionMultiplier = -1

        self.xSpeed = random.randrange(1, 3) * DirectionMultiplier
        self.ySpeed = random.randrange(1, 3) * DirectionMultiplier

    def GetSpeed(self, Task):
        if Task == 1:
            return self.xSpeed
        elif Task == 2:
            return self.ySpeed

    def BallMovement(self, Ball_Rect, Players):  # Movement and Collision Detection

        # Movement
        Ball_Rect.x += self.xSpeed  # Moves Ball along the X-axis
        Ball_Rect.y += self.ySpeed  # Moves Ball along the Y-axis

        # Collision Detection
        if Ball_Rect.top <= 0 or Ball_Rect.bottom >= WindowHeight:
            self.ySpeed *= -1  # Inverts the vertical speed of the ball if it hits the top or bottom of the game window

        for GameObject in Players:
            if Ball_Rect.colliderect(GameObject):  # If the ball collides with either player, the ball's horizontal velocity is inverted
                self.xSpeed *= -1

    def BallScoreKeeping(self, Ball_Rect):  # Keeps track of the ball's position, and adds a point if a player's scores.

        if Ball_Rect.left <= 0:  # Ball has moved past the left side of the game window

            Scoreboard.AddScore(2)  # Add a point to Player 2's score

            # Resets Ball location for another round
            print("Player 2 has Scored")
            self.xSpeed = 0
            self.ySpeed = 0
            Ball_Rect.center = (float(WindowWidth) / 2, float(WindowHeight) / 2)
            self.SetStartSpeedAndDirection()

        elif Ball_Rect.right >= WindowWidth:  # Ball has moved past right side of the game window

            Scoreboard.AddScore(1)   # Add a point to Player 1's score

            # Resets Ball location for another round
            print("Player 1 has Scored")
            self.xSpeed = 0
            self.ySpeed = 0
            Ball_Rect.center = (float(WindowWidth) / 2, float(WindowHeight) / 2)
            self.SetStartSpeedAndDirection()


"""
    Color Class
"""


class Color:
    def __init__(self, color):  # Constructor
        self.color = color  # Tuple containing Color RGB Values

    def GetColor(self):  # Getter
        return self.color  # Returns the color tuple


"""
    Player Class
"""


class Player(Image):
    def __init__(self, image, spawnX, spawnY, upKey, downKey, speed, imageXSizeDivisor, imageYSizeDivisor):  # Constructor
        super().__init__(image, imageXSizeDivisor, imageYSizeDivisor)
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.upKey = upKey
        self.downKey = downKey
        self.speed = speed

    # Movement Booleans
    CanMoveUp = True  # Allows the player to move up
    CanMoveDown = True # Allows the player to move down

    def PlayerMovement(self, Player_Rect):  # Player Movement and Collision Detection

        # Checks if Player has hit Top of Window
        if Player_Rect.top <= 0:
            self.CanMoveUp = False
        elif Player_Rect.top >= 0:
            self.CanMoveUp = True

        # Checks if Player has hit the Bottom of the Window
        if Player_Rect.bottom >= WindowHeight:
            self.CanMoveDown = False
        elif Player_Rect.bottom <= WindowHeight:
            self.CanMoveDown = True

        GetKeyDown = pygame.key.get_pressed()  # An event that is triggered, a kin to the "Input.GetKey()" method from Unity (it is a method right?)

        if GetKeyDown[self.upKey] and self.CanMoveUp:  # Moves Player Up
            Player_Rect.y -= self.speed

        if GetKeyDown[self.downKey] and self.CanMoveDown:  # Moves Player Down
            Player_Rect.y += self.speed


"""
    Class Instantiations
"""
# Note = For the Players, Ball and Mid-Line, they are all scaled to match the screen size after being instantiated

# Colors
Sliver = Color((192, 192, 192))
White = Color((255, 255, 255))

# Players
Player1 = Player(pygame.image.load(os.path.join("Assets", "Player1.png")),
                 WindowWidth / 40, WindowHeight / 2.6, pygame.K_w, pygame.K_s, 5, 40, 4)
Player1.ScaleImage()

Player2 = Player(pygame.image.load(os.path.join("Assets", "Player2.png")),
                 WindowWidth / 1.0526, WindowHeight / 2.6, pygame.K_UP, pygame.K_DOWN, 5, 40, 4)
Player2.ScaleImage()

# Mid Line
MidLine = Image(pygame.image.load(os.path.join("Assets", "MiddleLine.png")), 80, 1)
MidLine.ScaleImage()

# Ball
Ball = Ball(pygame.image.load(os.path.join("Assets", "Ball.png")), WindowWidth / 2, WindowHeight / 2, 16.6, 16.6)
Ball.ScaleImage()

# Score Board
Scoreboard = Scoreboard(0, 0, 2, pygame.font.SysFont("Comic Sans", int(WindowWidth/20), False, False))

"""
    Graphics
"""


def Graphics(Player1_Rect, Player2_Rect, MidLine_Rect, Ball_Rect):  # All the Visuals seen on screen is "drawn" here
    Window.fill(Sliver.GetColor())  # Background

    Scoreboard.ScoreKeeping()  # Score Board

    Window.blit(Player1.image, (Player1_Rect.x, Player1_Rect.y))  # Player 1

    Window.blit(Player2.image, (Player2_Rect.x, Player2_Rect.y))  # Player 2

    Window.blit(MidLine.image, (MidLine_Rect.x, MidLine_Rect.y))  # Midline

    Window.blit(Ball.image, (Ball_Rect.x, Ball_Rect.y))  # Ball

    pygame.display.update()  # Updates the Screen with whatever visuals were processed in this method prior.


"""
    Main Game Loop
"""


def Run():  # Basically the Unity Update Method - all the main game logic runs here.

    # Rect = Essentially pygame's equivalent of GameObjects from Unity or Actors from Greenfoot. Rects store values are really useful for collision detection and movement

    Players = []  # List that store Players

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    IsGameRunning = True  # If this boolean is true, then the program runs.

    Player1_Rect = pygame.Rect(Player1.spawnX, Player1.spawnY, Player1.image.get_width(), Player1.image.get_height())
    Players.append(Player1_Rect)  # Creates Player 1 Rect and adds that to the list of players

    Player2_Rect = pygame.Rect(Player2.spawnX, Player2.spawnY, Player2.image.get_width(), Player2.image.get_height())
    Players.append(Player2_Rect)  # Creates Player 2 Rect and adds that to the list of players

    MidLine_Rect = pygame.Rect(WindowWidth / 2 - MidLine.image.get_width(), 0, MidLine.image.get_width(),
                               MidLine.image.get_height())  # Creates Mid-Line Rect

    Ball_Rect = pygame.Rect(WindowWidth / 2 - Ball.image.get_width(), WindowHeight / 2 - Ball.image.get_height(),
                            Ball.image.get_width(), Ball.image.get_height())  # Creates Ball Rect

    Ball.SetStartSpeedAndDirection()  # Generates a starting speed and direction for the ball when the game initally begins

    global EndGame

    while IsGameRunning:  # Main Game Loop - code runs here
        GameClock.tick(FPS)  # Runs the Game at the Desired FPS

        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
            elif EndGame:  # Ends the game if one of the players have scored the max amount of points
                IsGameRunning = False
                # time.sleep(2)

        Graphics(Player1_Rect, Player2_Rect, MidLine_Rect, Ball_Rect)  # Drawing Visuals

        Player1.PlayerMovement(Player1_Rect)  # Player 1 Movement and Collision Detection
        Player2.PlayerMovement(Player2_Rect)  # Player 2 Movement and Collision Detection

        Ball.BallMovement(Ball_Rect, Players)  # Ball Movement and Collision Detection
        Ball.BallScoreKeeping(Ball_Rect)  # Ball Score Keeping

        Scoreboard.MonitorScore()  # Scoreboard Score Keeping

    EndGame = False


"""
    End Game Screen    
"""


def EndGameScreen(PlayerThatWon):
    # Create Fonts for UI
    WinnerFont = pygame.font.SysFont("Century Gothic", int(WindowWidth / 20), True, False)
    PromptFont = pygame.font.SysFont("Comic Sans MS", int(WindowHeight / 27), False, False)

    ScreenIsRunning = True
    while ScreenIsRunning:

        Window.fill(Sliver.GetColor())  # Background Color

        # Create Text for UI
        PromptLabel = PromptFont.render("Press any mouse button to continue!", True, 1, Sliver.GetColor())
        WinnerLabel = "none"

        if PlayerThatWon == 1:
            WinnerLabel = WinnerFont.render("Player 1 Won the Match!", True, 1, Sliver.GetColor())
        elif PlayerThatWon == 2:
            WinnerLabel = WinnerFont.render("Player 2 Won the Match!", True, 1, Sliver.GetColor())

        # Display UI on Screen
        Window.blit(PromptLabel,
                    (WindowWidth / 2 - PromptLabel.get_width() / 2, WindowHeight / 2 - PromptLabel.get_height() / 2))

        Window.blit(WinnerLabel,
                    (WindowWidth / 2 - WinnerLabel.get_width() / 2, WindowHeight / 4 - WinnerLabel.get_height() / 2))

        pygame.display.update()  # Updates the Screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exits the Application
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Returns to Main Menu
                ScreenIsRunning = False


"""
    Main Menu
"""


def MainMenu():
    # Create Fonts for UI
    TitleFont = pygame.font.SysFont("Century Gothic", int(WindowWidth/20), True, False)
    PromptFont = pygame.font.SysFont("Comic Sans MS", int(WindowHeight/27), False, False)
    MadeByFont = pygame.font.SysFont("Century Gothic", int(WindowWidth/40), False, False)

    MenuIsRunning = True
    while MenuIsRunning:

        Window.fill(Sliver.GetColor())

        # Create Text for UI
        TitleLabel = TitleFont.render("Rebound", False, 1, Sliver.GetColor())
        PromptLabel = PromptFont.render("Press any mouse button to begin!", False, 1, Sliver.GetColor())
        MadeByLabel = MadeByFont.render("Made by Mohit Sah.", False, 1, Sliver.GetColor())

        # Display UI Text on Screen
        Window.blit(PromptLabel,
                    (WindowWidth / 2 - PromptLabel.get_width() / 2, WindowHeight / 2 - PromptLabel.get_height() / 2))
        Window.blit(TitleLabel,
                    (WindowWidth / 2 - TitleLabel.get_width() / 2, WindowHeight / 4 - TitleLabel.get_height() / 2))
        Window.blit(MadeByLabel,
                    (WindowWidth / 2 - MadeByLabel.get_width() / 2, WindowHeight / 1.09 - MadeByLabel.get_height() / 2))

        pygame.display.update()  # Updates the Screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exits the Application
                MenuIsRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Runs the game if the user clicks any of the mouse buttons
                Run()  # Main Game
                EndGameScreen(Scoreboard.GetPlayerThatWon())  # End Screen

    pygame.quit()  # Quits the Application


"""
    Program Start
"""
if __name__ == "__main__":  # Program Starts Here
    MainMenu()

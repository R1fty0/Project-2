import pygame
import os
import random
# import time
pygame.font.init()  # Constructor for Fonts in Pygame

"""
    Window Variables
"""

# Frames Per Second
FPS = 60  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 1000, 700   # You can this to whatever resolution you would like, but make sure that the WindowHeight is smaller than the WindowWidth, as things otherwise do not scale well.

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # Tuple is the dimensions for Width & Height of Window

# Window Name
pygame.display.set_caption("Rebound V1.2")

"""
    Classes
"""


"""
    ScoreBoard Class
"""

EndGame = False  # Ends the Game and loads the End Screen


class Scoreboard:
    def __init__(self, Player1Score, Player2Score, MaxScore, ScoreboardFont):  # Constructor
        """ Create a scoreboard that keeps track of the scores of both players. """
        self.Player1Score = Player1Score
        self.Player2Score = Player2Score
        self.MaxScore = MaxScore
        self.ScoreBoardFont = ScoreboardFont

    Player1ScoreText = "Text"  # Player 1's Score
    Player2ScoreText = "Text"  # Player 2's Score
    PlayerThatWon = 0  # Which Player won the match

    def determine_which_player_won(self):  # Getter
        """ Returns which player won the match."""
        return self.PlayerThatWon  # Returns the Player that won the match

    def update_score(self):
        """ Updates the  score of both players."""
        self.Player1ScoreText = self.ScoreBoardFont.render(str(self.Player1Score), True, White.get_color(), Sliver.get_color())
        self.Player2ScoreText = self.ScoreBoardFont.render(str(self.Player2Score), True, White.get_color(), Sliver.get_color())

    def draw_score(self):  # Visually updates the Score on Screen for Both Players
        """ Displays the score of both players on screen.  """
        Window.blit(self.Player1ScoreText, (WindowWidth/4, WindowHeight/8))
        Window.blit(self.Player2ScoreText, (WindowWidth/1.33, WindowHeight / 8))

    def score_keeping(self):  # Calls both Score Management methods
        """ Calls all relevant methods for score keeping."""
        self.update_score()
        self.draw_score()

    def add_score(self, PlayerThatScored):
        """ Adds a point to a player's score depending on the player that scored.  """
        if PlayerThatScored == 1:
            self.Player1Score = self.Player1Score + 1
            print(str(self.Player1Score) + " point(s)")

        if PlayerThatScored == 2:
            self.Player2Score = self.Player2Score + 1
            print(str(self.Player2Score) + " point(s)")

    def monitor_score(self):
        """ Checks to see if either Player has hit the maximum amount of points, and ends the game if one of them did. """
        global EndGame

        if self.Player1Score >= self.MaxScore:
            self.reset_score()
            self.PlayerThatWon = 1
            EndGame = True

        if self.Player2Score >= self.MaxScore:
            self.reset_score()
            self.PlayerThatWon = 2
            EndGame = True

    def reset_score(self):
        """  Resets the scores of both players. """
        self.Player1Score = 0
        self.Player2Score = 0


"""
    Image Class
"""


class Image:  # Since All Sprites are Images, this helps to make images more accessible for each game object. Also enables each image to be scaled based on an X and Y divisor
    def __init__(self, image, imageXSizeDivisor, imageYSizeDivisor):  # Constructor
        """ Class that contains all relevant parameters required to create an image. """
        self.image = image
        # Divisors are based on the game's base resolution = 400 x 400
        self.imageXSizeDivisor = imageXSizeDivisor
        self.imageYSizeDivisor = imageYSizeDivisor

    def get_image(self):
        """ Returns an image upon request. """
        return self.image

    def scale_image(self):
        """ Scales an image upon request. """
        self.image = pygame.transform.scale(self.image, (WindowWidth/self.imageXSizeDivisor, WindowHeight/self.imageYSizeDivisor))


"""
    Ball Class
"""


class Ball(Image):
    def __init__(self, image, spawnX, spawnY, imageXSizeDivisor, imageYSizeDivisor, minBallSpeed, maxBallSpeed):  # Constructor
        """ Contains all necessary logic for a working ball that can bounce off walls. """
        super().__init__(image, imageXSizeDivisor, imageYSizeDivisor)
        self.image = image
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.minBallSpeed = minBallSpeed
        self.maxBallSpeed = maxBallSpeed

    xSpeed = 0  # Ball's Speed along the X-Axis
    ySpeed = 0  # Ball's Speed along the Y-Axis

    def set_starting_parameters(self):
        """ Determines a random starting direction and speed of the ball. """
        Direction = random.randrange(self.minBallSpeed, self.maxBallSpeed)

        if Direction <= self.minBallSpeed:
            DirectionMultiplier = 1
        else:
            DirectionMultiplier = -1

        self.xSpeed = random.randrange(self.minBallSpeed, self.maxBallSpeed) * DirectionMultiplier
        print(self.xSpeed)
        self.ySpeed = random.randrange(self.minBallSpeed, self.maxBallSpeed) * DirectionMultiplier
        print(self.ySpeed)

    def get_ball_speed(self, Task):
        if Task == 1:
            return self.xSpeed
        elif Task == 2:
            return self.ySpeed

    def movement(self, Ball_Rect, Players):
        """ Handles the ball's movement and collision detection. """

        # Movement
        Ball_Rect.x += self.xSpeed  # Moves Ball along the X-axis
        Ball_Rect.y += self.ySpeed  # Moves Ball along the Y-axis

        # Collision Detection
        if Ball_Rect.top <= 0 or Ball_Rect.bottom >= WindowHeight:
            self.ySpeed *= -1.1
            print(self.ySpeed)  # Inverts the vertical speed of the ball if it hits the top or bottom of the game window

        for GameObject in Players:
            if Ball_Rect.colliderect(GameObject):  # If the ball collides with either player, the ball's horizontal velocity is inverted
                self.xSpeed *= -1.1
                print(self.xSpeed)

    def ball_score_keeping(self, Ball_Rect):
        """ Keeps track of the ball's position, and adds a point if a player's scores. """

        if Ball_Rect.left <= 0:  # Ball has moved past the left side of the game window

            Scoreboard.add_score(2)  # Add a point to Player 2's score

            # Resets Ball location for another round
            print("Player 2 has Scored")
            self.xSpeed = 0
            self.ySpeed = 0
            Ball_Rect.center = (float(WindowWidth) / 2, float(WindowHeight) / 2)
            self.set_starting_parameters()

        elif Ball_Rect.right >= WindowWidth:  # Ball has moved past right side of the game window

            Scoreboard.add_score(1)   # Add a point to Player 1's score

            # Resets Ball location for another round
            print("Player 1 has Scored")
            self.xSpeed = 0
            self.ySpeed = 0
            Ball_Rect.center = (float(WindowWidth) / 2, float(WindowHeight) / 2)
            self.set_starting_parameters()


"""
    Color Class
"""


class Color:
    def __init__(self, color):  # Constructor
        """ Create a color based off of 3 values (Red, Green, Blue). """
        self.color = color  # Tuple containing Color RGB Values

    def get_color(self):  # Getter
        """ Returns a color upon request. """
        return self.color  # Returns the color tuple


"""
    Player Class
"""


class Player(Image):
    def __init__(self, image, spawnX, spawnY, upKey, downKey, speed, imageXSizeDivisor, imageYSizeDivisor):  # Constructor
        """ Creates a player that can move vertically across the screen and can interact with the game world."""
        super().__init__(image, imageXSizeDivisor, imageYSizeDivisor)
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.upKey = upKey
        self.downKey = downKey
        self.speed = speed

    # Movement Booleans
    CanMoveUp = True  # Allows the player to move up
    CanMoveDown = True   # Allows the player to move down

    def movement(self, Player_Rect):
        """ Handles Player movement and collision detection. """

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

        GetKeyDown = pygame.key.get_pressed()  # An event that is triggered, akin to the "Input.GetKey()" method from Unity (it is a method right?)

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
                 WindowWidth / 40, WindowHeight / 2.6, pygame.K_w, pygame.K_s, 8, 40, 4)
Player1.scale_image()

Player2 = Player(pygame.image.load(os.path.join("Assets", "Player2.png")),
                 WindowWidth / 1.0526, WindowHeight / 2.6, pygame.K_UP, pygame.K_DOWN, 8, 40, 4)
Player2.scale_image()

# Mid Line
MidLine = Image(pygame.image.load(os.path.join("Assets", "MiddleLine.png")), 80, 1)
MidLine.scale_image()

# Ball
Ball = Ball(pygame.image.load(os.path.join("Assets", "Ball.png")), WindowWidth / 2, WindowHeight / 2, 16.6, 16.6, 2, 3)
Ball.scale_image()

# Score Board
Scoreboard = Scoreboard(0, 0, 5, pygame.font.SysFont("Comic Sans", int(WindowWidth/20), False, False))

"""
    Graphics
"""


def Graphics(Player1_Rect, Player2_Rect, MidLine_Rect, Ball_Rect):  # All the Visuals seen on screen is "drawn" here
    Window.fill(Sliver.get_color())  # Background

    Scoreboard.score_keeping()  # Score Board

    Window.blit(Player1.image, (Player1_Rect.x, Player1_Rect.y))  # Player 1

    Window.blit(Player2.image, (Player2_Rect.x, Player2_Rect.y))  # Player 2

    Window.blit(MidLine.image, (MidLine_Rect.x, MidLine_Rect.y))  # Midline

    Window.blit(Ball.image, (Ball_Rect.x, Ball_Rect.y))  # Ball

    pygame.display.update()  # Updates the Screen with whatever visuals were processed in this method prior.


"""
    Main Game Loop
"""


def Run():  # Basically the Unity Update Method - all the main game logic runs here.
    """ The core game loop. All actions that happen in the game occur in this function. """

    # Rect = Essentially pygame's equivalent of GameObjects from Unity or Actors from Greenfoot. A rect stores values are really useful for collision detection and movement

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

    Ball.set_starting_parameters()  # Generates a starting speed and direction for the ball when the game initially begins

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

        Player1.movement(Player1_Rect)  # Player 1 Movement and Collision Detection
        Player2.movement(Player2_Rect)  # Player 2 Movement and Collision Detection

        Ball.movement(Ball_Rect, Players)  # Ball Movement and Collision Detection
        Ball.ball_score_keeping(Ball_Rect)  # Ball Score Keeping

        Scoreboard.monitor_score()  # Scoreboard Score Keeping

    EndGame = False


"""
    End Game Screen    
"""


def EndGameScreen(PlayerThatWon):
    """ Creates the visuals for the Game Over screen, which displays which player won and instructions on what to do next. """
    # Create Fonts for UI
    WinnerFont = pygame.font.SysFont("Century Gothic", int(WindowWidth / 20), True, False)
    PromptFont = pygame.font.SysFont("Comic Sans MS", int(WindowHeight / 27), False, False)

    ScreenIsRunning = True
    while ScreenIsRunning:

        Window.fill(Sliver.get_color())  # Background Color

        # Create Text for UI
        PromptLabel = PromptFont.render("Press any mouse button to continue!", True, 1, Sliver.get_color())
        WinnerLabel = "none"

        if PlayerThatWon == 1:
            WinnerLabel = WinnerFont.render("Player 1 Won the Match!", True, 1, Sliver.get_color())
        elif PlayerThatWon == 2:
            WinnerLabel = WinnerFont.render("Player 2 Won the Match!", True, 1, Sliver.get_color())

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
    """ Create a main menu screen with a title, instructions and the name of the author."""

    # Create Fonts for UI
    TitleFont = pygame.font.SysFont("Century Gothic", int(WindowWidth/20), True, False)
    PromptFont = pygame.font.SysFont("Comic Sans MS", int(WindowHeight/27), False, False)
    MadeByFont = pygame.font.SysFont("Century Gothic", int(WindowWidth/40), False, False)

    MenuIsRunning = True
    while MenuIsRunning:

        Window.fill(Sliver.get_color())

        # Create Text for UI
        TitleLabel = TitleFont.render("Rebound", False, 1, Sliver.get_color())
        PromptLabel = PromptFont.render("Press any mouse button to begin!", False, 1, Sliver.get_color())
        MadeByLabel = MadeByFont.render("Made by Mohit Sah.", False, 1, Sliver.get_color())

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
                EndGameScreen(Scoreboard.determine_which_player_won())  # End Screen

    pygame.quit()  # Quits the Application


"""
    Program Start
"""
if __name__ == "__main__":  # Program Starts Here
    MainMenu()

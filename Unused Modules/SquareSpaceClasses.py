import pygame
import os


class Objects():
    def __init__(self, speed):
        self.speed = speed

    def AddToGame(self, window):  # Adds Object to Window
        window.blit(self.image, (self.x, self.y))

    def Move(self, speed):
        self.y += speed


class Square(Objects):
    super().__init__()


class Circle(Objects):
    super().__init__()

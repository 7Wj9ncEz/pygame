import pygame
class Player:

    def __init__(self, left, top, width, height, movespeed):
        self.rectangle = pygame.Rect(left, top, width, height)
        self.movespeed = movespeed

    def move(self, directions):
        if directions["hor"]:
            if directions["hor"] == "left":
                self.rectangle.left -= self.movespeed

            if directions["hor"] == "right":
                self.rectangle.left +=self.movespeed

        if directions["ver"]:
            if directions["ver"] == "up":
                self.rectangle.top -= self.movespeed

            if directions["ver"] == "down":
                self.rectangle.top += self.movespeed



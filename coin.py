import pygame
import pygame.draw
class Coin:
    def __init__(self, x, y, xpos, ypos, draw):
        self.Surf = pygame.Surface((x,y))
        self.Rect = pygame.Rect(xpos,ypos,x,y)
        self.Color = "#b89d04"
        self.Draw = draw
    def SelfRet(self):
        return self

k = Coin.SelfRet
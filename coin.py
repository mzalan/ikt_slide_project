import pygame
from Globals import *
class Coin:
    def __init__(self, x, y, xpos, ypos, draw):
        self.Surf = pygame.Surface((180,180))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(r.coin_img, (width*0.1, height*0.1))
        self.Rect = self.Surf.get_rect(center=(xpos,ypos))
        self.Color = "#b89d04"
        self.Draw = draw
    def SelfRet(self):
        return self

k = Coin.SelfRet
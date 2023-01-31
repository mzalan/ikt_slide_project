import pygame
import pygame.draw
class Coin:
    def __init__(self, x, y, xpos, ypos, draw):
        self.Surf = pygame.Surface((x,y))
        self.Rect = self.Surf.get_rect(center=(xpos,ypos))
        self.Color = "#b89d04"
        self.Draw = True
    def SelfRet(self):
        return self

k = Coin.SelfRet
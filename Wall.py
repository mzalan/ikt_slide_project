import pygame

class Wall:
    def __init__(self, x, y, xpos, ypos, draw):
        self.Surf = pygame.Surface((x,y))
        self.Rect = self.Surf.get_rect(center=(xpos,ypos))
        self.Color = "#100133"
        self.Draw = False
    def SelfRet(self):
        return self

w = Wall.SelfRet
        
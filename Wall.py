import pygame

class Wall:
    def __init__(self, x, y, xpos, ypos, color):
        self.Surf = pygame.Surface((x,y))
        self.Rect = self.Surf.get_rect(center=(xpos,ypos))
        self.Color = color
    def SelfRet(self):
        return self
        
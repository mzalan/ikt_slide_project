import pygame
from Globals import *

class Wall:
    def __init__(self,xpos, ypos):
        self.Surf = pygame.Surface((100,100))
        self.Rect = self.Surf.get_rect(center=(xpos,ypos))
        self.Color = "#100133"

    def SelfRet(self):
        return self

    def Render(self, _id):
        self.Surf.fill(self.Color)
        r.screen.blit(self.Surf, self.Rect)

    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            r.Run = False
        
    
w = Wall.SelfRet
        
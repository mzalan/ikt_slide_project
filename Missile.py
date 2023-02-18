import pygame
import os
from Globals import *

img = pygame.image.load(os.path.join('assets', 'missile.png'))

class Missile:
    global speed
    speed = 0
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((100,160))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        # self.speed = 3

        self.Surf2 = pygame.Surface((120,1180))
        self.Surf2.fill("#fa5a39")

    def Render(self, _id):
        global speed
        if r.runs - r.objects[_id][4] > 100:
            speed = 4
            r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))
        elif r.runs - r.objects[_id][4] > 300:
            speed = 0
        else:
            r.screen.blit(self.Surf2,(r.objects[_id][1],r.objects[_id][2]))
        
    
    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            r.Run = 2
            
    def Speed():
        return speed
import pygame
from Globals import *
from MagnetActivation import *

img = pygame.image.load(os.path.join('assets', 'magnet.png'))

class Magnet:
    def __init__(self,xpos, ypos):
        self.Surf = pygame.Surface((135,135))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 1

    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))

    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            r.objects[_id][3] = False
            r.magnet_start = r.runs
            MagnetActivation()


    
    def Speed(self, _id):
        return self.speed

import pygame
from Globals import *
from PowerupActivation import *

img = pygame.image.load(os.path.join('assets', 'bullet.png'))

class Bullet:
    def __init__(self,xpos, ypos):
        self.Surf = pygame.Surface((45,70))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = -8

    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))

    def Collide(self, _id):
        pass
                
    def Speed(self, _id):
        return self.speed
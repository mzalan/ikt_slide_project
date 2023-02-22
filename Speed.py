import pygame
import pygame.draw
from Globals import *

img = pygame.image.load(os.path.join('assets', 'speed.png'))

class Speed:
    global speed
    speed = 1
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((130,190))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 1

    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))
    
    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            r.speed *= 3   
    def Speed(self, _id):
        return self.speed

            
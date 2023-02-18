import pygame
import pygame.draw
from Globals import *

img = pygame.image.load(os.path.join('assets', 'coin.png'))

class Coin:
    global speed
    speed = 1
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((86.4,86.4))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 1

    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))
    
    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            if r.objects[_id][3]:
                r.Coins += 1
            r.objects[_id][3] = False
    
    def Speed():
        return speed

            



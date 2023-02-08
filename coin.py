import pygame
from Globals import *

coin_img = pygame.image.load(os.path.join('images', 'coin.png'))

class Coin:
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((180,180))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(coin_img, (width*0.3, height*0.3))
        self.Rect = self.Surf.get_rect(center=(xpos,ypos))
        self.Color = "#b89d04"
    def SelfRet(self):
        return self

    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))
    
    def Collide(self):
        if self.Rect.colliderect(r.player_rect):
            r.Run = False



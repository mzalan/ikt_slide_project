import pygame
from Globals import *
from StartGame import *
from Turret import *

img = pygame.image.load(os.path.join('assets', 'wall.png'))

class Wall:
    def __init__(self,xpos, ypos):
        self.Surf = pygame.Surface((100,100))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 1

    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))

    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect) and r.objects[_id][3]:
            for i in range(len(r.powerups)):
                if r.powerups[i][0] == 1 or r.powerups[i][0] == 2:
                    r.objects[_id][3] = False
                    return [i, r.powerups[i][0]] 
            else:
                r.Run = 2
                
        for i in range(list(r.objects.keys())[0], r.objCount):

            try:
                if r.objects[i][0] == 10:
                    if self.Rect.colliderect(Laser(r.objects[i][1], r.objects[i][2]).Rect):  
                        r.objects[_id][3] = False
            except:
                pass

    
    def Speed(self, _id):
        return self.speed

        
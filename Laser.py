import pygame
from Globals import *
from PowerupActivation import *

img = pygame.image.load(os.path.join('assets', 'laser.png'))

class Laser:
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
            r.objects[_id][3] = False
            p = 3

            for i in range(len(r.powerups)):
                if p in r.powerups[i]:
                    if r.runs - r.powerups[i][1] < r.power_upgrades[r.powerups[i][0]]:
                        r.powerups[i] = [p, r.runs, r.powerup_img[p]]
                        break
                    else:
                        del r.powerups[i]
            else:
                r.powerups.append([p, r.runs, r.powerup_img[p]]) 
                

    def Speed(self, _id):
        return self.speed
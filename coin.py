import pygame
import pygame.draw
from Globals import *
from Wall import *
from Bouncepad import *

img = pygame.image.load(os.path.join('assets', 'coin.png'))

class Coin:
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((86.4,86.4))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 1

    def Render(self, _id):
        for i in range(len(r.powerups)):
            if r.powerups[i][0] == 0:
                if r.runs - r.powerups[i][1] < r.power_upgrades[r.powerups[i][0]]:
                    r.objects[_id][2] += 14
                    if abs(r.objects[_id][1] - r.player_rect.x) > r.diff:
                        try:
                            r.objects[_id][1] += (r.player_rect.x - self.Rect.x)/((r.player_rect.y - self.Rect.y)/(r.diff * 2))
                        except:
                            pass
                elif abs(r.objects[_id][1] - r.player_rect.x) <= r.diff:
                    r.objects[_id][1] = r.player_rect.x
                break
  
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))

    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            if r.objects[_id][3]:
                r.gamecoins += 1
            r.objects[_id][3] = False

        d = True
        for i in range(len(r.powerups)):
            if r.powerups[i][0] == 0:
                d = False
                break
        for i in range(list(r.objects.keys())[0], r.objCount):

            try:
                if (r.objects[i][0] == 5 or r.objects[i][0] == 6) and d:
                    if self.Rect.colliderect(Wall(r.objects[i][1], r.objects[i][2]).Rect) or self.Rect.colliderect(Bouncepad(r.objects[i][1], r.objects[i][2]).Rect):  
                        r.objects[_id][3] = False
                        
            except:
                pass
    
    def Speed(self, _id):
        return self.speed

            






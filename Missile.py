import pygame
import os
from Globals import *
from Turret import *

img = pygame.image.load(os.path.join('assets', 'missile.png'))
w1 = pygame.image.load(os.path.join('assets', 'warning.png'))
w2 = pygame.image.load(os.path.join('assets', 'warning2.png'))

low = [67, 78, 89]
high = [75, 86, 97]

class Missile:
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((100,160))
        surfx = self.Surf.get_rect().width
        surfy = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (surfx, surfy))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 0
        self.Surf2 = pygame.Surface((100,180))

        self.warnsurf = pygame.Surface((80, 63))
        warnx = self.warnsurf.get_rect().width
        warny = self.warnsurf.get_rect().height
        self.warn1 = pygame.transform.scale(w1, (warnx, warny))
        self.warn2 = pygame.transform.scale(w2, (warnx, warny))

        self.set_warn = self.warn1
        self.Surf2.fill("#d41c04")

    def Render(self, _id):
        rel_runs = r.runs - r.objects[_id][4]

        if rel_runs > 100:
            r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))
        elif r.runs - r.objects[_id][4] > 300:
            self.speed = 0
        else:
            if rel_runs < 68:
                if r.objects[_id][1] < r.player_rect.x:
                    a = 1
                else:
                    a = -1
                if abs(r.objects[_id][1] - r.player_rect.x) > r.diff:
                    r.objects[_id][1] += r.diff * a


            for l in zip(low, high):
                if rel_runs > l[0] and rel_runs < l[1]:
                    self.Surf2.fill("#ffd52b")
                    self.set_warn = self.warn2
            r.screen.blit(self.Surf2,(r.objects[_id][1],r.objects[_id][2]))
            r.screen.blit(self.set_warn,(r.objects[_id][1] + 10,r.objects[_id][2] + 108))
        
    
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
        if r.runs - r.objects[_id][4] > 100:
            self.speed = 7
        else:
            self.speed = 0
        return self.speed
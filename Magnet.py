import pygame
from Globals import *
from PowerupActivation import *

img = pygame.image.load(os.path.join('assets', 'magnet1.png'))

class Magnet:
    def __init__(self,xpos, ypos):
        self.Surf = pygame.Surface((80,80))
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
            r.powerups[0] = [r.runs, 0]
            print(f"Collision assignment magnet: {r.powerups}")


            drawables = 0
            pos = 0
            for i in range(len(r.powerups)):
                if r.runs - r.powerups[i][0] < 1000:
                    drawables += 1
                    if drawables == 1:
                        pos = 0
                    if drawables == 2:
                        pos = 1570
            PowerupActivation(r.powerup_img[0], 0, pos)



            


    
    def Speed(self, _id):
        return self.speed

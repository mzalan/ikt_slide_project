import pygame
import pygame.draw
from Globals import *
from playermoving import *

img = pygame.image.load(os.path.join('assets', 'trampoline.png'))

class Bouncepad:
    def __init__(self, xpos, ypos):
        self.Surf = pygame.Surface((70,180))
        width = self.Surf.get_rect().width
        height = self.Surf.get_rect().height
        self.Surf = pygame.transform.scale(img, (width, height))
        self.Rect = self.Surf.get_rect(topleft=(xpos,ypos))
        self.speed = 1
    def Render(self, _id):
        r.screen.blit(self.Surf,(r.objects[_id][1],r.objects[_id][2]))
    
    def Collide(self, _id):
        if self.Rect.colliderect(r.player_rect):
            if abs(r.player_rect.y - self.Rect.y) <= 180 - r.diff and r.elapsed == 0:

                if self.Rect.x < r.player_rect.x:
                    r.bounce_data = [1, 1820, r.speed*3]
                    
                else:
                    r.bounce_data = [-1, 0, r.speed*3]

            elif abs(r.player_rect.y - self.Rect.y) > 180 - r.diff:
                r.Run = 2
            else:
                r.elapsed = 0
                r.bounce_data[0] *= -1
                r.bounce_data[1] += 1820 * r.bounce_data[0]

    def Speed(self, _id):
        return self.speed

                
    
    
    
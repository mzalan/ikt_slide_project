import pygame
pygame.init()

class Globals:

    def __init__(self):
            
        self.screen = pygame.display.set_mode((1920,1080))

        self.clock = pygame.time.Clock()


        self.player = pygame.Surface((100,100))

        self.player_rect = self.player.get_rect(center=(960,930))

        self.speed_font = pygame.font.Font(None, 50)
        self.gover_font = pygame.font.Font(None, 120)
        self.leftRight = [False,False] #bal gomb - jobb gomb booleanok. keydown -> true, keyup -> false mindkét bool esetén.
        self.moveD = False #ha true, bal volt legutóbb lenyomva, ha false akkor jobb. keyupok esetén értékcsere (pl ha jobbot elengeded, falseról truera vált).
        self.speed = 11 #alapértelmezett sebesség, mindig a boost változó értékével növelődik, ha mindkét iránygomb el van engedve akkor resetelődik
        self.boost = 0.5 #alapértelmezett gyorsítási ráta, ez nullázódik majd fokozatosan 0.5-ig növekszik, ha a boosting bool true
        self.boosting = False #ha a leftRightban mindkét bool true, akkor ez is true
        self.speedCap = 38 #maxsebesség (pixel/frame)
        self.speedFloor = 11#minimumsebesség (pixel/frame)

        
    def SelfRet(self):
        return self

r = Globals.SelfRet(Globals())
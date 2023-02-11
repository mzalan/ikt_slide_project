import pygame
import random
import os

pygame.init()


class Globals:

    def __init__(self):
            
        self.screen = pygame.display.set_mode((1920,1080))

        self.clock = pygame.time.Clock()


        self.player = pygame.Surface((100,100))

        self.player_rect = self.player.get_rect(center=(960,930))

        self.font_family = os.path.join("assets", "pixel.ttf")

        self.small_font = pygame.font.Font(self.font_family, 35)
        self.first_font = pygame.font.Font(self.font_family, 55)
        self.gover_font = pygame.font.Font(self.font_family, 120)
        self.score_font = pygame.font.Font(self.font_family, 80) 
        #self.large_font = pygame.font.Font(self.font_family, 150)

        self.leftRight = [False,False] #bal gomb - jobb gomb booleanok. keydown -> true, keyup -> false mindkét bool esetén.
        self.moveD = False #ha true, bal volt legutóbb lenyomva, ha false akkor jobb. keyupok esetén értékcsere (pl ha jobbot elengeded, falseról truera vált).
        self.speed = 11 #alapértelmezett sebesség, mindig a boost változó értékével növelődik, ha mindkét iránygomb el van engedve akkor resetelődik
        self.boost = 0.5 #alapértelmezett gyorsítási ráta, ez nullázódik majd fokozatosan 0.5-ig növekszik, ha a boosting bool true
        self.boosting = False #ha a leftRightban mindkét bool true, akkor ez is true
        self.speedCap = 38 #maxsebesség (pixel/frame)
        self.speedFloor = 11#minimumsebesség (pixel/frame)
        

        self.objects = {}
        self.spawnPoint = -100

        self.objects[0] = [random.randint(1,2), random.randint(100,1800), self.spawnPoint, True] #objects dictionary: az azonosító a key (0-tól végtelenig)
    #                                                                    értéklista 0.eleme a renderelések száma, 1. az xpozíció, 2. az y pozíció 
        self.diff = 5
        self.diffCap = 40
        self.Run = True
        self.Points = 0
        self.Best = 0

        self.Coins = 0
        self.elapsed = 0
        self.bounce_data = None
        # self.coin_rect = [85, 85, random.randint(100,1800), -100]

    def SelfRet(self):
        return self


r = Globals.SelfRet(Globals())
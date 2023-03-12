import pygame
import random
import os

pygame.init()


class Globals:

    def __init__(self):
            
        self.screen = pygame.display.set_mode((1920,1080))

        self.clock = pygame.time.Clock()


        self.player = pygame.Surface((90,90))

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

        self.obj_type = 9
        self.objects[-1] = [1, random.randint(100,1800), self.spawnPoint, False] #objects dictionary: az azonosító a key (0-tól végtelenig)
    #                                                                    értéklista 0.eleme a renderelések száma, 1. az xpozíció, 2. az y pozíció 
        self.diff = 6.5
        self.diffCap = 23
        self.Points = 0
        self.Best = 0

        self.Run = 0 #értéke megmutatja, hogy melyik felületre kell váltani 0 - menu, 1 - játék, 2 - game over, 3 - upgrades

        self.Coins = 0
        self.elapsed = 0
        self.bounce_data = None

        self.objCount = 1
        self.click = False
        self.runs = 0


        self.powerup_img = [pygame.image.load(os.path.join('assets', 'magnet.png')), pygame.image.load(os.path.join('assets', 'shield.png')), pygame.image.load(os.path.join('assets', 'speed.png')), pygame.image.load(os.path.join('assets', 'laser.png'))]
        self.powerups = []
        self.power_upgrades = []
        self.default_upgrades = [1000, 1000, 200, 1200]
        
        self.setCap = True

        self.ammo = 4

        self.ratext = False

        self.blacklist = []

        self.beolvasottadatok = []

        self.arak = [20,50,140,260,480, "MAX LEVEL!"]

        self.gamecoins = 0

        self.wallSection = 0 # 0 inaktív, 1 - aktiváció, falszekció tulajdonságainak meghatározása, 2 - aktiválva
        self.wsdata = [None, None, None] # 0 - távolság a sorok között, 1 - sorok száma, 2 - r.runs upon aktiválás

        self.coingen = None
        self.coinx = None
        self.cpattern = None # 0 - egyenes, 1 - ferdebal, 2 - ferdejobb, 3 - zigzag

        self.tgen = None
        self.tdx = None
        self.tb = None

        self.distance = random.randint(18,42)

        self.dead = False

    def SelfRet(self):
        return self


r = Globals.SelfRet(Globals())
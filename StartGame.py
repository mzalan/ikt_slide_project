from Globals import *

def StartGame():
    if r.Points > r.Best:
        r.Best = r.Points
    r.Run = 1
    r.diff = 6.5
    r.objCount = 0
    r.objects = {}
    r.objects[-1] = [1, random.randint(100,1800), r.spawnPoint, False]
    r.runs = 0
    r.Points = 0
    r.Coins = 0
    r.bounce_data = None
    r.player_rect.x = 960
    r.elapsed = 0
    r.protected = False
    r.powerups = []
    r.setCap = True

def ShieldGame():
    r.bounce_data = None
    r.elapsed = 0
    r.objCount = 0
    r.objects = {}
    r.protected = False



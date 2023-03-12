from Globals import *
import math
from Render import *
from coin import *
from Bouncepad import *
from Missile import *
from Magnet import *
from Shield import *
from Turbo import *
from Turret import *
from Bullet import *

def Generating(op):
    if op == 0:
        if random.randint(1,24) == 1 and r.wallSection == 0 and r.tgen == None:
            WallSection()
        else:
            if random.randint(1,15) == 1 and r.wallSection == 0:
                r.objects[max(r.objects.keys())+1] = [3, random.randint(0,1833), -100, True]
                r.objCount += 1
            if random.randint(1,3) == 1 and r.wallSection == 0:
                WallGen()
            elif random.randint(1,10) == 1 and r.wallSection == 0:
                BpadSection()
            if random.randint(1,5) == 1 and r.wallSection == 0:
                CoinGen()
            if random.randint(1,25) == 1 and r.wallSection == 0:
                rp = random.randint(1,4)
                if rp == 1:
                    rp = 2
                elif rp == 2:
                    rp = 4
                elif rp == 3:
                    rp = 7
                else:
                    rp = 8
                r.objects[max(r.objects.keys())+1] = [rp, random.randint(0,1826), r.spawnPoint, True]
                r.objCount += 1
    if op == 1:
        WallSection()
    if op == 2:
        CoinGen()
    if op == 3:
        BpadSection()
    for i in range(list(r.objects.keys())[0], r.objCount):
        if r.objects[i][0] == 2:
            Render(Turbo, i)
        elif r.objects[i][0] == 1:
            Render(Coin, i)
        elif r.objects[i][0] == 4:
            Render(Magnet, i)
        elif r.objects[i][0] == 3:
            col = Render(Missile, i)
            if col != None:
                if col[1] == 1 and r.setCap:
                    ShieldGame()
                    r.powerups[col[0]][1] -= (1000 - (r.runs - r.powerups[col[0]][1])) + 1
                    del r.powerups[col[0]]
                    break
        elif r.objects[i][0] == 5:
            col = Render(Wall, i)
            if col != None:
                if col[1] == 2 and r.setCap:
                    ShieldGame()
                    r.powerups[col[0]][1] -= (1000 - (r.runs - r.powerups[col[0]][1])) + 1
                    del r.powerups[col[0]]
                    break
        elif r.objects[i][0] == 6:
            col = Render(Bouncepad, i)
            if col != None:
                if col[1] == 2 and r.setCap:
                    ShieldGame()
                    r.powerups[col[0]][1] -= (1000 - (r.runs - r.powerups[col[0]][1])) + 1
                    del r.powerups[col[0]]
                    break
        elif r.objects[i][0] == 10:
            Render(Bullet, i)
        elif r.objects[i][0] == 7:
            Render(Laser, i)
        else:
            Render(Shield, i)

def WallSection():
    if r.wallSection == 0:
        
        r.coingen = None
        r.coinx = None
        r.wsdata[0] = random.randint(40, 80)
        r.wsdata[1] = random.randint(2, 5)
        r.wsdata[2] = r.runs
        r.wallSection = 1

    if r.wsdata[1] > -1:
        if r.wallSection == 1:
            holeCount = random.randint(1,4)
            holes = []
            totalHoles = 0

            for i in range(holeCount):
                
                s = random.randint(3,8)
                if totalHoles + s > 19:
                    holes.append(19 - totalHoles)
                else:
                    holes.append(s)
                totalHoles += holes[i]


            blocks = []
            totalBlocks = 0

            for i in range(holeCount + 2):
                
                if i < holeCount - 1:
                    if totalHoles + totalBlocks < 20:
                    


                        if int((20 - totalHoles)/holeCount) == 0:
                            blocks.append(random.randint(1, math.ceil((20 - totalHoles)/holeCount)))
                        else:
                            blocks.append(random.randint(1, int((20 - totalHoles)/holeCount)))
                        totalBlocks += blocks[i]
                    else:
                        blocks.append(0)

                elif i == holeCount - 1:
                    blocks.append(20 - totalHoles - totalBlocks)

                    totalBlocks += blocks[i]
                    

                else:
                    s = random.randint(1,4)
                    if s == 1:
                        if i == holeCount:
                            blocks.insert(0, 0)
                        else:
                            blocks.append(0)
            i = 0
            x = 0
            c = True
            while i < len(blocks):
                if c:
                    for bl in range(blocks[i]):
                        r.objects[max(r.objects.keys())+1] = [5, x * 96 + bl * 96, -100, True]
                        r.objCount += 1
                    else:
                        x += blocks[i]
                    if i+1 > len(holes):
                        i += 1
                else:
                    
                    if i+1 <= len(holes):
                        if x * 96 + holes[i]* 48 - 43.3 < 1874:
                            det = random.randint(1,10)
                            if det < 5:
                                r.objects[max(r.objects.keys())+1] = [1, x * 96 + holes[i]* 48 - 43.3 , -100, True]
                                r.objCount += 1
                            elif det < 7:
                                r.objects[max(r.objects.keys())+1] = [1, x * 96 + holes[i]* 40 - 43.3 , -100, True]
                                r.objects[max(r.objects.keys())+1] = [1, x * 96 + holes[i]* 56 - 43.3 , -100, True]
                                r.objCount += 2
                            elif det < 8:
                                r.objects[max(r.objects.keys())+1] = [1, x * 96 + holes[i]* 38 - 43.3 , -100, True]
                                r.objects[max(r.objects.keys())+1] = [1, x * 96 + holes[i]* 48 - 43.3 , -100, True]
                                r.objects[max(r.objects.keys())+1] = [1, x * 96 + holes[i]* 58 - 43.3 , -100, True]
                                r.objCount += 3
                        x += holes[i]
                        i += 1

                c = not c

            r.wsdata[1] -= 1
    else:
        r.wsdata = [None, None, None]
        r.wallSection = 0

def CoinGen():
   
    if r.coingen == None:
        r.coingen = random.randint(4, 9)
        r.coinx = random.randint(0,1833)
        cdet = random.randint(1,12)
        if cdet < 8:
            r.cpattern = 0
        elif cdet < 10:
            r.cpattern = 150
        elif cdet < 12:
            r.cpattern = -150
        else:
            r.cpattern = 2

    if r.coingen > 0:
        if r.cpattern == 2:
            rdet = random.randint(1,2)
            if rdet == 1:
                r.coinx += 150
            else:
                r.coinx -= 150
        else:
            r.coinx += r.cpattern
        r.objects[max(r.objects.keys())+1] = [1, r.coinx, -100, True]
        r.objCount += 1
        r.coingen -= 1

    else:
        r.coingen = None
        r.coinx = None
        r.cpattern = None
    
def WallGen():
    rc = random.randint(1,3)
    wgx = []
    while True:
        if len(wgx) != rc:
            a = True
            rax = random.randint(0,1824)
            for x in wgx:
                if x + 192 > rax and x - 192 < rax:
                    a = False 
                    break
            if a:
                wgx.append(rax)
        else:
            break
    for o in wgx:
        r.objects[max(r.objects.keys())+1] = [5, o, -100, True]
        r.objCount += 1

def ObjectClean():
   
    for black in r.blacklist:
        if black in r.objects:
            del r.objects[black]

    if len(r.objects) == 0:
        r.objects[-1] = [3, random.randint(100,1800), r.spawnPoint, False]
        r.objCount = 0

    r.blacklist = []

def BpadSection():
    if r.tgen == None:
        r.tdx = random.randint(100,1626)
        r.tgen = random.randint(2,6)
        r.tb = True
    
    if r.tb:
        a = 0
    else:
        a = 250
    r.objects[max(r.objects.keys())+1] = [6, r.tdx + a, -180, True]
    r.objCount += 1

    r.tgen -= 1
    r.tb = not r.tb
    if r.tgen == 0:
        r.tgen = None
        r.tdx = None

    
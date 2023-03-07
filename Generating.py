from Globals import *
import math


def ObjectFill():
    holeCount = random.randint(1,4)
    holes = []
    totalHoles = 0

    for i in range(holeCount):
        
        s = random.randint(2,5)
        if i == holeCount - 1 and totalHoles == 15 and s == 5:
            holes.append(4)
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
                x += holes[i]
                i += 1
                
        
        c = not c



def ObjectClean():
    for black in r.blacklist:
        del r.objects[black]

    if len(r.objects) == 0:
        r.objects[-1] = [1, random.randint(100,1800), r.spawnPoint, False]
        r.objCount = -1
    r.blacklist = []
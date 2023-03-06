from Globals import *
import math


def ObjectFill():

    lista = []


    holeCount = random.randint(1,4)
    holes = []
    totalHoles = 0

    for i in range(holeCount):
        
        r = random.randint(2,5)
        if i == holeCount - 1 and totalHoles == 15 and r == 5:
            holes.append(4)
        else:
            holes.append(r)
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
            r = random.randint(1,4)
            if r == 1:
                if i == holeCount:
                    blocks.insert(0, 0)
                else:
                    blocks.append(0)


    i = 0
    while i < len(blocks):
        #########################
        if c:
            r.objects[len(r.objects)] = [1, ]
            if i+1 > len(holes):
                i += 1
        else:
            if i+1 <= len(holes):
                lista.append(holes[i])
                i += 1
        
        c = not c

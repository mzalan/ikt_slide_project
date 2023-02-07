from Globals import *
from Wall import *
import random
from coin import *


def Render(Class, cl, _id):
    # print(r.objects)

    # if _id+1 not in r.objects.keys():
    #     c = Class(100,100,r.objects[_id][0],r.objects[_id][1],False)
    #     # print("if not in keys")
    # else:
    #     r.objects[_id][1] += r.diff
    #     c = Class(100,100,r.objects[_id][0],r.objects[_id][1], False)
    if _id+1 not in r.objects.keys():
        c = Class(85,85,r.objects[_id][0],r.objects[_id][1], True)
    else:
        r.objects[_id][1] += r.diff
        c = Class(85,85,r.objects[_id][0],r.objects[_id][1], True)

    if r.objects[_id][1] > 1120:
        del r.objects[_id]
        r.Points += r.diff * 2
        # print("delete")
        
    try:
        if r.objects[_id+1][0] == None:
            pass
    except:#100133
        # print("hehe")
        r.objects[_id+1] = [random.randint(100,1800), r.spawnPoint]

    # for obj in r.objects.items():


    surf = cl(c).Surf
    rect = cl(c).Rect
    color = cl(c).Color



    if cl(c).Draw:
        r.screen.blit(surf,(r.objects[_id][0],r.objects[_id][1]))
    else:
        r.screen.blit(surf, rect)

    if rect.colliderect(r.player_rect):
        r.Run = False

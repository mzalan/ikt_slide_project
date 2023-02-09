from Globals import *
from Wall import *
import random
from coin import *


def Render(Class, _id):

    if _id+1 not in r.objects.keys():
        c = Class(r.objects[_id][1],r.objects[_id][2])
    else:
        r.objects[_id][2] += r.diff
        c = Class(r.objects[_id][1],r.objects[_id][2])

    if r.objects[_id][3]:
        Class.Render(c, _id)

    Class.Collide(c, _id)
    
    if r.objects[_id][2] > 1120:
            del r.objects[_id]
            r.Points += r.diff * 2
            # print("delete")
            
    try:
        if r.objects[_id+1][1] == None:
            pass
    except:
        r.objects[_id+1] = [random.randint(1,2), random.randint(100,1800), r.spawnPoint, True]
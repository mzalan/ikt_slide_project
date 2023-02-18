from Globals import *
from Wall import *
import random
from coin import *
from Missile import *

def Render(Class, _id):
    # if Class == Missile:
    #     r.objects[_id].append()
    if _id+1 not in r.objects.keys():
        c = Class(r.objects[_id][1],r.objects[_id][2])
        if Class == Missile:
            r.objects[_id].append(r.runs)
            
    else:
        r.objects[_id][2] += r.diff * Class.Speed()
        c = Class(r.objects[_id][1],r.objects[_id][2])
        

    if r.objects[_id][3]:
        Class.Render(c, _id)

    Class.Collide(c, _id)
    
    if r.objects[_id][2] > (-100 + 1270) * Class.Speed() - 100:
            del r.objects[_id]
            r.Points += r.diff * 2
            
    try:
        if r.objects[_id+1][1] == None:
            pass
    except:
        r.objects[_id+1] = [random.randint(1,3), random.randint(100,1800), r.spawnPoint, True]
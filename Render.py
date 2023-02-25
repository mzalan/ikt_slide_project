from Globals import *
from Wall import *
import random
from coin import *
from Missile import *

def Render(Class, _id):

    try:   
        r.objects[_id][4]
    except:
        r.objects[_id].append(r.runs)
        
    if _id+1 not in r.objects.keys():
        c = Class(r.objects[_id][1],r.objects[_id][2])

        
            
    else:
        r.objects[_id][2] += r.diff * Class.Speed(Class(0,0), _id)
        c = Class(r.objects[_id][1],r.objects[_id][2])


    if r.objects[_id][3]:
        Class.Render(c, _id)

    col = Class.Collide(c, _id)

    if (r.objects[_id][2] > 1070 or r.objects[_id][2] < -100) and _id == min(r.objects.keys()):
        del r.objects[_id]
        r.Points += r.diff * 2

    
    try:
        if r.objects[_id+1][1] == None:
            pass
    except:
        r.objects[_id+1] = [random.randint(1,r.obj_type), random.randint(100,1820), r.spawnPoint, True]


    return col

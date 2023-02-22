from Globals import *
from Wall import *
import random
from coin import *
from Missile import *

def Render(Class, _id):
    sorting = sorted(r.objects)
    # print(sorting)
    soted = {}
    i = 0
    for s in sorting:
        soted[s] = r.objects[s]
        i += 1

    r.objects = soted

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

    Class.Collide(c, _id)

    if r.objects[_id][2] > 1070: #* Class.Speed(c, _id) 
        
        if Class != Missile:
            # print(f"Index {_id} object has been deleted at {r.runs}")
            del r.objects[_id]
            r.Points += r.diff * 2
        else:
            # print(r.objects)
            # print(f"min objects: {min(r.objects.keys())}")
            if _id == min(r.objects.keys()):
                print(f"{_id} rocket deleted")
                del r.objects[_id]
    
    



    # blacklist = []
    # if d == 1:
    #     for obj in r.objects.items():

    #         if r.objects[obj[0]][0] == 2 or r.objects[obj[0]][0] == 3:
    #             blacklist.append(obj[0])
    #             break
        
    #     for black in blacklist:
    #         print(f"Index {black} missile has been deleted at {r.runs}")
    #         del r.objects[black]

  





    try:
        if r.objects[_id+1][1] == None:
            pass
    except:
        r.objects[_id+1] = [random.randint(1,3), random.randint(100,1800), r.spawnPoint, True]

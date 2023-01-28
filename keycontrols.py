from Globals import *

def KeyupControls(dirIndex, comp, isMoveD):
    r.leftRight[dirIndex] = False
    r.moveD = isMoveD

    if not r.leftRight[comp]: #ez az if azért kell, hogy leellenőrizzük a másik boolt a leftRight-ban, mert ha hamis, le kell resetelnünk a sebességet és a boost ratet.
        r.speed = r.speedFloor
        r.boost = 0.5

def KeydownControls(dirIndex, comp, isMoveD): 
    r.leftRight[dirIndex] = True
    r.moveD = isMoveD

    if r.leftRight[comp]: #ez az if azért kell, hogy leellenőrizzük a másik boolt a leftRight-ban, mert ha igaz, mérsékelnünk kell a gyorsítási rátát.
        r.boost = 0
        r.boosting = True

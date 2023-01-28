from Globals import *
from Wall import *

def Render(Class):
    c = Class(100,100,250,900,"#100133")
    surf = w(c).Surf
    rect = w(c).Rect
    color = w(c).Color
    surf.fill(color)
    r.screen.blit(surf, rect)
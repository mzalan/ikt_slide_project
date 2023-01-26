import pygame
from Wall import *

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Slicky Slide")
clock = pygame.time.Clock()


player = pygame.Surface((100,100))

player_rect = player.get_rect(center=(960,930))

speed_font = pygame.font.Font(None, 50)

leftRight = [False,False] #bal gomb - jobb gomb booleanok. keydown -> true, keyup -> false mindkét bool esetén.
moveD = False #ha true, bal volt legutóbb lenyomva, ha false akkor jobb. keyupok esetén értékcsere (pl ha jobbot elengeded, falseról truera vált).
speed = 11 #alapértelmezett sebesség, mindig a boost változó értékével növelődik, ha mindkét iránygomb el van engedve akkor resetelődik
boost = 0.5 #alapértelmezett gyorsítási ráta, ez nullázódik majd fokozatosan 0.5-ig növekszik, ha a boosting bool true
boosting = False #ha a leftRightban mindkét bool true, akkor ez is true
speedCap = 38 #maxsebesség (pixel/frame)
speedFloor = 11 #minimumsebesség (pixel/frame)

def KeyupControls(dirIndex, comp, isMoveD):
    global leftRight
    leftRight[dirIndex] = False
    global moveD
    moveD = isMoveD
    if not leftRight[comp]: #ez az if azért kell, hogy leellenőrizzük a másik boolt a leftRight-ban, mert ha hamis, le kell resetelnünk a sebességet és a boost ratet.
        global speed
        speed = speedFloor
        global boost
        boost = 0.5

def KeydownControls(dirIndex, comp, isMoveD): 
    global leftRight
    leftRight[dirIndex] = True
    global moveD
    moveD = isMoveD
    if leftRight[comp]: #ez az if azért kell, hogy leellenőrizzük a másik boolt a leftRight-ban, mert ha igaz, mérsékelnünk kell a gyorsítási rátát.
        global boost
        boost = 0
        global boosting
        boosting = True

def PlayerMoving(a, edge): #sebességnövelés a boost változó által illetve a maximum sebesség meghatározása
    global speed
    global boost
    if speed < speedCap:
        speed += boost            
    else:
        speed = speedCap
    player_rect.x += speed * a
    if player_rect.x * a > edge * a:
        player_rect.x = edge

def Print(Class):
    c = Class(100,100,960,900,"purple")
    surf = Wall.SelfRet(c).Surf
    rect = Wall.SelfRet(c).Rect
    color = Wall.SelfRet(c).Color
    surf.fill(color)
    screen.blit(surf, rect)
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                KeyupControls(0, 1, False)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                KeyupControls(1, 0, True) 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_F5:
                pygame.quit()
                exit()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                KeydownControls(0, 1, True)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                KeydownControls(1, 0, False)
    

    screen.fill("lightblue")
    Print(Wall)

    if boosting:
        boost += 0.003
        if boost >= 0.5:
            boosting = False
            boost = 0.5
    
    if moveD and leftRight[0]:
        PlayerMoving(-1, 0)

    if not moveD and leftRight[1]:
        PlayerMoving(1, 1820)
    

    greenness = int((str(255-((255/(speedCap-speedFloor))*(speed-speedFloor)))).split(".")[0])
    screen.blit(player, player_rect)

    if greenness < 0:
        greenness = 0
    player.fill(pygame.Color(255, greenness, 0))

    speed_text = speed_font.render(str(speed), True, "black") #ki lehet írni változók értékeit a bal felső sarokba tesztelési célokból.
    screen.blit(speed_text,(5,5)) 

    
    pygame.display.update()
    clock.tick(60)

    

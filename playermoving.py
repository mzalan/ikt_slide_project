from Globals import *
from Wall import *

def PlayerMoving(a, edge, wedge): #sebességnövelés a boost változó által illetve a maximum sebesség meghatározása

    if r.speed < r.speedCap:
        r.speed += r.boost            
    else:
        r.speed = r.speedCap
    r.player_rect.x += r.speed * a
    if r.player_rect.x * a > edge * a:
        r.player_rect.x = edge

    if Wall.SelfRet(Wall(100,100,250,900,"#100133")).Rect.colliderect(r.player_rect):
        gover_text = r.gover_font.render("Game over", True, "red")
        r.screen.blit(gover_text,(900,320))
        if r.player_rect.x * a > wedge * a:
            r.player_rect.x = wedge

def BoostMoving():
    if r.boosting:
        r.boost += 0.003
    if r.boost >= 0.5:
        r.boosting = False
        r.boost = 0.5
    
    if r.moveD and r.leftRight[0]:
        PlayerMoving(-1, 0, 300)

    if not r.moveD and r.leftRight[1]:
        PlayerMoving(1, 1820,100)

def PlayerBlit():
    greenness = int((str(255-((255/(r.speedCap-r.speedFloor))*(r.speed-r.speedFloor)))).split(".")[0])
    r.screen.blit(r.player, r.player_rect)

    if greenness < 0:
        greenness = 0
    r.player.fill(pygame.Color(255, greenness, 0))

    speed_text = r.speed_font.render(str(r.speed), True, "black") #ki lehet írni változók értékeit a bal felső sarokba tesztelési célokból.
    r.screen.blit(speed_text,(5,5)) 
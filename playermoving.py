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

    # if Wall.SelfRet(Wall(100,100,1500,900)).Rect.colliderect(r.player_rect):
    #     gover_text = r.gover_font.render("Game over", True, "red")
    #     r.screen.blit(gover_text,(900,320))
    #     if r.player_rect.x * a > wedge * a:
    #         r.player_rect.x = wedge
    # for obj in r.objects.items():
    #     print(r.player_rect.x)
    #     print(obj[1][0])
    #     if obj[1][1] < r.player_rect.y + 50 and obj[1][1] > r.player_rect.y -50 and obj[1][0] < r.player_rect.x + 50 and obj[1][0] > r.player_rect.x -50:
           
    #         gover_text = r.gover_font.render("Game over", True, "red")
    #         r.screen.blit(gover_text,(900,320))
    #         print("CONGRATULATIONS MUHAHAHHAHAHA")
    #         pygame.quit()
    #         exit()

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

def PlayerBlit(cond):
    if cond:
        greenness = int((str(255-((255/(r.speedCap-r.speedFloor))*(r.speed-r.speedFloor)))).split(".")[0])
        r.screen.blit(r.player, r.player_rect)

        if greenness < 0:
            greenness = 0
        r.player.fill(pygame.Color(255, greenness, 0))

        first_text = r.first_font.render(str(round(r.Points,0)).split(".")[0], True, "black")
        second_text = r.first_font.render(str(round(r.Best,0)).split(".")[0], True, "black")#ki lehet írni változók értékeit a bal felső sarokba tesztelési célokból.
        second_rect = second_text.get_rect(topright=(1915,5))

        r.screen.blit(first_text,(5,5)) 
        r.screen.blit(second_text,second_rect) 

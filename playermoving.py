from Globals import *
from Wall import *
from keycontrols import *

def PlayerMoving(a, edge): #sebességnövelés a boost változó által illetve a maximum sebesség meghatározása
    if r.speed < r.speedCap:
        r.speed += r.boost        
    else:
        r.speed = r.speedCap
    r.player_rect.x += r.speed * a
    if r.player_rect.x * a > edge * a:
        r.player_rect.x = edge

def BoostMoving():
    if r.boosting:
        r.boost += 0.003
    if r.boost >= 0.5:
        r.boosting = False
        r.boost = 0.5
    
    if r.moveD and r.leftRight[0]:
        PlayerMoving(-1, 0)

    if not r.moveD and r.leftRight[1]:
        PlayerMoving(1, 1820)


def Bounce(d,edge, speed):

    if r.elapsed < 25:

        r.player_rect.x += speed * d
        if r.player_rect.x * d > edge * d:
            
            r.player_rect.x = edge
            
            r.bounce_data[0] *= -1
            r.bounce_data[1] += 1820 * r.bounce_data[0]


    else:
        r.elapsed = -1
        r.bounce_data = None
        if not r.leftRight[0] and not r.leftRight[1]:
            KeyupControls(0, 1, False)

    r.elapsed += 1


def PlayerBlit(cond):
    if cond == 1:
        greenness = int((str(255-((255/(r.speedCap-r.speedFloor))*(r.speed-r.speedFloor)))).split(".")[0])
        r.screen.blit(r.player, r.player_rect)

        if greenness < 0:
            greenness = 0
        r.player.fill(pygame.Color(255, greenness, 0))



        if r.Points > r.Best:
            first_text = r.first_font.render(str(round(r.Points,0)).split(".")[0], True, "#5800d4")
        else:
            first_text = r.first_font.render(str(round(r.Points,0)).split(".")[0], True, "black")

        second_text = r.first_font.render(str(round(r.Coins,0)).split(".")[0], True, "#856e1c")
        second_rect = second_text.get_rect(topright=(1915,5))

        r.screen.blit(first_text,(5,5)) 
        r.screen.blit(second_text,second_rect) 


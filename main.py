import pygame
from Wall import *
from keycontrols import *
from Globals import *
from playermoving import *
from Render import *
from gameover import *
from coin import *
from Bouncepad import *
from Missile import *
from menu import *
from Speed import *
from Magnet import *
from Shield import *
from Turbo import *
from Laser import *

pygame.init()


def Generating(cond):

    if cond:
        r.objCount += 2
    for i in range(list(r.objects.keys())[0], r.objCount):
        if r.objects[i][0] == 2:
            Render(Turbo, i)
        elif r.objects[i][0] == 1:
            Render(Shield, i)
        elif r.objects[i][0] == 4:
            Render(Magnet, i)
        elif r.objects[i][0] == 3:
            col = Render(Missile, i)
            if col != None:
                if col[1] == 1 and r.setCap:
                    ShieldGame()
                    r.powerups[col[0]][1] -= (1000 - (r.runs - r.powerups[col[0]][1])) + 1
                    del r.powerups[col[0]]
                    break
        elif r.objects[i][0] == 5:
            col = Render(Wall, i)
            if col != None:
                if col[1] == 1 and r.setCap:
                    ShieldGame()
                    r.powerups[col[0]][1] -= (1000 - (r.runs - r.powerups[col[0]][1])) + 1
                    del r.powerups[col[0]]
                    break
        else:
            Render(Coin, i)

while True:
    r.click = False
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
                

            if event.key == pygame.K_r and r.Run == 2:
                StartGame()
            
            if event.key == pygame.K_e:
                r.Run = 2

            
        if event.type == pygame.MOUSEBUTTONDOWN and (r.Run == 0 or r.Run == 2):
            r.click = True
                

    r.screen.fill("lightblue")

    if r.Run == 0:
        Menu(r.screen)

    elif r.Run == 1:

        if r.runs % 50 == 0:
            if r.diff < r.diffCap:
                r.diff += 0.2
            else:
                if r.setCap:
                    r.diff = r.diffCap

            Generating(True)
        else:
            Generating(False)

        if r.runs % 5 == 0 and r.Run == 1:
            r.Points += 10

        if r.bounce_data == None:
            BoostMoving()
        else:
            Bounce(r.bounce_data[0],r.bounce_data[1], r.bounce_data[2])

        PlayerBlit(r.Run)

        drawables = -1
        to_delete = []
        for i in range(len(r.powerups)):
            if r.runs - r.powerups[i][1] < r.power_upgrades[r.powerups[i][0]]:
                drawables += 1
                pos = drawables * 350
                PowerupActivation(r.powerups[i][2], i, pos)

                if not r.setCap and (r.powerups[i][0] == 1 or r.powerups[i][0] == 3):
                    r.powerups[i][1] += 1

            elif r.runs - r.powerups[i][1] == r.power_upgrades[r.powerups[i][0]]:
                to_delete.append([i, r.powerups[i][0]])
            
        for i in range(len(to_delete)):
            if to_delete[i][1] == 1:
                pass
            elif to_delete[i][1] == 2:
                r.diff = r.powerups[to_delete[0][i]][3]
                r.setCap = True
            del r.powerups[to_delete[i][0]]

        r.runs += 1  

    elif r.Run == 2:
        GameOver()

    # t = r.score_font.render(str(round(r.diff,0)).split(".")[0], True, "#6b0101")
    # tr = t.get_rect(center=(960,400))
    # r.screen.blit(t, tr)


    pygame.display.update()
    r.clock.tick(60)

            #WALL RENDERING 
            # col = Render(Wall, i)
            # if col != None:
            #     ShieldGame()
            #     r.powerups[col][1] -= (1000 - (r.runs - r.powerups[col][1])) + 1
            #     del r.powerups[col]
            #     break
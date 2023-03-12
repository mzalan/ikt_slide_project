import pygame
from Wall import *
from keycontrols import *
from Globals import *
from playermoving import *
from gameover import *
from menu import *
from Upgrade import *
from Save import *
from Generating import *


Fajlolvas()
pygame.init()


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

            
        if event.type == pygame.MOUSEBUTTONDOWN:
            r.click = True
                

    r.screen.fill("lightblue")

    if r.Run == 0:
        Menu()

    elif r.Run == 1:

        if r.wsdata[0] != None and (r.runs - r.wsdata[2]) % r.wsdata[0] == 0:
            Generating(1)
        if r.runs % 18 == 0:
            if r.diff < r.diffCap:
                r.diff += 0.04
            else:
                if r.setCap:
                    r.diff = r.diffCap
            rd = random.randint(1,20)
            if rd == 1:
                r.distance = random.randint(30, 100)
            if r.coingen != None:
                Generating(2)

        if r.runs % r.distance == 0:
            if r.coingen == None:
                Generating(0)
            if r.tgen == None:
                Generating(0)
            elif r.tgen != None:
                Generating(3)
        else:
            Generating(5)


        
        if r.runs % 3 == 0 and r.Run == 1:
            r.Points += r.diff * 1.3

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

                if not r.setCap and (r.powerups[i][0] == 1 or r.powerups[i][0] == 3):
                    r.powerups[i][1] += 1

                if r.powerups[i][0] == 3 and r.click and r.setCap and r.ammo != 0:
                    bullet = {max(r.objects.keys())+1: [10, r.player_rect.x + 22.5, r.player_rect.y, True]}
                    r.objCount += 1
                    r.objects.update(bullet)
                    if r.ammo > 0:
                        r.ammo -= 1
                PowerupActivation(r.powerups[i][2], i, pos)

            elif r.runs - r.powerups[i][1] == r.power_upgrades[r.powerups[i][0]]:
                to_delete.append([i, r.powerups[i][0]])
            
        for i in range(len(to_delete)):
            if to_delete[i][1] == 1:
                pass
            elif to_delete[i][1] == 2:
                r.diff = r.powerups[to_delete[0][i]][3]
                r.setCap = True
                
            del r.powerups[to_delete[i][0]]

        ObjectClean()

        r.runs += 1  

    elif r.Run == 2:
        GameOver()

    elif r.Run == 3:
        Upgrades()

    pygame.display.update()
    r.clock.tick(60)
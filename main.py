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

pygame.init()


def Generating(cond):

    if cond:
        r.objCount += 1
    for i in range(list(r.objects.keys())[0], r.objCount):
        if r.objects[i][0] == 1:
            Render(Magnet, i)
        elif r.objects[i][0] == 2:
            Render(Coin, i)
        elif r.objects[i][0] == 3:
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
        
        r.runs += 1   
    elif r.Run == 2:
        GameOver()

    if r.runs - r.magnet_start < 1000:
        MagnetActivation()

    pygame.display.update()
    r.clock.tick(60)

    

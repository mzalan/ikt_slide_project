import pygame
from Wall import *
from keycontrols import *
from Globals import *
from playermoving import *
from Render import *
from gameover import *
import random
from coin import *

pygame.init()

wallCount = 0


def Walling(cond):

    if r.Run:
        global wallCount
        if cond:
            wallCount += 5
        print(r.objects)
        for i in range(list(r.objects.keys())[0], wallCount):
            if r.objects[i][0] == 1:
                Render(Wall, i)
            else:
                Render(Coin, i)


runs = 0

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

            if event.key == pygame.K_e:
                r.player_rect.x = 1200
            if event.key == pygame.K_o:
                r.player_rect.x = 50

            #restart game
            if event.key == pygame.K_r and not r.Run:
                if r.Points > r.Best:
                    r.Best = r.Points
                r.Run = True
                r.diff = 5
                wallCount = 0
                r.objects = {}
                r.objects[0] = [random.randint(1,2), random.randint(100,1800), r.spawnPoint]
                runs = 0
                r.Points = 0
    
    r.screen.fill("lightblue")

    if runs % 50 == 0:
        if r.diff < r.diffCap:
            r.diff += 0.2
        else:
            r.diff = 40

            
        Walling(True)

    else:
        Walling(False)

    if runs % 5 == 0 and r.Run:
        r.Points += 10

    BoostMoving()

    PlayerBlit(r.Run)
    
    if r.Run:
        runs += 1   
    else:
        GameOver()
    # if runs == 1000:
    #     pygame.quit()
    #     exit()

    pygame.display.update()
    r.clock.tick(60)

    

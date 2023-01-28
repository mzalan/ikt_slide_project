import pygame
from Wall import *
from keycontrols import *
from Globals import *
from playermoving import *
from Render import *

pygame.init()

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
            if event.key == pygame.K_r:
                r.player_rect.x = 50
    
    r.screen.fill("lightblue")
    Render(Wall)

    BoostMoving()
    
    PlayerBlit()
    
    pygame.display.update()
    r.clock.tick(60)

    

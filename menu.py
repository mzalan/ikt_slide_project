import pygame
from Globals import *
from StartGame import *

def Menu(screen):

    color_light = (170,170,170)
    color_dark = "#111112"
    width = screen.get_width()
    height = screen.get_height()
    mouse = pygame.mouse.get_pos()
    
    
    title_text = r.gover_font.render("Slicky Slide", True, "black")
    play_text = r.score_font.render("Play", True, "black")
    exit_text = r.score_font.render("Exit", True, "black")
    

    r.screen.blit(title_text, (width/2+50,height/2))
    r.screen.blit(play_text, (width/2+50,height/2))
    r.screen.blit(exit_text, (width/2+50,height/2))

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
        if r.click:
            StartGame()
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
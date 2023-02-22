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
    title_rect = title_text.get_rect(center=(960,240))

   
    

    exit_text = r.score_font.render("Exit", True, "black")
    exit_rect = exit_text.get_rect(center=(960,640))
    

    play_draw_surf = pygame.Surface((300,120))
    play_draw_rect = play_draw_surf.get_rect(center=(960,440))

    exit_draw_surf = pygame.Surface((300,120))
    exit_draw_rect = exit_draw_surf.get_rect(center=(960,640))

#play gomb

    if play_draw_rect.x <= mouse[0] <= play_draw_rect.x+play_draw_rect.w and play_draw_rect.y <= mouse[1] <= play_draw_rect.y+play_draw_rect.height:
        drawing = pygame.draw.rect(play_draw_surf, color_light, play_draw_rect)
        
        play_draw_surf.fill("#f5eeda")
        screen.blit(play_draw_surf, drawing)

        play_text = r.score_font.render("Play", True, "black")
        play_rect = play_text.get_rect(center=(960,440))
        if r.click:
            StartGame()
    else:
       
        drawing = pygame.draw.rect(play_draw_surf, "red",play_draw_rect)
        screen.blit(play_draw_surf, drawing)

        play_text = r.score_font.render("Play", True, "white")
        play_rect = play_text.get_rect(center=(960,440))
    
#exit gomb

    if exit_draw_rect.x <= mouse[0] <= exit_draw_rect.x+exit_draw_rect.w and exit_draw_rect.y <= mouse[1] <= exit_draw_rect.y+exit_draw_rect.height:
        drawing = pygame.draw.rect(exit_draw_surf, color_light, exit_draw_rect)
        
        exit_draw_surf.fill("#f5eeda")
        screen.blit(exit_draw_surf, drawing)

        exit_text = r.score_font.render("Exit", True, "black")
        exit_rect = exit_text.get_rect(center=(960,640))
        if r.click:
            StartGame()
    else:
       
        drawing = pygame.draw.rect(exit_draw_surf, "red",exit_draw_rect)
        screen.blit(exit_draw_surf, drawing)

        exit_text = r.score_font.render("Exit", True, "white")
        exit_rect = exit_text.get_rect(center=(960,640))


    r.screen.blit(title_text, title_rect)
    r.screen.blit(play_text, play_rect)
    r.screen.blit(exit_text, exit_rect)
import pygame
from Globals import *
from menu import *

def Upgrades(screen):

    color_light = (170,170,170)
    color_dark = "#111112"
    width = screen.get_width()
    height = screen.get_height()
    mouse = pygame.mouse.get_pos()

    magnet_text = r.gover_font.render("Magnet", True, "black")
    magnet_rect = magnet_text.get_rect(center=(600,240))


    turbo_text = r.score_font.render("Turbo", True, "black")
    turbo_rect = turbo_text.get_rect(center=(600,640))


    shield_text = r.score_font.render("Shield", True, "black")
    shield_rect = shield_text.get_rect(center=(1000,240))

    
    turret_text = r.score_font.render("Turret", True, "black")
    turret_rect = turret_text.get_rect(center=(1000,640))

    
    back_text = r.score_font.render("Back", True, "black")
    back_rect = back_text.get_rect(center=(1500,1040))


    magnet_draw_surf = pygame.Surface((350,300))
    magnet_draw_rect = magnet_draw_surf.get_rect(center=(960,440))


    turbo_draw_surf = pygame.Surface((350,300))
    turbo_draw_rect = turbo_draw_surf.get_rect(center=(960,640))


    shield_draw_surf = pygame.Surface((350,300))
    shield_draw_rect = shield_draw_surf.get_rect(center=(960,840))


    turret_draw_surf = pygame.Surface((350,300))
    turret_draw_rect = turret_draw_surf.get_rect(center=(960,440))


    back_draw_surf = pygame.Surface((100,80))
    back_draw_rect = back_draw_surf.get_rect(center=(960,640))

#back gomb

    if back_draw_rect.x <= mouse[0] <= back_draw_rect.x+back_draw_rect.w and back_draw_rect.y <= mouse[1] <= back_draw_rect.y+back_draw_rect.height:
        drawing = pygame.draw.rect(back_draw_surf, color_light, back_draw_rect)
        
        back_draw_surf.fill("#f5eeda")
        screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "black")
        back_rect = back_text.get_rect(center=(960,440))
        if r.click:
            Menu()
    else:
       
        drawing = pygame.draw.rect(back_draw_surf, "red",back_draw_rect)
        screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "white")
        back_rect = back_text.get_rect(center=(960,440))
    


    r.screen.blit(magnet_text, magnet_rect)
    r.screen.blit(turbo_text, turbo_rect)
    r.screen.blit(shield_text, shield_rect)
    r.screen.blit(turret_text, turret_rect)
    r.screen.blit(back_text, back_rect)
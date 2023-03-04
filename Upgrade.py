import pygame
import os
from Globals import *
from menu import *
from Turret import *
from Magnet import *
from Shield import *
from Turbo import *

def Upgrades():

    color_light = (170,170,170)
    color_dark = "#111112"
    width = r.screen.get_width()
    height = r.screen.get_height()
    mouse = pygame.mouse.get_pos()


    coin_text = r.gover_font.render("Your Coins:", True, "black")
    coin_rect = coin_text.get_rect(center=(960,200))


    magnet_title = r.gover_font.render("Magnet", True, "black")
    magnet_rect1 = magnet_title.get_rect(center=(660,340))
    magnet_img_kep = pygame.image.load(os.path.join('assets', 'magnet1.png'))
    magnet_img_meret = pygame.transform.scale(magnet_img_kep,(100,80))
    magnet_rect2 = magnet_img_meret.get_rect(center=(660,480))


    turbo_title = r.score_font.render("Turbo", True, "black")
    turbo_rect1 = turbo_title.get_rect(center=(600,700))
    turbo_img_kep = pygame.image.load(os.path.join('assets', 'speed.png'))
    turbo_img_meret = pygame.transform.scale(turbo_img_kep,(100,80))
    turbo_rect2 = turbo_img_meret.get_rect(center=(600,880))


    shield_title = r.score_font.render("Shield", True, "black")
    shield_rect1 = shield_title.get_rect(center=(1220,340))
    shield_img_kep = pygame.image.load(os.path.join('assets', 'shield.png'))
    shield_img_meret = pygame.transform.scale(shield_img_kep,(100,80))
    shield_rect2 = shield_img_meret.get_rect(center=(1220,480))

    
    turret_title = r.score_font.render("Turret", True, "black")
    turret_rect1 = turret_title.get_rect(center=(1220,700))
    turret_img_kep = pygame.image.load(os.path.join('assets', 'missile.png'))
    turret_img_meret = pygame.transform.scale(turret_img_kep,(100,80))
    turret_rect2 = turret_img_meret.get_rect(center=(1220,880))

    
    back_text = r.score_font.render("Back", True, "black")
    back_rect = back_text.get_rect(center=(200,1040))


    magnet_draw_surf = pygame.Surface((450,300))
    magnet_draw_rect = magnet_draw_surf.get_rect(center=(660,440))
    

    turbo_draw_surf = pygame.Surface((450,300))
    turbo_draw_rect = turbo_draw_surf.get_rect(center=(660,800))


    shield_draw_surf = pygame.Surface((450,300))
    shield_draw_rect = shield_draw_surf.get_rect(center=(1220,440))


    turret_draw_surf = pygame.Surface((450,300))
    turret_draw_rect = turret_draw_surf.get_rect(center=(1220,800))


    back_draw_surf = pygame.Surface((100,80))
    back_draw_rect = back_draw_surf.get_rect(center=(200,1040))


#magnet rész

    if magnet_draw_rect.x <= mouse[0] <= magnet_draw_rect.x+magnet_draw_rect.w and magnet_draw_rect.y <= mouse[1] <= magnet_draw_rect.y+magnet_draw_rect.height:
        drawing = pygame.draw.rect(magnet_draw_surf, color_light, magnet_draw_rect)
        
        magnet_draw_surf.fill("#f5eeda")
        r.screen.blit(magnet_draw_surf, drawing)

        magnet_title = r.gover_font.render("Magnet", True, "black")
        magnet_rect1 = magnet_title.get_rect(center=(660,340))
        magnet_img_kep = pygame.image.load(os.path.join('assets', 'magnet1.png'))
        magnet_img_meret = pygame.transform.scale(magnet_img_kep,(100,80))
        magnet_rect2 = magnet_img_meret.get_rect(center=(660,480))

    else:
       
        drawing = pygame.draw.rect(magnet_draw_surf, "black", magnet_draw_rect)
        r.screen.blit(magnet_draw_surf, drawing)

        magnet_title = r.gover_font.render("Magnet", True, "white")
        magnet_rect1 = magnet_title.get_rect(center=(660,340))
        magnet_img_kep = pygame.image.load(os.path.join('assets', 'magnet1.png'))
        magnet_img_meret = pygame.transform.scale(magnet_img_kep,(100,80))
        magnet_rect2 = magnet_img_meret.get_rect(center=(660,480))


#turbo rész

    if turbo_draw_rect.x <= mouse[0] <= turbo_draw_rect.x+turbo_draw_rect.w and turbo_draw_rect.y <= mouse[1] <= turbo_draw_rect.y+turbo_draw_rect.height:
        drawing = pygame.draw.rect(turbo_draw_surf, color_light, turbo_draw_rect)
        
        turbo_draw_surf.fill("#f5eeda")
        r.screen.blit(turbo_draw_surf, drawing)

        turbo_title = r.gover_font.render("Turbo", True, "black")
        turbo_rect1 = turbo_title.get_rect(center=(660,700))
        turbo_img_kep = pygame.image.load(os.path.join('assets', 'speed.png'))
        turbo_img_meret = pygame.transform.scale(turbo_img_kep,(100,80))
        turbo_rect2 = turbo_img_meret.get_rect(center=(660,880))
        
    else:
       
        drawing = pygame.draw.rect(turbo_draw_surf, "black", turbo_draw_rect)
        r.screen.blit(turbo_draw_surf, drawing)

        turbo_title = r.gover_font.render("Turbo", True, "white")
        turbo_rect1 = turbo_title.get_rect(center=(660,700))
        turbo_img_kep = pygame.image.load(os.path.join('assets', 'speed.png'))
        turbo_img_meret = pygame.transform.scale(turbo_img_kep,(100,80))
        turbo_rect2 = turbo_img_meret.get_rect(center=(660,880))


#shield rész

    if shield_draw_rect.x <= mouse[0] <= shield_draw_rect.x+shield_draw_rect.w and shield_draw_rect.y <= mouse[1] <= shield_draw_rect.y+shield_draw_rect.height:
        drawing = pygame.draw.rect(shield_draw_surf, color_light, shield_draw_rect)
        
        shield_draw_surf.fill("#f5eeda")
        r.screen.blit(shield_draw_surf, drawing)

        shield_title = r.gover_font.render("Shield", True, "black")
        shield_rect1 = shield_title.get_rect(center=(1220,340))
        shield_img_kep = pygame.image.load(os.path.join('assets', 'shield.png'))
        shield_img_meret = pygame.transform.scale(shield_img_kep,(100,80))
        shield_rect2 = shield_img_meret.get_rect(center=(1220,480))
        
    else:
       
        drawing = pygame.draw.rect(shield_draw_surf, "black", shield_draw_rect)
        r.screen.blit(shield_draw_surf, drawing)

        shield_title = r.gover_font.render("Shield", True, "white")
        shield_rect1 = shield_title.get_rect(center=(1220,340))
        shield_img_kep = pygame.image.load(os.path.join('assets', 'shield.png'))
        shield_img_meret = pygame.transform.scale(shield_img_kep,(100,80))
        shield_rect2 = shield_img_meret.get_rect(center=(1220,480))


#turret rész

    if turret_draw_rect.x <= mouse[0] <= turret_draw_rect.x+turret_draw_rect.w and turret_draw_rect.y <= mouse[1] <= turret_draw_rect.y+turret_draw_rect.height:
        drawing = pygame.draw.rect(turret_draw_surf, color_light, turret_draw_rect)
        
        turret_draw_surf.fill("#f5eeda")
        r.screen.blit(turret_draw_surf, drawing)

        turret_title = r.gover_font.render("Turret", True, "black")
        turret_rect1 = turret_title.get_rect(center=(1220,700))
        turret_img_kep = pygame.image.load(os.path.join('assets', 'missile.png'))
        turret_img_meret = pygame.transform.scale(turret_img_kep,(100,80))
        turret_rect2 = turret_img_meret.get_rect(center=(1220,880))
        
    else:
       
        drawing = pygame.draw.rect(turret_draw_surf, "black", turret_draw_rect)
        r.screen.blit(turret_draw_surf, drawing)

        turret_title = r.gover_font.render("Turret", True, "white")
        turret_rect1 = turret_title.get_rect(center=(1220,700))
        turret_img_kep = pygame.image.load(os.path.join('assets', 'missile.png'))
        turret_img_meret = pygame.transform.scale(turret_img_kep,(100,80))
        turret_rect2 = turret_img_meret.get_rect(center=(1220,880))


#back gomb

    if back_draw_rect.x <= mouse[0] <= back_draw_rect.x+back_draw_rect.w and back_draw_rect.y <= mouse[1] <= back_draw_rect.y+back_draw_rect.height:
        drawing = pygame.draw.rect(back_draw_surf, color_light, back_draw_rect)
        
        back_draw_surf.fill("#f5eeda")
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "black")
        back_rect = back_text.get_rect(center=(200,1040))
        if r.click:
            Menu()
    else:
       
        drawing = pygame.draw.rect(back_draw_surf, "black",back_draw_rect)
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "white")
        back_rect = back_text.get_rect(center=(200,1040))
    


    r.screen.blit(coin_text, coin_rect)
    r.screen.blit(magnet_title, magnet_rect1)
    r.screen.blit(magnet_img_meret, magnet_rect2)
    r.screen.blit(turbo_title, turbo_rect1)
    r.screen.blit(turbo_img_meret, turbo_rect2)
    r.screen.blit(shield_title, shield_rect1)
    r.screen.blit(shield_img_meret, shield_rect2)
    r.screen.blit(turret_title, turret_rect1)
    r.screen.blit(turret_img_meret, turret_rect2)
    r.screen.blit(back_text, back_rect)
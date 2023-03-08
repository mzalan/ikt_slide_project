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


    coin_text = r.score_font.render("Your Coins:", True, "black")
    coin_rect = coin_text.get_rect(center=(960,90))
    coin_szam = r.gover_font.render(str(r.Coins), True, "black")
    coin_szam_rect = coin_szam.get_rect(center=(960,185))

    magnet_title = r.gover_font.render("Magnet", True, "black")
    magnet_title_meret = pygame.transform.scale(magnet_title,(300,50))
    magnet_rect1 = magnet_title.get_rect(center=(720,340))
    magnet_img_kep = pygame.image.load(os.path.join('assets', 'magnet1.png'))
    magnet_img_meret = pygame.transform.scale(magnet_img_kep,(100,80))
    magnet_rect2 = magnet_img_meret.get_rect(center=(660,400))

    


    turbo_title = r.score_font.render("Turbo", True, "black")
    turbo_title_meret = pygame.transform.scale(turbo_title,(300,50))
    turbo_rect1 = turbo_title.get_rect(center=(680,700))
    turbo_img_kep = pygame.image.load(os.path.join('assets', 'speed.png'))
    turbo_img_meret = pygame.transform.scale(turbo_img_kep,(100,80))
    turbo_rect2 = turbo_img_meret.get_rect(center=(660,760))


    shield_title = r.score_font.render("Shield", True, "black")
    shield_title_meret = pygame.transform.scale(shield_title,(300,50))
    shield_rect1 = shield_title.get_rect(center=(1280,340))
    shield_img_kep = pygame.image.load(os.path.join('assets', 'shield.png'))
    shield_img_meret = pygame.transform.scale(shield_img_kep,(100,80))
    shield_rect2 = shield_img_meret.get_rect(center=(1220,400))


    turret_title = r.score_font.render("Turret", True, "black")
    turret_title_meret = pygame.transform.scale(turret_title,(300,50))
    turret_rect1 = turret_title.get_rect(center=(1280,700))
    turret_img_kep = pygame.image.load(os.path.join('assets', 'laser.png'))
    turret_img_meret = pygame.transform.scale(turret_img_kep,(100,80))
    turret_rect2 = turret_img_meret.get_rect(center=(1220,800))


    back_text = r.score_font.render("Back", True, "black")
    back_rect = back_text.get_rect(center=(300,900))


    magnet_draw_surf = pygame.Surface((450,300))
    magnet_draw_rect = magnet_draw_surf.get_rect(center=(660,440))


    turbo_draw_surf = pygame.Surface((450,300))
    turbo_draw_rect = turbo_draw_surf.get_rect(center=(660,800))


    shield_draw_surf = pygame.Surface((450,300))
    shield_draw_rect = shield_draw_surf.get_rect(center=(1220,440))


    turret_draw_surf = pygame.Surface((450,300))
    turret_draw_rect = turret_draw_surf.get_rect(center=(1220,800))


    back_draw_surf = pygame.Surface((200,80))
    back_draw_rect = back_draw_surf.get_rect(center=(300,900))


#magnet rész

    if magnet_draw_rect.x <= mouse[0] <= magnet_draw_rect.x+magnet_draw_rect.w and magnet_draw_rect.y <= mouse[1] <= magnet_draw_rect.y+magnet_draw_rect.height:
        drawing = pygame.draw.rect(magnet_draw_surf, color_light, magnet_draw_rect)

        magnet_draw_surf.fill("#f5eeda")
        r.screen.blit(magnet_draw_surf, drawing)

        magnet_title = r.gover_font.render("Magnet", True, "black")
        magnet_title_meret = pygame.transform.scale(magnet_title,(300,50))
        magnet_rect1 = magnet_title.get_rect(center=(720,340))
        magnet_img_kep = pygame.image.load(os.path.join('assets', 'magnet1.png'))
        magnet_img_meret = pygame.transform.scale(magnet_img_kep,(100,80))
        magnet_rect2 = magnet_img_meret.get_rect(center=(660,400))

    else:

        drawing = pygame.draw.rect(magnet_draw_surf, "black", magnet_draw_rect)
        r.screen.blit(magnet_draw_surf, drawing)

        magnet_title = r.gover_font.render("Magnet", True, "white")
        magnet_title_meret = pygame.transform.scale(magnet_title,(300,50))
        magnet_rect1 = magnet_title.get_rect(center=(720,340))
        magnet_img_kep = pygame.image.load(os.path.join('assets', 'magnet1.png'))
        magnet_img_meret = pygame.transform.scale(magnet_img_kep,(100,80))
        magnet_rect2 = magnet_img_meret.get_rect(center=(660,400))


#turbo rész

    if turbo_draw_rect.x <= mouse[0] <= turbo_draw_rect.x+turbo_draw_rect.w and turbo_draw_rect.y <= mouse[1] <= turbo_draw_rect.y+turbo_draw_rect.height:
        drawing = pygame.draw.rect(turbo_draw_surf, color_light, turbo_draw_rect)

        turbo_draw_surf.fill("#f5eeda")
        r.screen.blit(turbo_draw_surf, drawing)

        turbo_title = r.gover_font.render("Turbo", True, "black")
        turbo_title_meret = pygame.transform.scale(turbo_title,(300,50))
        turbo_rect1 = turbo_title.get_rect(center=(680,700))
        turbo_img_kep = pygame.image.load(os.path.join('assets', 'speed.png'))
        turbo_img_meret = pygame.transform.scale(turbo_img_kep,(100,80))
        turbo_rect2 = turbo_img_meret.get_rect(center=(660,760))

    else:

        drawing = pygame.draw.rect(turbo_draw_surf, "black", turbo_draw_rect)
        r.screen.blit(turbo_draw_surf, drawing)

        turbo_title = r.gover_font.render("Turbo", True, "white")
        turbo_title_meret = pygame.transform.scale(turbo_title,(300,50))
        turbo_rect1 = turbo_title.get_rect(center=(680,700))
        turbo_img_kep = pygame.image.load(os.path.join('assets', 'speed.png'))
        turbo_img_meret = pygame.transform.scale(turbo_img_kep,(100,80))
        turbo_rect2 = turbo_img_meret.get_rect(center=(660,760))


#shield rész

    if shield_draw_rect.x <= mouse[0] <= shield_draw_rect.x+shield_draw_rect.w and shield_draw_rect.y <= mouse[1] <= shield_draw_rect.y+shield_draw_rect.height:
        drawing = pygame.draw.rect(shield_draw_surf, color_light, shield_draw_rect)

        shield_draw_surf.fill("#f5eeda")
        r.screen.blit(shield_draw_surf, drawing)

        shield_title = r.gover_font.render("Shield", True, "black")
        shield_title_meret = pygame.transform.scale(shield_title,(300,50))
        shield_rect1 = shield_title.get_rect(center=(1280,340))
        shield_img_kep = pygame.image.load(os.path.join('assets', 'shield.png'))
        shield_img_meret = pygame.transform.scale(shield_img_kep,(100,80))
        shield_rect2 = shield_img_meret.get_rect(center=(1220,400))

    else:

        drawing = pygame.draw.rect(shield_draw_surf, "black", shield_draw_rect)
        r.screen.blit(shield_draw_surf, drawing)

        shield_title = r.gover_font.render("Shield", True, "white")
        shield_title_meret = pygame.transform.scale(shield_title,(300,50))
        shield_rect1 = shield_title.get_rect(center=(1280,340))
        shield_img_kep = pygame.image.load(os.path.join('assets', 'shield.png'))
        shield_img_meret = pygame.transform.scale(shield_img_kep,(100,80))
        shield_rect2 = shield_img_meret.get_rect(center=(1220,400))


#turret rész

    if turret_draw_rect.x <= mouse[0] <= turret_draw_rect.x+turret_draw_rect.w and turret_draw_rect.y <= mouse[1] <= turret_draw_rect.y+turret_draw_rect.height:
        drawing = pygame.draw.rect(turret_draw_surf, color_light, turret_draw_rect)

        turret_draw_surf.fill("#f5eeda")
        r.screen.blit(turret_draw_surf, drawing)

        turret_title = r.gover_font.render("Turret", True, "black")
        turret_title_meret = pygame.transform.scale(turret_title,(300,50))
        turret_rect1 = turret_title.get_rect(center=(1280,700))
        turret_img_kep = pygame.image.load(os.path.join('assets', 'laser.png'))
        turret_img_meret = pygame.transform.scale(turret_img_kep,(100,80))
        turret_rect2 = turret_img_meret.get_rect(center=(1220,760))

    else:

        drawing = pygame.draw.rect(turret_draw_surf, "black", turret_draw_rect)
        r.screen.blit(turret_draw_surf, drawing)

        turret_title = r.gover_font.render("Turret", True, "white")
        turret_title_meret = pygame.transform.scale(turret_title,(300,50))
        turret_rect1 = turret_title.get_rect(center=(1280,700))
        turret_img_kep = pygame.image.load(os.path.join('assets', 'laser.png'))
        turret_img_meret = pygame.transform.scale(turret_img_kep,(100,80))
        turret_rect2 = turret_img_meret.get_rect(center=(1220,760))


#back gomb

    if back_draw_rect.x <= mouse[0] <= back_draw_rect.x+back_draw_rect.w and back_draw_rect.y <= mouse[1] <= back_draw_rect.y+back_draw_rect.height:
        drawing = pygame.draw.rect(back_draw_surf, color_light, back_draw_rect)

        back_draw_surf.fill("#f5eeda")
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "black")
        back_rect = back_text.get_rect(center=(300,900))
        if r.click:
            Menu()
    else:

        drawing = pygame.draw.rect(back_draw_surf, "black",back_draw_rect)
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "white")
        back_rect = back_text.get_rect(center=(300,900))


    focsik = pygame.Surface((420,15))

    mellekcsik = pygame.Surface((416,11))
    mellekcsik.fill("white")

    egyegyseg1 = pygame.Surface((r.beolvasottadatok[0] * 83, 11))
    egyegyseg2 = pygame.Surface((r.beolvasottadatok[1] * 83, 11))
    egyegyseg3 = pygame.Surface((r.beolvasottadatok[2] * 83, 11))
    egyegyseg4 = pygame.Surface((r.beolvasottadatok[3] * 83, 11))
    egyegyseg1.fill("#de8a02")
    egyegyseg2.fill("#de8a02")
    egyegyseg3.fill("#de8a02")
    egyegyseg4.fill("#de8a02")

    vonal = pygame.Surface((2,11))
    gomb = pygame.Surface((370,50))
    gomb.fill("green")

    r.screen.blit(focsik, (450,480))
    r.screen.blit(mellekcsik, (452,482))
    r.screen.blit(egyegyseg1, (452,482))

    r.screen.blit(vonal, (533,482))
    r.screen.blit(vonal, (617,482))
    r.screen.blit(vonal, (701,482))
    r.screen.blit(vonal, (785,482))

    r.screen.blit(gomb, (475,500))

    r.screen.blit(focsik, (450,840))
    r.screen.blit(mellekcsik, (452,842))
    r.screen.blit(egyegyseg2, (452,842))

    r.screen.blit(vonal, (533,842))
    r.screen.blit(vonal, (617,842))
    r.screen.blit(vonal, (701,842))
    r.screen.blit(vonal, (785,842))

    r.screen.blit(focsik, (1010,480))
    r.screen.blit(mellekcsik, (1012,482))
    r.screen.blit(egyegyseg3, (1012,482))

    r.screen.blit(vonal, (1093,482))
    r.screen.blit(vonal, (1177,482))
    r.screen.blit(vonal, (1261,482))
    r.screen.blit(vonal, (1345,482))

    r.screen.blit(focsik, (1010,840))
    r.screen.blit(mellekcsik, (1012,842))
    r.screen.blit(egyegyseg4, (1012,842))

    r.screen.blit(vonal, (1093,842))
    r.screen.blit(vonal, (1177,842))
    r.screen.blit(vonal, (1261,842))
    r.screen.blit(vonal, (1345,842))



    r.screen.blit(coin_text, coin_rect)
    r.screen.blit(coin_szam, coin_szam_rect)
    r.screen.blit(magnet_title_meret, magnet_rect1)
    r.screen.blit(magnet_img_meret, magnet_rect2)
    r.screen.blit(turbo_title_meret, turbo_rect1)
    r.screen.blit(turbo_img_meret, turbo_rect2)
    r.screen.blit(shield_title_meret, shield_rect1)
    r.screen.blit(shield_img_meret, shield_rect2)
    r.screen.blit(turret_title_meret, turret_rect1)
    r.screen.blit(turret_img_meret, turret_rect2)
    r.screen.blit(back_text, back_rect)
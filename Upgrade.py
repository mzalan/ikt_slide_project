import pygame
import os
from Globals import *
from menu import *
from Turret import *
from Magnet import *
from Shield import *
from Turbo import *
from Save import *

def Upgrades():

    color_light = (170,170,170)
    color_dark = "#111112"
    width = r.screen.get_width()
    height = r.screen.get_height()
    mouse = pygame.mouse.get_pos()


    coin_text = r.score_font.render("Your Coins:", True, "black")
    coin_rect = coin_text.get_rect(center=(960,90))
    coin_szam = r.gover_font.render(str(r.Coins), True, "#856e1c")
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
    back_rect = back_text.get_rect(center=(300,909))


    magnet_draw_surf = pygame.Surface((450,300))
    magnet_draw_rect = magnet_draw_surf.get_rect(center=(660,440))


    turbo_draw_surf = pygame.Surface((450,300))
    turbo_draw_rect = turbo_draw_surf.get_rect(center=(660,800))


    shield_draw_surf = pygame.Surface((450,300))
    shield_draw_rect = shield_draw_surf.get_rect(center=(1220,440))


    turret_draw_surf = pygame.Surface((450,300))
    turret_draw_rect = turret_draw_surf.get_rect(center=(1220,800))


    back_draw_surf = pygame.Surface((200,80))
    back_draw_rect = back_draw_surf.get_rect(center=(300,909))


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
        back_rect = back_text.get_rect(center=(300,909))
        if r.click:
            Menu()
    else:

        drawing = pygame.draw.rect(back_draw_surf, "black",back_draw_rect)
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "white")
        back_rect = back_text.get_rect(center=(300,909))
    
    
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
    
    gomb = pygame.Surface((270,45))

    gomb_rect1 = gomb.get_rect(center=(660,540))
    gomb_rect2 = gomb.get_rect(center=(660,900))
    gomb_rect3 = gomb.get_rect(center=(1220,540))
    gomb_rect4 = gomb.get_rect(center=(1220,900))

    
    r.screen.blit(gomb, gomb_rect2)
    r.screen.blit(gomb, gomb_rect3)
    r.screen.blit(gomb, gomb_rect4)

    if gomb_rect1.x <= mouse[0] <= gomb_rect1.x+gomb_rect1.w and gomb_rect1.y <= mouse[1] <= gomb_rect1.y+gomb_rect1.height:
        drawing = pygame.draw.rect(gomb, "#e93e30", gomb_rect1)
        gomb.fill("#02e602")
        r.screen.blit(gomb, drawing)
        if r.click:
            Fejlesztes(0,"magnet")
    else:
        gomb.fill("#00c700")
        drawing = pygame.draw.rect(gomb, "#00c700", gomb_rect1)
        r.screen.blit(gomb, drawing)

    if gomb_rect2.x <= mouse[0] <= gomb_rect2.x+gomb_rect2.w and gomb_rect2.y <= mouse[1] <= gomb_rect2.y+gomb_rect2.height:
        drawing = pygame.draw.rect(gomb, "#e93e30", gomb_rect2)
        gomb.fill("#02e602")
        r.screen.blit(gomb, drawing)
        if r.click:
            Fejlesztes(1,"turbo")
    else:
        gomb.fill("#00c700")
        drawing = pygame.draw.rect(gomb, "#00c700", gomb_rect2)
        r.screen.blit(gomb, drawing)

    if gomb_rect3.x <= mouse[0] <= gomb_rect3.x+gomb_rect3.w and gomb_rect3.y <= mouse[1] <= gomb_rect3.y+gomb_rect3.height:
        drawing = pygame.draw.rect(gomb, "#e93e30", gomb_rect3)
        gomb.fill("#02e602")
        r.screen.blit(gomb, drawing)
        if r.click:
            Fejlesztes(2,"shield")
    else:
        gomb.fill("#00c700")
        drawing = pygame.draw.rect(gomb, "#00c700", gomb_rect3)
        r.screen.blit(gomb, drawing)

        
    if gomb_rect4.x <= mouse[0] <= gomb_rect4.x+gomb_rect4.w and gomb_rect4.y <= mouse[1] <= gomb_rect4.y+gomb_rect4.height:
        drawing = pygame.draw.rect(gomb, "#e93e30", gomb_rect4)
        gomb.fill("#02e602")
        r.screen.blit(gomb, drawing)
        if r.click:
            Fejlesztes(3,"turret")
    else:
        gomb.fill("#00c700")
        drawing = pygame.draw.rect(gomb, "#00c700", gomb_rect4)
        r.screen.blit(gomb, drawing)

    
    

    r.screen.blit(focsik, (450,480))
    r.screen.blit(mellekcsik, (452,482))
    r.screen.blit(egyegyseg1, (452,482))

    r.screen.blit(vonal, (533,482))
    r.screen.blit(vonal, (617,482))
    r.screen.blit(vonal, (701,482))
    r.screen.blit(vonal, (785,482))

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

    arak = []

    for i in range(0,4):
        arak.append(r.arak[r.beolvasottadatok[i]])

    if arak[0] == "MAX LEVEL!":
        szam_title1 = r.small_font.render(str(arak[0]), True, "black")
    else:
        szam_title1 = r.first_font.render(str(arak[0]), True, "black")

    if arak[1] == "MAX LEVEL!":
        szam_title2 = r.small_font.render(str(arak[1]), True, "black")
    else:
        szam_title2 = r.first_font.render(str(arak[1]), True, "black")

    if arak[2] == "MAX LEVEL!":
        szam_title3 = r.small_font.render(str(arak[2]), True, "black")
    else:
        szam_title3 = r.first_font.render(str(arak[2]), True, "black")

    if arak[3] == "MAX LEVEL!":
        szam_title4 = r.small_font.render(str(arak[3]), True, "black")
    else:
        szam_title4 = r.first_font.render(str(arak[3]), True, "black")


    szam_rect1 = szam_title1.get_rect(center=(660,540))
    szam_rect2 = szam_title2.get_rect(center=(660,900))
    szam_rect3 = szam_title3.get_rect(center=(1220,540))
    szam_rect4 = szam_title4.get_rect(center=(1220,900))

    r.screen.blit(szam_title1,szam_rect1)
    r.screen.blit(szam_title2,szam_rect2)
    r.screen.blit(szam_title3,szam_rect3)
    r.screen.blit(szam_title4,szam_rect4)
    
def Fejlesztes(ertek, nev):
    ujLista = []
    with open('progress.txt') as f:
        line = f.readline()
        c = 1
        while line:
            if line.strip().split(":")[0] == nev and int(line.strip().split(":")[1]) < 5 and r.Coins >= r.arak[r.beolvasottadatok[ertek]]:
                print(line.strip().split(":")[1])
                frissit = int(line.strip().split(":")[1]) + 1
                ujLista.append(f"{nev}:{frissit}")
                r.Coins -= r.arak[r.beolvasottadatok[ertek]]
                r.beolvasottadatok[ertek] += 1
                print(frissit)
            else:
                ujLista.append(line.strip())
            line = f.readline()
            c += 1
    f.close()
    fa = open("progress.txt", "w", encoding="utf-8")
    for i in range(len(ujLista)):
        fa.write(f"{ujLista[i]}\n")
        print(ujLista[i])
    fa.close()


# def Fejlesztes(ertek, nev):
#     f = open("progress.txt", "a", encoding="utf-8")
#     f[ertek].write(f"{nev}:{r.beolvasottadatok[ertek]+1}")
#     f.close()
#     Fajlolvas()
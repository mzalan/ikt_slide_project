from Globals import * 

shot_time = 0
pre_ammo = 0
def PowerupActivation(img, i, pos):
    global pre_ammo
    global shot_time

    duration = r.power_upgrades[r.powerups[i][0]]

    surf = pygame.Surface((90,90))
    width = surf.get_rect().width
    height = surf.get_rect().height
    surf = pygame.transform.scale(img, (width, height))

    base = pygame.Surface((350,60))
    base.fill("#1294ff")

    icon = pygame.Surface((50,50))
    width = icon.get_rect().width
    height = icon.get_rect().height
    icon = pygame.transform.scale(img, (width, height))

    progb = pygame.Surface((285, 50))
    progb.fill("#063257")

    vividness = 252
    rect = surf.get_rect(topleft=(r.player_rect.x + 5,r.player_rect.y + 5))

    prog = pygame.Surface((285 - ((r.runs - r.powerups[i][1])/duration * 285),50))

    if r.runs - r.powerups[i][1] <= duration/2:
        prog.fill((vividness*((r.runs - r.powerups[i][1])/((duration)/2)),vividness, 0))
    else:
        try:
            prog.fill((vividness,int(vividness-(vividness*((r.runs - (r.powerups[i][1] + duration/2))/duration))*2.03), 0))
        except:
            prog.fill((vividness, 0, 0))
        

    if r.powerups[i][0] == 3:
        if pre_ammo != None and pre_ammo > r.ammo:
            shot_time = r.runs
            
        if shot_time != None and r.runs - shot_time > 20 and r.ammo < 4:
            r.ammo += 1
            shot_time = r.runs

        

        pre_ammo = r.ammo
        
        abase = pygame.Surface((100,15))

        ammo = pygame.Surface((96,11))
        ammo.fill("white")
        
        ammo_prog = pygame.Surface((r.ammo * 24,11))
        ammo_prog.fill("#de8a02")

        line = pygame.Surface((2,11))

        r.screen.blit(abase, (r.player_rect.x, r.player_rect.y+100))
        r.screen.blit(ammo, (r.player_rect.x+2, r.player_rect.y+102))
        r.screen.blit(ammo_prog, (r.player_rect.x+2, r.player_rect.y+102))

        r.screen.blit(line, (r.player_rect.x+24, r.player_rect.y+102))
        r.screen.blit(line, (r.player_rect.x+49, r.player_rect.y+102))
        r.screen.blit(line, (r.player_rect.x+74, r.player_rect.y+102))


    r.screen.blit(surf,rect)
    r.screen.blit(base,(0 + pos,1020))
    r.screen.blit(icon,(5 + pos,1025))
    r.screen.blit(progb, (60 + pos,1025))
    r.screen.blit(prog, (60 + pos,1025))

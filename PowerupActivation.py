from Globals import * 


def PowerupActivation(img, i, pos):
    
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
    progb.fill("white")

    vividness = 252
    rect = surf.get_rect(topleft=(r.player_rect.x + 5,r.player_rect.y + 5))
    
    print(r.powerups[i])
    prog = pygame.Surface((285 - ((r.runs - r.powerups[i][0])/1000 * 285),50))

    if r.runs - r.powerups[i][0] <= 500:
        prog.fill((vividness*((r.runs - r.powerups[i][0])/500),vividness, 0))
    else:
        try:
            prog.fill((vividness,int(vividness-(vividness*((r.runs - (r.powerups[i][0] + 500))/1000))*2.03), 0))
        except:
            prog.fill((vividness, 0, 0))
        

    r.screen.blit(surf,rect)
    r.screen.blit(base,(0 + pos,1020))
    r.screen.blit(icon,(5 + pos,1025))
    r.screen.blit(progb, (60 + pos,1025))
    r.screen.blit(prog, (60 + pos,1025))
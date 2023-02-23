from Globals import * 


img = pygame.image.load(os.path.join('assets', 'magnet.png'))


def MagnetActivation():
    surf = pygame.Surface((100,100))
    width = surf.get_rect().width
    height = surf.get_rect().height
    surf = pygame.transform.scale(img, (width, height))
    rect = surf.get_rect(topleft=(r.player_rect.x,r.player_rect.y))
    
    r.screen.blit(surf,rect)
import pygame
import pygame.draw


pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Slicky Slide")
clock = pygame.time.Clock()


player = pygame.Surface((100,100))
player.fill("red")
player_rect = player.get_rect(center=(960,930))

moveD = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveD.append(1)
            if event.key == pygame.K_RIGHT:
                moveD.append(2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveD = 1
            if event.key == pygame.K_RIGHT:
                moveD = 2
        
    screen.fill("lightblue")
    screen.blit(player, player_rect)

    if moveD == 1:
        player_rect.x -= 5
    if moveD == 2:
        player_rect.x += 5

    pygame.display.update()
    clock.tick(60)

    

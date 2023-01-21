import pygame

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Slicky Slide")
clock = pygame.time.Clock()


player = pygame.Surface((100,100))

player_rect = player.get_rect(center=(960,930))

speed_font = pygame.font.Font(None, 50)

leftRight = [False,False]
moveD = False
speed = 11
boost = 0.5
boosting = False

def KeyupControls(dirIndex, comp, isMoveD):
    global leftRight
    leftRight[dirIndex] = False
    global moveD
    moveD = isMoveD
    if not leftRight[comp]:
        global speed
        speed = 11
        global boost
        boost = 0.5

def KeydownControls(dirIndex, comp, isMoveD):
    global leftRight
    leftRight[dirIndex] = True
    global moveD
    moveD = isMoveD
    if leftRight[comp]:
        global boost
        boost = 0
        global boosting
        boosting = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                KeyupControls(0, 1, False)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                KeyupControls(1, 0, True) 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                KeydownControls(0, 1, True)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                KeydownControls(1, 0, False)
    

    screen.fill("lightblue")


    if boosting:
        boost += 0.003
        if boost >= 0.5:
            boosting = False
            boost = 0.5
    if player_rect.x >= 0:
        if moveD and leftRight[0]:
            if speed < 38:
                speed += boost            
            else:
                speed = 38
            player_rect.x -= speed
        if player_rect.x < 0:
            player_rect.x = 0
        if not moveD and leftRight[1]:
            if speed < 38:
                speed += boost            
            else:
                speed = 38
            player_rect.x += speed
        if player_rect.x > 1820:
            player_rect.x = 1820

    


    greenness = int((str(255-((255/27)*(speed-11)))).split(".")[0])
    screen.blit(player, player_rect)

    if greenness < 0:
        greenness = 0
    player.fill(pygame.Color(255, greenness, 0))

    speed_text = speed_font.render(str(speed), True, "black")
    screen.blit(speed_text,(5,5))

    
    pygame.display.update()
    clock.tick(60)

    

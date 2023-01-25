import pygame

pygame.init()




class coins:
    def __init__(self,x,y,height,width,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect((x,y), (width,height))
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(255, 255, 0, self.rect)



# --------------------------define coins colors and width,heights anD coins LIST
coins.__init__(height=50, width=50, color=(255, 255, 0))
coin1 = coins(50,50)
coin2 = coins(50,50)
coin3  = coins(50,50)
coin4 = coins(50,50)
coin5  = coins(50,50)
Coins_list = [coin1,coin2,coin3,coin4,coin5]

pygame.display.update()
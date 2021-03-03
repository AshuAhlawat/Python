import pygame
pygame.init()

# Window Setup 
screen = pygame.display.set_mode((1000,600))
tank = pygame.image.load("tank.png")
pygame.display.set_icon(tank)
pygame.display.set_caption("Tanks")

# ENTITIES
#bullet

#player
playerX = 480
playerY = 100
playerX_p = 0
playerX_m = 0
playerY_p = 0
playerY_m = 0

def player(x,y):
    screen.blit(tank, (x,600 - y))

# Game Loop 
running = 1
while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_m = -0.15
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_p = 0.15
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_p = 0.2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_m = -0.1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_m = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_p = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_p = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_m = 0
        
    #entities
    screen.fill((25,50,25))
    playerX += playerX_p + playerX_m
    playerY += playerY_p + playerY_m
    if playerX<0-4:
        playerX=0-4
    elif playerX>1000-60:
        playerX=1000-60
    if playerY<0+64:
        playerY=0+64
    elif playerY>600+14:
        playerY=600+14
    player(playerX,playerY)
    
    #refreshing display
    pygame.display.update()
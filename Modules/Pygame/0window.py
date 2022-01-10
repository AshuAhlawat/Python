# IMPORTS  
import pygame
pygame.init()

# Creating Screen 
screen = pygame.display.set_mode((800,600))

# Title
pygame.display.set_caption("Hello World")
# Icon
yt_icon = pygame.image.load(r"./graphic-tablet.png")
pygame.display.set_icon(yt_icon)

# Game Status 
running = True

# MAIN GAME LOOP 
while running:
    #Events Checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((25,25,50))
    
    
    #Refreshing Screen
    pygame.display.update()
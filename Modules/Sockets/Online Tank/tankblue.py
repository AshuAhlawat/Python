import socket

#CONSTANTS
PORT = 5555
SERVER = "192.168.29.87"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

import pygame
pygame.init()

# Window Setup 
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Blue")

# ENTITIES

blue_tank = pygame.image.load(r"C:\Users\ashua\OneDrive\Desktop\Coding\Python\Modules\Sockets\Online Tank\bluetank.png")
green_tank = pygame.image.load(r"C:\Users\ashua\OneDrive\Desktop\Coding\Python\Modules\Sockets\Online Tank\greentank.png")

blueX = 520
blueY = 500
blueX_p = 0
blueX_m = 0
blueY_p = 0
blueY_m = 0

def send_pos(x,y):
    screen.blit(blue_tank, (x,600 - y))
    client.send(f"{x},{600-y}".encode())

def get_pos():
    green = client.recv(256).decode()
    green=green.split(",")
    x=int(green[0])
    y=int(green[1])
    screen.blit(green_tank, (x,y))

# Game Loop 
running = 1
while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client.send(f"!Logout".encode())
            running = False
        
        #movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                blueX_m = -1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                blueX_p = 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                blueY_p = 2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                blueY_m = -1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                blueX_m = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                blueX_p = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                blueY_p = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                blueY_m = 0
        
    #entities
    screen.fill((25,50,25))
    blueX += blueX_p + blueX_m
    blueY += blueY_p + blueY_m
    
    if blueX<0-4:
        blueX=0-4
    elif blueX>1000-60:
        blueX=1000-60
    if blueY<0+44:
        blueY=0+44
    elif blueY>600:
        blueY=600

    send_pos(round(blueX),round(blueY))
    get_pos()
    
    #refreshing display
    pygame.display.update()
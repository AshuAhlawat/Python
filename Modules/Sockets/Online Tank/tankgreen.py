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
pygame.display.set_caption("Green")

# ENTITIES

blue_tank = pygame.image.load(r"C:\Users\ashua\OneDrive\Desktop\Coding\Python\Modules\Sockets\Online Tank\bluetank.png")
green_tank = pygame.image.load(r"C:\Users\ashua\OneDrive\Desktop\Coding\Python\Modules\Sockets\Online Tank\greentank.png")

greenX = 480
greenY = 100
greenX_p = 0
greenX_m = 0
greenY_p = 0
greenY_m = 0

def send_pos(x,y):
    screen.blit(green_tank, (x,600 - y))
    client.send(f"{x},{600-y},".encode()) 
    
def get_pos():
    blue = client.recv(256).decode()
    blue=blue.split(",")
    x=int(blue[0])
    y=int(blue[1])
    screen.blit(blue_tank, (x,y))

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
                greenX_m = -1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                greenX_p = 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                greenY_p = 2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                greenY_m = -1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                greenX_m = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                greenX_p = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                greenY_p = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                greenY_m = 0
        
    #entities
    screen.fill((25,50,25))
    greenX += greenX_p + greenX_m
    greenY += greenY_p + greenY_m
    
    if greenX<0-4:
        greenX=0-4
    elif greenX>1000-60:
        greenX=1000-60
    if greenY<0+64:
        greenY=0+64
    elif greenY>600+14:
        greenY=600+14

    send_pos(round(greenX),round(greenY))
    get_pos()
    
    #refreshing display
    pygame.display.update()
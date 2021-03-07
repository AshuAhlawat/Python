import pygame
from pygame import mixer
from random import randrange,choice
pygame.init()

def pos():
    if direction:
        if direction=="left":
            if state=="down":
                screen.blit(soldier_down_left, (512,y))
            else:
                screen.blit(soldier_up_left, (512,y))
        if direction=="right":
            if state=="down":
                screen.blit(soldier_down_right, (512,y))
            else:
                screen.blit(soldier_up_right, (512,y))
    else:
        screen.blit(soldier_rest, (512,y))

def fire():
    global super_bullet
    global fired
    global x
    fired = 1
    
    if bullet_path=="left":
        screen.blit(bullet_left, (x-10,y+20))
        x -= 5
    if bullet_path=="right":
        screen.blit(bullet_right, (x+45,y+20))
        x += 5
    if x<0 or x > 1000:
        fired=0
        x=512
    
    super_bullet=0

def superfire():
    global super_bullet
    global fired
    global x
    fired = 1
    
    if bullet_path=="left":
        screen.blit(pygame.transform.scale2x(bullet_left), (x-10,y+10))
        x -= 8
    if bullet_path=="right":
        screen.blit(pygame.transform.scale2x(bullet_right), (x+45,y+10))
        x += 8
    if x< -600 or x > 1600:
        fired=0
        x=512

    super_bullet=1

def spawn_snake_left():
    new_snake = snake_left.get_rect(midright = (randrange(-600, 100,5),684))
    return new_snake
def spawn_snake_right():
    new_snake = snake_left.get_rect(midleft = (randrange(1020, 1520,5),684))
    return new_snake

def move_snakes_left(snakes):
    for snake in snakes:
        snake.centerx+=3
    return snakes
def move_snakes_right(snakes):
    for snake in snakes:
        snake.centerx-=3
    return snakes

def draw_snakes_left(snakes):
    for snake in snakes:
        screen.blit(snake_left, snake)
def draw_snakes_right(snakes):
    for snake in snakes:
        screen.blit(snake_right, snake)

def collision(snakes_left,snakes_right):
    global score
    global fired
    global x
    if super_bullet:
        for snake in snakes_left:
            if abs(snake.right - 512) < 5:
                print(score)
                pygame.quit()
            if abs(snake.centerx - x + 15) < 5:
                snakes_left.remove(snake)
                score += 1
        for snake in snakes_right:
            if abs(snake.left - 552) < 5:
                print(score)
                pygame.quit()
            if abs(snake.centerx - x - 40) < 5:
                snakes_right.remove(snake)
                score += 1
    else:
        for snake in snakes_left:
            if abs(snake.right - 512) < 5:
                print(score)
                pygame.quit()
            if abs(snake.centerx - x + 15) < 5:
                snakes_left.remove(snake)
                score += 1
                fired = 0
                x = 512
        for snake in snakes_right:
            if abs(snake.left - 552) < 5:
                print(score)
                pygame.quit()
            if abs(snake.centerx - x - 40) < 5:
                snakes_right.remove(snake)
                score += 1
                fired = 0
                x = 512

def draw_score():
    screen.blit(heading_font.render("SOLDIER", True, (0, 0, 0)), (370, 250))
    screen.blit(score_font.render("Score : " + str(score), True, (0, 0, 0)), (860, 20))

# Textures
    #soldier
direction=""
state = "up"
jump = "no"
y = 650
soldier_rest = pygame.image.load("assets/standmid.png")
soldier_up_left = pygame.image.load("assets/standleft.png")
soldier_up_right = pygame.image.load("assets/standright.png")
soldier_down_right = pygame.image.load("assets/crouchright.png")
soldier_down_left = pygame.image.load("assets/crouchleft.png")
soldier_jump = pygame.image.load("assets/jump.png")

    #bullet
fired=0
bullet_path=""
super_bullet=0
x = 512
bullet_left = pygame.image.load("assets/bulletleft.png")
bullet_right = pygame.image.load("assets/bulletright.png")

    #snake
snake_y=  650+10
snake_left = pygame.image.load("assets/snakeleft.png")
snake_right = pygame.image.load("assets/snakeright.png")
snake_list_left=[]
snake_list_right=[]
SPAWNSNAKE = pygame.USEREVENT
pygame.time.set_timer(SPAWNSNAKE,3000)

    #score
score = 0
score_font = pygame.font.Font('freesansbold.ttf',32)
heading_font = pygame.font.Font('freesansbold.ttf',80)


# Video
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1024,724))
# Audio
mixer.music.load("assets/theme.wav")
mixer.music.play(-1)

while 1:
    screen.fill((25,50,25))
    pygame.draw.rect(screen, (0,0,0), (0, 683, 1024, 5),1)
    draw_score()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = "left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = "right"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                state = "down"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                jump = "yes"
        
        if event.type == SPAWNSNAKE:
            choice([snake_list_left.append(spawn_snake_left()),snake_list_right.append(spawn_snake_right())])
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                state = "up"
        
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if not fired:
                fired=1
                bullet_path = direction
                if state =="up":
                    super_bullet = 0
                else:
                    super_bullet = 1
    
    # Bullet
    if fired:
        if super_bullet:
            mixer.Sound("assets/superfire.wav").play()
            superfire()
        else:
            mixer.Sound("assets/fire.wav").play()
            fire()
            
    # Soldier 
    pos()
    
    # Snake
    snake_list_left = move_snakes_left(snake_list_left)
    snake_list_right = move_snakes_right(snake_list_right)
    draw_snakes_left(snake_list_left)
    draw_snakes_right(snake_list_right)
    
    # Collision
    collision(snake_list_left,snake_list_right)
    
    pygame.display.update()
    clock.tick(60)
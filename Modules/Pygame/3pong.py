import pygame,sys,random


def draw(object):
    pygame.draw.rect(screen, (255, 255, 255), object)

def bar(barX, barY):
    return pygame.Rect(barX, barY, 8, 80)

def ball(ballX, ballY):
    return pygame.Rect(ballX, ballY, 20, 20)

def write(text, size, dim):
    text = str(text)
    font = pygame.font.Font('freesansbold.ttf',size)
    screen.blit(font.render(text, True, (255, 255, 255)), dim)

# GENERAL SETUP
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Pong')

# ENTITIES
#bar
left_change_m = 0
right_change_p = 0
left_change_p = 0
right_change_m = 0
left_bar = bar(0, 300)
right_bar = bar(1000-8, 300)

left_lives = 3
right_lives = 3

#ball
ballX = 500
ballY = 300
ballY_change = 0
ballX_change = random.choice([5,-5])
ball = ball(ballX,ballY)

# GAME LOOP
while True:
    screen.fill((10,20,20))
    pygame.draw.rect(screen, (255,255,255), (500 , 0, 1, 600))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_change_m -= 3
            if event.key == pygame.K_s:
                left_change_p += 3
            if event.key == pygame.K_UP:
                right_change_m -= 3
            if event.key == pygame.K_DOWN:
                right_change_p += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_change_m = 0
            if event.key == pygame.K_s:
                left_change_p = 0
            if event.key == pygame.K_UP:
                right_change_m = 0
            if event.key == pygame.K_DOWN:
                right_change_p = 0
            
    #bars mechanics
    left_bar.centery += left_change_m + left_change_p
    right_bar.centery += right_change_m + right_change_p
    
    if left_bar.centery < 40:
        left_bar.centery = 40
    elif left_bar.centery > 560:
        left_bar.centery = 560
    if right_bar.centery < 40:
        right_bar.centery = 40
    elif right_bar.centery > 560:
        right_bar.centery = 560
    
    #ball mechanics
    ball.centery += ballY_change
    ball.centerx += ballX_change
    
    if ball.left < 0 :
        ball.centerx = 500
        ball.centery = 300
        ballY_change = 0
        ballX_change = random.choice([5,-5])
        left_lives -= 1
    elif ball.right >1000:
        ball.centerx = 500
        ball.centery = 300
        ballY_change = 0
        ballX_change = random.choice([5,-5])
        right_lives -= 1
    
    if ball.centery < 10:
        ball.centery = 10
        ballY_change *= -1
    elif ball.centery > 590:  
        ball.centery = 590 
        ballY_change *= -1

    #collision
    if ball.colliderect(left_bar):
        dist = left_bar.centery - ball.centery
        if  dist > 0:
            ballY_change = -5*dist/40
        if  dist <= 0:
            ballY_change = -5*dist/40
        ballX_change *= -1
    
    if ball.colliderect(right_bar):
        dist = right_bar.centery - ball.centery
        if  dist > 0:
            ballY_change = -5*dist/40
        if  dist <= 0:
            ballY_change = -5*dist/40
        ballX_change *= -1
            

    draw(left_bar)
    draw(right_bar)
    draw(ball)
    
    if left_lives <= 0: 
        write("RIGHT WINS",70, (300,270))
    elif right_lives <=0:
        write("LEFT WINS",70, (325,270))
    else:
        write(left_lives, 24 ,(400,300))
        write(right_lives, 24 ,(600,300))
        
    
    pygame.display.update()
    clock.tick(60)
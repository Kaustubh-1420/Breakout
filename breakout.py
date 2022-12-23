import pygame
from pygame.locals import *
import sys
from breakout_sprites import *

# game init
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.key.set_repeat(400, 30)
clock = pygame.time.Clock()

# title and icon
pygame.display.set_caption("Breakout")
icon = pygame.image.load('ball.png')
pygame.display.set_icon(icon)

# groups
all_sprites_group = pygame.sprite.Group()
player_bricks_group = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()

# add sprites to their group
ball = Ball('ball.png', BALL_SPEED, -BALL_SPEED)
all_sprites_group.add(ball)

# player
player = Player('player.png')
all_sprites_group.add(player)
player_bricks_group.add(player)

# score
score = 0
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# highscore
f=open('highscore.txt', 'r+')
for line in f:
    pass
last_line = line
highscore_value=int(last_line)

# Font
over_font = pygame.font.Font('freesansbold.ttf', 32)

def show_highscore(x, y):
    highscore = font.render("High Score :" + str(highscore_value), True, (225, 255, 255))
    window.blit(highscore, (x, y))

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (225, 255, 255))
    window.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (225, 255, 255))
    window.blit(over_text, (300, 250))

# Loop for number of brickes.
for i in range(10):
    for j in range(10):
        brick = Brick('brick.png', (i+1)*BRICK_WIDTH + 5, (j+3)*BRICK_HEIGHT + 5)
        all_sprites_group.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)

# game loop
menu = True 

while True:
    while menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False

            window.fill((0, 0, 0))
            clock.tick(10)
            start_text = over_font.render("Press SPACE to PLAY GAME!!!", True, (225, 255, 255))
            pause_text = over_font.render("Press P to Pause the GAME", True, (225, 255, 255))
            window.blit(start_text, (160, 240))
            window.blit(pause_text, (175, 270))
            pygame.display.update()
    
    # game over
    if ball.rect.y > WINDOW_HEIGHT:
        window.fill((0, 0, 0))
        clock.tick(10)
        game_over_text()
        pygame.display.update()  # till here start menu
        if score_value > highscore_value:
            f.write('\n')
            f.write(str(score_value))
            f.close()
        print('Game Over')
        pygame.quit()
        sys.exit()

    # move player horizontally
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()

    # collision detection (ball bounce against brick & player)
    hits = pygame.sprite.spritecollide(ball, player_bricks_group, False)
    if hits:
        hit_rect = hits[0].rect
        # bounce the ball (according to side collided)
        if hit_rect.left > ball.rect.left or ball.rect.right < hit_rect.right:
            ball.speed_y *= -1
        else:
            ball.speed_x *= -1

        # collision with blocks
        if pygame.sprite.spritecollide(ball, bricks_group, True):
            score_value += 1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            menu = True
            

    # render groups
    window.fill((0, 0, 0))
    all_sprites_group.draw(window)
    show_highscore(550,10)
    show_score(textX, textY)

    # refresh screen
    all_sprites_group.update()
    clock.tick(60)
    pygame.display.update()



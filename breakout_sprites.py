import pygame
import random
# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 540
BALL_WIDTH, BALL_HEIGHT = 16, 16
BRICK_WIDTH, BRICK_HEIGHT = 64, 16
PLAYER_WIDTH, PLAYER_HEIGHT = 64, 16
PLAYER_SPEED = 20
BALL_SPEED = 3
class Breakout_Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)

        # load image & rect
        self.image = pygame.image.load('images/' + image_file).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

class Player(Breakout_Sprite):

    def __init__(self, image_file):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.left = (WINDOW_WIDTH - self.image.get_width()) / 2

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-PLAYER_SPEED, 0)

    def move_right(self):
        if self.rect.right < WINDOW_WIDTH:
            self.rect.move_ip(PLAYER_SPEED, 0)

class Brick(Breakout_Sprite):

    def __init__(self, image_file, x, y):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.x, self.rect.y = x, y

class Ball(Breakout_Sprite):

    def __init__(self, image_file, speed_x, speed_y):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.bottom =random.randint(420,465)
        self.rect.left = WINDOW_WIDTH / 2
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        # bounce against borders
        if self.rect.x > WINDOW_WIDTH - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1

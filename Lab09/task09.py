import pygame, sys 
from pygame.locals import *
import random, time
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0

font = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Falling Objects")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-7, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(7, 0)

class Triangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.randint(1, 3)
        self.size = 20

        self.x = random.randint(20, SCREEN_WIDTH - 20)
        self.y = 0
        self.speed = 5

        self.rect = pygame.Rect(self.x - self.size, self.y,
                                self.size * 2, self.size * 2)

    def move(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y > SCREEN_HEIGHT:
            self.kill()    

    def draw(self):
        p1 = (self.x, self.y)
        p2 = (self.x - self.size, self.y + self.size)
        p3 = (self.x + self.size, self.y + self.size)
        pygame.draw.polygon(DISPLAYSURF, RED, [p1, p2, p3])


P1 = Player()
triangles = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN, 700)

while True:
   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SPAWN:
            T = Triangle()
            triangles.add(T)
            all_sprites.add(T)

    DISPLAYSURF.fill(WHITE)

    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    for entity in all_sprites:
        if isinstance(entity, Triangle):
            entity.draw()
        else:
            DISPLAYSURF.blit(entity.image, entity.rect)

        entity.move()

    hits = pygame.sprite.spritecollide(P1, triangles, True)
    for t in hits:
        SCORE += t.weight

    pygame.display.update()
    FramePerSec.tick(FPS)
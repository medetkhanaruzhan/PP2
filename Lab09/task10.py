import pygame, sys, random
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task 10")

WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 30)

speed = 6
score = 0

player_x = WIDTH // 2
player_y = HEIGHT // 2
size = 25

def draw_player(x, y):
    p1 = (x, y - size)
    p2 = (x - size, y + size)
    p3 = (x + size, y + size)
    pygame.draw.polygon(screen, BLUE, [p1, p2, p3])
    return [p1, p2, p3]

circle_x = random.randint(30, WIDTH - 30)
circle_y = random.randint(30, HEIGHT - 30)
circle_r = 12

def respawn_circle():
    return random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_LEFT] or keys[K_a]:
        player_x -= speed
    if keys[K_RIGHT] or keys[K_d]:
        player_x += speed
    if keys[K_UP] or keys[K_w]:
        player_y -= speed
    if keys[K_DOWN] or keys[K_s]:
        player_y += speed

    if player_x < size: player_x = size
    if player_x > WIDTH - size: player_x = WIDTH - size
    if player_y < size: player_y = size
    if player_y > HEIGHT - size: player_y = HEIGHT - size

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_r)
    draw_player(player_x, player_y)

    if (player_x - circle_x)**2 + (player_y - circle_y)**2 <= (circle_r + size)**2:
        score += random.randint(1, 5)
        circle_x, circle_y = respawn_circle()

    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (15, 15))

    pygame.display.update()
    clock.tick(60)
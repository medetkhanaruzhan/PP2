import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("moving square")
clock = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = 50
step = 10

pos_x = WIDTH // 2 - size // 2
pos_y = HEIGHT // 2 - size // 2

font = pygame.font.SysFont("Verdana", 20)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, (pos_x, pos_y, size, size))

    #text = font.render(f"x = {pos_x}, y = {pos_y}", True, RED)
    text = font.render("x=" + str(pos_x)+ "y=" + str(pos_y),True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
    
            if event.key == K_LEFT:
                if pos_x - step >= 0:
                    pos_x -= step

            elif event.key == K_RIGHT:
                if pos_x + size + step <= WIDTH:
                    pos_x += step

            elif event.key == K_UP:
                if pos_y - step >= 0:
                    pos_y -= step

            elif event.key == K_DOWN:
                if pos_y + size + step <= HEIGHT:
                    pos_y += step

            elif event.key == K_SPACE:
                pos_x = WIDTH // 2 - size // 2
                pos_y = HEIGHT // 2 - size // 2

    clock.tick(20)

pygame.quit()

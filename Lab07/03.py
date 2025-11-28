import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

pos_x = 400
pos_y = 250
radius = 25
step = 20

running = True
while running:
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, "red", (pos_x, pos_y), radius)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and pos_y + radius + step <= 500:
                pos_y += step
            elif event.key == pygame.K_UP and pos_y - radius - step >= 0:
                pos_y -= step
            elif event.key == pygame.K_LEFT and pos_x - radius - step >= 0:
                pos_x -= step
            elif event.key == pygame.K_RIGHT and pos_x + radius + step <= 500:
                pos_x += step

    clock.tick(20)

pygame.quit()
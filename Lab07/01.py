import pygame
import datetime

pygame.init()

clock_face = pygame.image.load("photos/base_micky.jpg")
minute_hand = pygame.image.load("photos/minute.png")
second_hand = pygame.image.load("photos/second.png")

WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

extra_width = 100
clock_face = pygame.transform.smoothscale(clock_face, (WIDTH + extra_width, HEIGHT - 50))

bg_x_offset = -extra_width // 2
bg_y_offset = 25 

def rotate_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)  
    rotated_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rotated_rect


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(clock_face, (bg_x_offset, bg_y_offset))

    now = datetime.datetime.now()
    minutes = now.minute + now.second / 60.0
    seconds = now.second + now.microsecond / 1e6

    minute_angle = (minutes / 60.0) * 360.0
    second_angle = (seconds / 60.0) * 360.0

    rotated_minute_hand, minute_rect = rotate_hand(minute_hand, minute_angle, (CENTER_X, CENTER_Y))
    rotated_second_hand, second_rect = rotate_hand(second_hand, second_angle, (CENTER_X, CENTER_Y))
    
    screen.blit(rotated_minute_hand, minute_rect)
    screen.blit(rotated_second_hand, second_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
import pygame, sys, random, time
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 500, 540
CELL = 24

GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

score = 0
level = 1
speed = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("nostalgia")

font_big = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 18)
game_over = font_big.render("Вы проиграли :(", True, RED)

clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [(120, 120), (96, 120), (72, 120)]
        self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL
        elif self.direction == "DOWN":
            y += CELL
        elif self.direction == "LEFT":
            x -= CELL
        elif self.direction == "RIGHT":
            x += CELL
        new_head = (x, y)
        self.body.insert(0, new_head)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL, CELL))

    def hit_wall_or_self(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False


class Food:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, CELL, CELL)
        self.weight = random.randint(1, 3)    # вес еды
        self.timer = 100                      # таймер жизни еды
        self.random_position()

    def random_position(self):
        while True:
            x = random.randrange(0, WIDTH // CELL) * CELL
            y = random.randrange(0, HEIGHT // CELL) * CELL
            if (x, y) not in snake.body:
                self.rect.topleft = (x, y)
                break

        self.weight = random.randint(1, 3)    # новый вес
        self.timer = 35                     # сброс таймера

    def update(self):
        self.timer -= 1
        if self.timer <= 0:                   # если еду НЕ съели вовремя
            self.random_position()            # сразу перемещаем

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)


snake = Snake()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    snake.move()

    
    if snake.hit_wall_or_self():
        screen.fill(BLACK)
        screen.blit(game_over, (88, 140))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    
    if snake.body[0] == food.rect.topleft:
        score += food.weight
        if score % 3 == 0:
            level += 1
            speed += 2
        food.random_position()
    else:
        snake.body.pop()

    screen.fill(BLACK)
    snake.draw()

    food.update()  
    food.draw()

    score_text = font_small.render("Score: " + str(score), True, WHITE)
    level_text = font_small.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (420, 10))

    pygame.display.update()
    clock.tick(speed)
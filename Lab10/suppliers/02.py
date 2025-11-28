import pygame, sys, random, time
import psycopg2
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

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5434"
)
cursor = conn.cursor()

def login():
    username = input("Введите ваш username: ")

    cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute(
            "INSERT INTO users(username) VALUES(%s) RETURNING id",
            (username,)
        )
        user_id = cursor.fetchone()[0]

        cursor.execute(
            "INSERT INTO user_score(user_id, level, score, speed) VALUES(%s,1,0,10)",
            (user_id,)
        )
        conn.commit()

        print("Создан новый пользователь:", username)
        return user_id, 1, 0, 10

    user_id = row[0]
    cursor.execute(
        "SELECT level, score, speed FROM user_score WHERE user_id=%s",
        (user_id,)
    )
    level, score, speed = cursor.fetchone()

    print(f"Добро пожаловать, {username}! Ваш уровень: {level}, очки: {score}")
    return user_id, level, score, speed


def save_state(user_id, level, score, speed):
    cursor.execute(
        "UPDATE user_score SET level=%s, score=%s, speed=%s WHERE user_id=%s",
        (level, score, speed, user_id)
    )
    conn.commit()
    print("Сохранено!")


user_id, level, score, speed = login()
paused = False

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
        self.weight = random.randint(1, 3)
        self.timer = 100
        self.random_position()

    def random_position(self):
        while True:
            x = random.randrange(0, WIDTH // CELL) * CELL
            y = random.randrange(0, HEIGHT // CELL) * CELL
            if (x, y) not in snake.body:
                self.rect.topleft = (x, y)
                break

        self.weight = random.randint(1, 3)
        self.timer = 35

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.random_position()

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)


snake = Snake()
food = Food()


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            save_state(user_id, level, score, speed)
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:

            if event.key == K_p:
                paused = not paused
                if paused:
                    save_state(user_id, level, score, speed)

            if event.key == K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"


    if paused:
        pause_text = font_big.render("Пауза", True, WHITE)
        screen.blit(pause_text, (160, 200))
        pygame.display.update()
        continue


    snake.move()

    if snake.hit_wall_or_self():
        save_state(user_id, level, score, speed)
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
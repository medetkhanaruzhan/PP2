#1 рэйсееер 
import pygame, sys #пайгейм понятно а сис позволяет программе взаимодействовать с самой системой
from pygame.locals import * #импортируем все из модуля локал он дает нам доступ к константам пайгейма
import random, time #импортируем рандом для генерации случайных чисел и тайм для работы со временем
pygame.init() #инициализация пайгейма

FPS = 60 #частота кадров в секунду
FramePerSec = pygame.time.Clock() #для контроля частоты кадров

BLUE  = (0, 0, 255) 
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5 #базовая скорость падения врагов
SCORE = 0 
COINS = 0 
 
font = pygame.font.SysFont("Verdana", 60) #создаем два системных шрифта
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK) #рендер заранее готовит обложку с надписью гейм овер 
 
background = pygame.image.load("images/AnimatedStreet.png") #загружаем картинку дороги

DISPLAYSURF = pygame.display.set_mode((400,600)) #создаем окно 400 на 600
DISPLAYSURF.fill(WHITE) #заполняем его белым цветом
pygame.display.set_caption("Game") #заголовок игры
 # Спрайт это игровой обьект = картинка + координаты + логика поведения
class Enemy(pygame.sprite.Sprite): #класс для вражеской машины
      def __init__(self): 
        super().__init__() #вызывает конструктор родительского класса Sprite.
        #Это нужно, чтобы корректно инициализировать внутренние поля, которые использует Pygame (например, группы, события и т.п.)

        self.image = pygame.image.load("images/Enemy.png") #загружаем картинку врага
        self.rect = self.image.get_rect() #получаем прямоугольник картинки для позиционирования
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  #устанавливаем начальную позицию врага в случайно точке сверху экрана
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
       
P1 = Player()
E1 = Enemy()
C1 = Coin() 

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()  
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)  
    DISPLAYSURF.blit(coin_text, (300,10))  
 
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('sounds/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        

    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        for coin in coins:
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
         
    pygame.display.update()
    FramePerSec.tick(FPS)




#3 пэйнтиииик
import pygame #импортируем библиотеку пайгейм

def main(): #инициализация главной функции
    pygame.init()
    screen = pygame.display.set_mode((640, 480)) #создаем окно программы
    pygame.display.set_caption("Paint") #задаем название окну
    clock = pygame.time.Clock() #для контроля частоты кадров

    mode = None #переменная для хранения текущего режима рисования
    color = (255, 255, 255) #цвет по умолчанию - белый
    start = None #переменная для хранения начальной точки рисования
    
    while True: #главный цикл программы
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #выход из программы
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #выход по нажатию эскейпа
                    return
                if event.key == pygame.K_r: #переключение в режим рисования прямоугольников
                    mode = "rect"
                elif event.key == pygame.K_c: #переключение в режим рисования кругов
                    mode = "circle"
                elif event.key == pygame.K_e: #переключение в режим стирания
                    mode = "erase"
                elif event.key == pygame.K_1: #смена цвета на красный
                    color = (255, 0, 0)
                elif event.key == pygame.K_2: #смена цвета на зеленый
                    color = (0, 255, 0)
                elif event.key == pygame.K_3: #смена цвета на синий
                    color = (0, 0, 255)
                elif event.key == pygame.K_4: #смена цвета на желтый
                    color = (255, 255, 0)
                elif event.key == pygame.K_5: #смена цвета на белый
                    color = (255, 255, 255)

            if event.type == pygame.MOUSEBUTTONDOWN: #обработка нажатия кнопки мыши
                if mode == "erase": #если режим стирания то рисуем черный круг
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)
                else:
                    start = event.pos #сохраняем начальную точку рисования
            if event.type == pygame.MOUSEBUTTONUP and start: #обработка отпускания кнопки мыши
                end = event.pos #сохраняем конечную точку рисования
                x1, y1 = start #разбираем начальную точку на координаты
                x2, y2 = end #разбираем конечную точку на координаты
                w, h = abs(x1 - x2), abs(y1 - y2) #вычисляет размер фигуры (ширину и высоту) между точкой, где мышь была нажата, и где её отпустили.
                rect = pygame.Rect(min(x1, x2), min(y1, y2), w, h) #создаем прямоугольник для рисования фигуры
                if mode == "rect": #если режим рисования прямоугольников
                    pygame.draw.rect(screen, color, rect) #рисуем прямоугольник
                elif mode == "circle": #если режим рисования кругов
                    center = rect.center #находим центр прямоугольника
                    r = int(((w)**2 + (h)**2)**0.5 / 2) #вычисляем радиус круга
                    pygame.draw.circle(screen, color, center, r) #рисуем круг
                start = None #сбрасываем начальную точку
            if event.type == pygame.MOUSEMOTION and mode == "erase": #код внутри выполнится только когда мышь двигается и активен режим ластика
                pygame.draw.circle(screen, (0, 0, 0), event.pos, 20) #рисуем черный круг будто стирая

        pygame.display.flip() #обновляем экран --- Без этого строка, нарисованные изменения, не покажутся.
        clock.tick(60) #масимум 60 кадров в секунду
main() #запуск главной функции, без этого программа не запустится
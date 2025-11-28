import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    mode = None
    color = (255, 255, 255)
    start = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = "rect"
                elif event.key == pygame.K_c:
                    mode = "circle"
                elif event.key == pygame.K_e:
                    mode = "erase"
                elif event.key == pygame.K_1:
                    color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)
                elif event.key == pygame.K_4:
                    color = (255, 255, 0)
                elif event.key == pygame.K_5:
                    color = (255, 255, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == "erase":
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)
                else:
                    start = event.pos
            if event.type == pygame.MOUSEBUTTONUP and start:
                end = event.pos
                x1, y1 = start
                x2, y2 = end
                w, h = abs(x1 - x2), abs(y1 - y2)
                rect = pygame.Rect(min(x1, x2), min(y1, y2), w, h)
                if mode == "rect":
                    pygame.draw.rect(screen, color, rect)
                elif mode == "circle":
                    center = rect.center
                    r = int(((w)**2 + (h)**2)**0.5 / 2)
                    pygame.draw.circle(screen, color, center, r)
                start = None
            if event.type == pygame.MOUSEMOTION and mode == "erase":
                pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)

        pygame.display.flip()
        clock.tick(60)
main()
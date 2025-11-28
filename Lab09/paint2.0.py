import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint upd")
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
                elif event.key == pygame.K_s:            
                    mode = "square"
                elif event.key == pygame.K_y:            
                    mode = "right_triangle"
                elif event.key == pygame.K_t:            
                    mode = "triangle"
                elif event.key == pygame.K_h:            
                    mode = "rhombus"
                elif event.key == pygame.K_b:            
                    mode = "brush"
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
                    r = int((w*w + h*h)**0.5 / 2)
                    pygame.draw.circle(screen, color, center, r)

                elif mode == "square":       
                    side = min(w, h)
                    sq = pygame.Rect(min(x1, x2), min(y1, y2), side, side)
                    pygame.draw.rect(screen, color, sq)

                elif mode == "right_triangle":  
                    pygame.draw.polygon(screen, color, [
                        (x1, y1), (x1, y2), (x2, y2)
                    ])

                elif mode == "triangle":     
                    mid = ((x1 + x2)//2, y1)
                    pygame.draw.polygon(screen, color, [
                        mid, (x1, y2), (x2, y2)
                    ])

                elif mode == "rhombus":     
                    pygame.draw.polygon(screen, color, [
                        ((x1+x2)//2, y1),
                        (x2, (y1+y2)//2),
                        ((x1+x2)//2, y2),
                        (x1, (y1+y2)//2)
                    ])

                start = None

            if event.type == pygame.MOUSEMOTION and mode == "erase":
                pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)

            if event.type == pygame.MOUSEMOTION and mode == "brush":  
                pygame.draw.circle(screen, color, event.pos, 6)

        pygame.display.flip()
        clock.tick(60)

main()

#########
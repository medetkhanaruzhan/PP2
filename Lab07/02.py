import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

tracks = [
    {
        "path": "musics/Kendrick Lamar - Count Me Out.mp3",
        "cover": "photos/N95.png",
        "name": "Kendrick Lamar - Count Me Out"
    },
    {
        "path": "musics/Kendrick Lamar - Euphoria.mp3",
        "cover": "photos/euphoria.png",
        "name": "Kendrick Lamar - Euphoria"
    },
    {
        "path": "musics/Kendrick Lamar - N95.mp3",
        "cover": "photos/N95.png",
        "name": "Kendrick Lamar - N95"
    },
    {
        "path": "musics/Melanie Martinez - Pacify Her.mp3",
        "cover": "photos/pacifyher.png",
        "name": "Melanie Martinez - Pacify Her"
    },
    {
        "path": "musics/Melanie Martinez - Play Date.mp3",
        "cover": "photos/pacifyher.png",
        "name": "Melanie Martinez - Play Date"
    },
    {
        "path": "musics/Монеточка - Каждый Раз.mp3",
        "cover": "photos/monetochka.jpeg",
        "name": "Монеточка - Каждый Раз"
    }
]

current_track = 0
is_playing = False


font = pygame.font.SysFont("Arial", 32, bold=True)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def load_track(index):
    pygame.mixer.music.load(tracks[index]["path"])
    img = pygame.image.load(tracks[index]["cover"])
    img = pygame.transform.smoothscale(img, (400, 400))
    return img

cover = load_track(current_track)

running = True
while running:
    screen.fill(WHITE)

    screen.blit(cover, (200, 80))
    title = font.render(tracks[current_track]["name"], True, BLACK)
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 500))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_playing = not is_playing
                if is_playing:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.stop()

            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(tracks)
                cover = load_track(current_track)
                pygame.mixer.music.play()
                is_playing = True

            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(tracks)
                cover = load_track(current_track)
                pygame.mixer.music.play()
                is_playing = True

    clock.tick(30)

pygame.quit()
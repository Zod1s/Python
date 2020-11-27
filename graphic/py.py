import GraphicEngineV1 as graphic
import numpy as np
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 800, 800

done = False

center = np.array((WIDTH / 2, HEIGHT / 2, 0.0))

sun = graphic.Sphere(center, center, 2, WHITE, 100, 0, BLACK, 20)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
graphic.screen = screen
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(BLACK)

    graphic.draw_solid(sun, "x,y,z")

    pygame.display.flip()

    clock.tick(100)

pygame.quit()
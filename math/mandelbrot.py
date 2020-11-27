import pygame
import cmath
import math
import pygame.surfarray as surfarray

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def f(c):
    z = 0
    n = 0
    for _ in range(MAX_ATTEMPTS):
        if abs(z) < 2:
            z = z * z + c
        else:
            n = _
            break
    return n

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
EXA_WHITE = 0xFFFFFF
EXA_BLACK = 0x000000
MAX_ATTEMPTS = 100

width = 800
height = 600
size = (width, height)

center = width // 2 + 1j * (height // 2)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
surface = surfarray.array2d(screen)

for a, row in enumerate(surface):
    for b, item in enumerate(row):
        attempts = f(a + b * 1j)
        if attempts > MAX_ATTEMPTS // 2:
            surface[a][b] = EXA_BLACK
        else:
            surface[a][b] = EXA_WHITE

pygame.surfarray.blit_array(screen, surface)
pygame.display.flip()

done = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

pygame.quit()
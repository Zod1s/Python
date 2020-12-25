import heapsort as hps
import pygame
from numpy import around
from random import randrange

pygame.init()

def map_value(x, in_min, in_max, out_min, out_max):
    return int(around((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min))

def heapsort(a):
    hps.buildheap(a)
    n = len(a)
    for i in range(n-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        hps.heapify(a, i, 0)

    return a

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

N = 400
MIN = 1
MAX = 100
width = 800
height = 600

data = [randrange(MIN, MAX) for _ in range(N)]
sor = data.copy()
size = (width, height)
screen = pygame.display.set_mode(size)
done = to_sort = to_heapify = False

w = int(around(width / N))

clock = pygame.time.Clock()

n = N

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_h:
                to_heapify = True
            elif event.key == pygame.K_s:
                to_sort = True
            elif event.key == pygame.K_r:
                sor = data.copy()
                n = N

    screen.fill(BLACK)

    for i in range(len(sor)):
        h = map_value(sor[i], MIN, MAX, 0, height)
        pointlist = [[i * w, height], [i * w + w - 1, height], [i * w + w - 1, height - h], [i * w, height - h]]
        color = GREEN if not i and to_sort else RED
        pygame.draw.polygon(screen, color, pointlist, 1)

    if to_heapify:
        hps.buildheap(sor)
        to_heapify = False

    if to_sort:
        if n > 0:
            n -= 1
            sor[0], sor[n] = sor[n], sor[0]
            hps.heapify(sor, n, 0)
        else:
            to_sort = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
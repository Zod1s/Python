import pygame
import pygame.gfxdraw
from numpy import pi, cos, sin

pygame.init()

BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
BALL       = (191, 191, 191)
BACKGROUND = (127, 127, 127)

i = 0
width = 800
height = 800
frameRate = 100
n = frameRate / 5
damping = 1

mass = 200
length = 400
radius = int(mass / 5)
g = 9.81

pendulum_origin = (width / 2, 0)
size = (width, height)

ang_0 = pi/4
angle = ang_0
vel = 0
acc = 0
max_angle = 0
min_angle = 0

done = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_r:
                angle = ang_0
                vel = 0
                acc = 0

    mass_x = int(length*sin(angle) + pendulum_origin[0])
    mass_y = int(length*cos(angle) + pendulum_origin[1])

    screen.fill(BACKGROUND)

    pygame.draw.line(screen, BLACK, pendulum_origin, (mass_x, mass_y), 2)
    pygame.gfxdraw.filled_circle(screen, mass_x, mass_y, radius, BALL)
    pygame.gfxdraw.aacircle(screen, mass_x, mass_y, radius, BALL)

    pygame.display.flip()

    acc = -(g/length)*sin(angle) / n 
    vel += acc
    angle += vel
    angle *= damping

    clock.tick(frameRate)

pygame.quit()
import pygame
import pygame.gfxdraw
import pygame.surfarray as surfarray
from numpy import pi, cos, sin
from numpy import zeros as array
from numpy import longdouble as long

pygame.init()

BLACK = (0, 0, 0)
EXA_BLACK = 0x000000
WHITE = (255, 255, 255)
EXA_WHITE = 0xFFFFFF
BALL = (191, 191, 191)
BACKGROUND = (127, 127, 127)
EXA_BACKGROUND = 0x7F7F7F

i = 0
width, height = 850, 850
frameRate = 100
n = frameRate / 25
offset = 50
damping = 0.9995

mass_1 = 100
mass_2 = 100
length_1 = 200
length_2 = 200
radius_1 = int(mass_1 / 5)
radius_2 = int(mass_2 / 5)
g = 2

angle_1 = array(1, dtype=long)
angle_2 = array(1, dtype=long)
vel_1 = array(1, dtype=long)
vel_2 = array(1, dtype=long)
acc_1 = array(1, dtype=long)
acc_2 = array(1, dtype=long)

angle_1[0] = pi / 2
angle_2[0] = pi / 2

pendulum1_origin = (width / 2, offset)

size = (width, height)

done = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
surface = surfarray.array2d(screen)

for i in range(width):
    for j in range(height):
        surface[i][j] = EXA_BACKGROUND

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    pendulum2_origin = (width /
                        2 +
                        length_1 *
                        sin(angle_1[0]),
                        offset + length_1 * cos(angle_1[0]))

    mass1_x = int(length_1 * sin(angle_1[0]) + pendulum1_origin[0])
    mass1_y = int(length_1 * cos(angle_1[0]) + pendulum1_origin[1])
    mass1_coordinates = (mass1_x, mass1_y)

    mass2_x = int(length_2 * sin(angle_2[0]) + pendulum2_origin[0])
    mass2_y = int(length_2 * cos(angle_2[0]) + pendulum2_origin[1])
    mass2_coordinates = (mass2_x, mass2_y)
    if 0 <= mass2_x < width and 0 <= mass2_y < height:
        surface[mass2_x][mass2_y] = EXA_BLACK

    screen.fill(WHITE)

    pygame.surfarray.blit_array(screen, surface)
    pygame.draw.line(screen, BLACK, pendulum1_origin, mass1_coordinates, 2)
    pygame.draw.line(screen, BLACK, pendulum2_origin, mass2_coordinates, 2)
    pygame.gfxdraw.filled_circle(screen, mass1_x, mass1_y, radius_1, BALL)
    pygame.gfxdraw.filled_circle(screen, mass2_x, mass2_y, radius_2, BALL)
    pygame.gfxdraw.aacircle(screen, mass1_x, mass1_y, radius_1, BALL)
    pygame.gfxdraw.aacircle(screen, mass2_x, mass2_y, radius_2, BALL)
    pygame.display.flip()

    acc_1[0] = ((-g * (2 * mass_1 + mass_2) * sin(angle_1[0]) -
                 mass_2 * g * sin(angle_1[0] - 2 * angle_2[0]) -
                 2 * sin(angle_1[0] - angle_2[0]) * mass_2 *
                 ((vel_2[0]**2) * length_2 + (vel_1[0]**2) * length_1 * cos(angle_1[0] - angle_2[0]))) /
                (length_1 * (2 * mass_1 + mass_2 - mass_2 * cos(2 * angle_1[0] - 2 * angle_2[0])))) / n

    acc_2[0] = (2 * sin(angle_1[0] - angle_2[0]) * (vel_1[0]**2 * length_1 * (mass_1 + mass_2) +
                                                    g * (mass_1 + mass_2) * cos(angle_1[0]) +
                                                    vel_2**2 * length_2 * mass_2 * cos(angle_1[0] - angle_2[0])) /
                (length_2 * (2 * mass_1 + mass_2 - mass_2 * cos(2 * (angle_1[0] - angle_2[0]))))) / n

    vel_1[0] += acc_1[0]
    vel_2[0] += acc_2[0]

    angle_1[0] = (angle_1[0] + vel_1[0]) * damping
    angle_2[0] = (angle_2[0] + vel_2[0]) * damping

    clock.tick(frameRate)

pygame.quit()

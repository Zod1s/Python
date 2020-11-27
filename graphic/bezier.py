import pygame
import pygame.gfxdraw

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
size = (600, 600)

done = False

radius = 10

ctrl_points = []
res = 10000

def fact(x):
    if x >= 0 and type(x) == int:
        result = 1
        for i in range(x):
            result *= (i + 1)
        return result
    else:
        raise Exception("In order for the factorial function to work, x must be a positive integer")

def binomial(n, k):
    num = fact(n)
    den = fact(k) * fact(n - k)
    return int(num / den)

def bernstein(n, i, u):
    return binomial(n, i) * u**i * (1 - u)**(n - i)

def beizer_curve(control_points, res):
    num = len(control_points)
    points = []

    for j in range(res + 1):
        x = 0
        y = 0
        t = j / res
        for i in range(num):
            x += bernstein(num - 1, i, t) * control_points[i][0]
            y += bernstein(num - 1, i, t) * control_points[i][1]

        points.append((int(x), int(y)))

    return points

def get_points(num, screen):
    global done
    finish = False

    while not finish:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ctrl_points.append(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    finish = True
        for point in ctrl_points:
            pygame.draw.circle(screen, WHITE, point, radius)

        pygame.display.flip()
        if len(ctrl_points) == num:
            finish = True

def create_curve(screen):
    num_points = int(input("quanti punti di controllo?: "))
    res = int(input("qual e' la risoluzione?: "))

    ctrl_points.clear()
    get_points(num_points, screen)
    return beizer_curve(ctrl_points, res)

pygame.init()

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

points = create_curve(screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_r:
                points = create_curve(screen)

    screen.fill(BLACK)

    for point in ctrl_points:
        pygame.draw.circle(screen, WHITE, point, radius)

    for point in points:
        pygame.gfxdraw.pixel(screen, point[0], point[1], WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
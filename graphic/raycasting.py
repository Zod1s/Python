from math import cos, degrees, hypot, inf, pi, sin, sqrt, tan
from random import randrange

import pygame
from numpy import around, inf, linspace

pygame.init()

BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)

WIDTH, HEIGHT = 800, 600

class Ray:
    def __init__(self, pos, angle, screen):
        self.pos = pygame.math.Vector2(pos)
        self.angle = angle
        self.screen = screen

    def cast(self, wall):
        (x1, y1) = wall.start
        (x2, y2) = wall.end

        (x3, y3) = self.pos
        x4 = self.pos.x + cos(self.angle)
        y4 = self.pos.y + sin(self.angle)

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return None
        else:
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = - ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

            if u > 0.0 and t > 0.0 and t < 1.0:
                x, y = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
                return pygame.math.Vector2((x, y))
            else:
                return None

    # def show(self):
    #     direction = pygame.math.Vector2((cos(self.angle), sin(self.angle)))
    #     pygame.draw.line(self.screen, WHITE, self.pos, (self.pos + direction * 10))


class Source:
    def __init__(self, pos, angle, fov, resolution, screen):
        self.pos = pygame.math.Vector2(pos)
        self.angle = angle
        self.fov = fov
        self.screen = screen
        self.radius = 4
        res = resolution if resolution % 2 != 0 else resolution + 1
        self.rays = [Ray(self.pos, self.angle + angle, self.screen)
                     for angle in linspace(-self.fov / 2, self.fov / 2, res)]

    def rotate(self, angle):
        self.angle += angle
        for ray in self.rays:
            ray.angle += angle

    def move(self, amt):
        direction = pygame.math.Vector2((cos(self.angle), sin(self.angle)))
        self.pos += direction * amt

        self.pos.x = self.radius if self.pos.x < self.radius else WIDTH - \
            self.radius if self.pos.x > WIDTH - self.radius else self.pos.x
        self.pos.y = self.radius if self.pos.y < self.radius else HEIGHT - \
            self.radius if self.pos.y > HEIGHT - self.radius else self.pos.y

        for ray in self.rays:
            ray.pos = self.pos

    def raycast(self, walls):
        distances = []
        colours = []

        for ray in self.rays:
            record_dist = hypot(WIDTH, HEIGHT)
            record_point = None
            record_colour = BLACK

            for wall in walls:
                point = ray.cast(wall)

                if point is not None:
                    a = ray.angle - self.angle
                    dist = self.pos.distance_to(point) * cos(a) # the cosine corrects the fisheye effect

                    if dist < record_dist:
                        record_dist = dist
                        record_point = point
                        record_colour = wall.colour

            distances.append(record_dist)
            colours.append(record_colour)

        return distances, colours

    # def show(self):
    #     pygame.draw.circle(self.screen, WHITE, (int(around(self.pos.x)), int(around(self.pos.y))), self.radius)
    #     for ray in self.rays:
    #         ray.show()


class Wall:
    def __init__(self, startpos, endpos, colour, screen):
        self.start = pygame.math.Vector2(startpos)
        self.end = pygame.math.Vector2(endpos)
        self.colour = colour
        self.screen = screen

    # def show(self):
    #     pygame.draw.line(self.screen, self.colour, self.start, self.end)


def map_value(x, in_min, in_max, out_min, out_max):
    return int(around((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min))


def constrain(x, min, max):
    return min if x <= min else max if x >= max else x


light_dir = 0
fov = pi / 3
res = 61

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

center = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
origin = pygame.math.Vector2(0, 0)

done = False

clock = pygame.time.Clock()

light = Source(center, light_dir, fov, res, screen)
walls = [Wall([0, 0], [WIDTH - 1, 0], WHITE, screen), Wall([WIDTH - 1, 0], [WIDTH - 1, HEIGHT - 1], WHITE, screen),
         Wall([WIDTH - 1, HEIGHT - 1], [0, HEIGHT - 1], WHITE, screen), Wall([0, HEIGHT - 1], [0, 0], WHITE, screen)]

walls.append(Wall([50, 50], [250, 50], RED, screen))
walls.append(Wall([250, 50], [250, 250], BLUE, screen))
walls.append(Wall([250, 250], [50, 250], RED, screen))
walls.append(Wall([50, 250], [50, 50], BLUE, screen))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        light.move(1)
    if pressed[pygame.K_s]:
        light.move(-1)
    if pressed[pygame.K_a]:
        light.rotate(-pi / 128)
    if pressed[pygame.K_d]:
        light.rotate(pi / 128)

    screen.fill(BLACK)

    # light.show()

    # for wall in walls:
    #     wall.show()

    scene, colours = light.raycast(walls)

    w = int(around(WIDTH / len(scene), 0))

    for i, dist in enumerate(scene):

        color = [0, 0, 0]

        W = hypot(WIDTH, HEIGHT)

        b = map_value(dist**2, 0, W**2, 255, 0) # cambia i massimi e minimi a seconda del massimo dell'array
        h = constrain(HEIGHT * degrees(fov) / dist, 0, HEIGHT) # usa map cambiando i massimi e minimi a seconda del massimo dell'array

        if colours[i] == BLACK:
            color = BLACK
        else:
            color[0] = b if colours[i][0] == 255 else 0
            color[1] = b if colours[i][1] == 255 else 0
            color[2] = b if colours[i][2] == 255 else 0

        pointlist = [pygame.math.Vector2([i * w, int(around(HEIGHT / 2 - h / 2, 0))]) + origin, pygame.math.Vector2([i * w + w, int(around(HEIGHT / 2 - h / 2, 0))]) + origin,
                     pygame.math.Vector2([i * w + w, int(around(HEIGHT / 2 + h / 2, 0))]) + origin, pygame.math.Vector2([i * w, int(around(HEIGHT / 2 + h / 2, 0))]) + origin]
        pygame.draw.polygon(screen, color, pointlist)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

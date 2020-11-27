#--This program shows a rotating orthogonal 2D projection of a cube--#

import pygame
import pygame.gfxdraw
import numpy as np

#-----------------------point classes-------------------------#

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.point = np.array([x, y, z], dtype=np.float64)

    def rotationX(self, angle, center):
        matrix = np.array(     #rotation around X axis
            [
                [1.0,           0.0,            0.0],
                [0.0, np.cos(angle), -np.sin(angle)],
                [0.0, np.sin(angle),  np.cos(angle)]
            ]
        )
        new_point = np.sum([np.dot(matrix, (np.subtract(self.point, center))), center], axis=0)
        return Point3D(new_point[0], new_point[1], new_point[2])

    def rotationY(self, angle, center):
        matrix = np.array(     #rotation around Y axis
            [
                [np.cos(angle),  0.0,  np.sin(angle)],
                [          0.0,  1.0,            0.0],
                [-np.sin(angle), 0.0,  np.cos(angle)]
            ]
        )
        new_point = np.sum([np.dot(matrix, (np.subtract(self.point, center))), center], axis=0)
        return Point3D(new_point[0], new_point[1], new_point[2])

    def rotationZ(self, angle, center):
        matrix = np.array(     #rotation around Z axis 
            [   
                [np.cos(angle), -np.sin(angle),  0.0],
                [np.sin(angle),  np.cos(angle),  0.0],
                [          0.0,            0.0,  1.0]
            ]
        )
        new_point = np.sum([np.dot(matrix, (np.subtract(self.point, center))), center], axis=0)
        return Point3D(new_point[0], new_point[1], new_point[2])

    def project(self):
        points = np.dot(projection_matrix, self.point)
        return Point2D(points[0], points[1])  

class Point2D:  #for the 2D representation of the points
    def __init__(self, x=0, y=0):
        self.point = np.array([x,y], dtype=np.float64)

#-----------------------drawing functions---------------------#

def draw_point(surface, center, radius, colour):
    pygame.gfxdraw.filled_circle(surface, center[0], center[1], radius, colour)

def connect(surface, a, b, colour):
    pygame.gfxdraw.line(surface, a[0], a[1], b[0], b[1], colour)

#--------------------------matrices---------------------------#

identity_matrix = np.array( #it's the 3x3 identity matrix
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]
)

projection_matrix = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]
)

#-------------------costants and variables--------------------#

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH  = 800
HEIGHT = 800
WIDTH_FLOAT  = float(WIDTH)
HEIGHT_FLOAT = float(HEIGHT)

radius = 5
angle = 0.0

done = False

#----------------------declaring points-----------------------#

points = []

points.append(Point3D(WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2-100.0, 100.0))
points.append(Point3D(WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2-100.0, 100.0))
points.append(Point3D(WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2+100.0, 100.0))
points.append(Point3D(WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2+100.0, 100.0))
points.append(Point3D(WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2-100.0,-100.0))
points.append(Point3D(WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2-100.0,-100.0))
points.append(Point3D(WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2+100.0,-100.0))
points.append(Point3D(WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2+100.0,-100.0))

center = np.array((WIDTH_FLOAT / 2, HEIGHT_FLOAT / 2, 0.0))

projected_points = [[0,0]]*len(points)

#--------------------initialising pygame----------------------#

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for i in range(len(points)):
        rotatedX   = points[i].rotationX(angle, center)
        rotatedXY  = rotatedX.rotationY(angle, center)
        rotatedXYZ = rotatedXY.rotationZ(angle, center)
        
        projected = rotatedXYZ.project()

        x_point = int(projected.point[0])
        y_point = int(projected.point[1])
        projected_points[i] = (x_point, y_point)

        draw_point(surface=screen, center=(x_point, y_point), radius=radius, colour=WHITE)
    
    for i in range(4):
        connect(screen,     projected_points[i],     projected_points[((i+1)%4)], colour=WHITE)
        connect(screen, projected_points[(i+4)], projected_points[(((i+1)%4)+4)], colour=WHITE)
        connect(screen,     projected_points[i],         projected_points[(i+4)], colour=WHITE) 

    pygame.display.flip()

    angle += 0.01
    clock.tick(100)

pygame.quit()
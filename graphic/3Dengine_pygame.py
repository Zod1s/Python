#---This program shows a rotating 2D projection in perspective of a cube--#

import pygame
import pygame.gfxdraw
import numpy as np

#-----------------------point classes-------------------------#

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.point = np.array([x, y, z], dtype=np.float64)

    def rotationX(self, angle):
        matrix = np.array(     #rotation around X axis
            [
                [1.0,           0.0,            0.0],
                [0.0, np.cos(angle), -np.sin(angle)],
                [0.0, np.sin(angle),  np.cos(angle)]
            ]
        )
        new_point = np.dot(matrix, self.point)
        return Point3D(new_point[0], new_point[1], new_point[2])

    def rotationY(self, angle):
        matrix = np.array(     #rotation around Y axis
            [
                [np.cos(angle),  0.0,  np.sin(angle)],
                [          0.0,  1.0,            0.0],
                [-np.sin(angle), 0.0,  np.cos(angle)]
            ]
        )
        new_point = np.dot(matrix, self.point)
        return Point3D(new_point[0], new_point[1], new_point[2])

    def rotationZ(self, angle):
        matrix = np.array(     #rotation around Z axis 
            [   
                [np.cos(angle), -np.sin(angle),  0.0],
                [np.sin(angle),  np.cos(angle),  0.0],
                [          0.0,            0.0,  1.0]
            ]
        )
        new_point = np.dot(matrix, self.point)
        return Point3D(new_point[0], new_point[1], new_point[2])
    
    def project(self, fov, distance, center):

        if (self.point[2] >= distance):
            projection_matrix = np.array(
                [
                    [1.0,  0.0, 0.0],
                    [0.0, -1.0, 0.0]
                ]
            )
            new_point = np.dot(projection_matrix, self.point)
            new_point = np.sum([new_point, center], axis=0)
            is_seen = 0

        else:
            factor = fov / (distance - self.point[2])
            projection_matrix = np.array(
                [
                    [factor,  0.0, 0.0],
                    [0.0, -factor, 0.0]
                ]
            )
            new_point = np.dot(projection_matrix, self.point)
            new_point = np.sum([new_point, center], axis=0)
            is_seen = 1

        return Point2D(new_point[0], new_point[1], is_seen)

class Point2D:  #for the 2D representation of the points
    def __init__(self, x=0, y=0, show=1):
        self.point = np.array([x,y,show], dtype=np.float64)

#-----------------------drawing functions---------------------#

def draw_point(surface, center, radius, colour):
    pygame.gfxdraw.filled_circle(surface, center[0], center[1], radius, colour)

def connect(surface, a, b, colour):
    if a[2] == 1 and b[2] == 1:
        pygame.draw.aaline(surface, colour, (a[0], a[1]), (b[0], b[1]))

#--------------------------matrices---------------------------#

identity_matrix = np.array( #it's the 3x3 identity matrix
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]
)

#-------------------costants and variables--------------------#

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
width  = 1000
height = 1000
width_float  = float(width)
height_float = float(height)

radius = 5
angle = 0
fov = 90.0
distance = 230.0

done = False

#----------------------declaring points-----------------------#

points = []

points.append(Point3D(-100, -100,  100))
points.append(Point3D( 100, -100,  100))
points.append(Point3D( 100,  100,  100))
points.append(Point3D(-100,  100,  100))
points.append(Point3D(-100, -100, -100))
points.append(Point3D( 100, -100, -100))
points.append(Point3D( 100,  100, -100))
points.append(Point3D(-100,  100, -100))

center = np.array((width_float / 2, height_float / 2))

projected_points = [[0,0]]*len(points)

#--------------------initialising pygame----------------------#

pygame.init()

size = (width, height)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for i in range(len(points)):
        rotatedX   = points[i].rotationX(angle)
        rotatedXY  = rotatedX.rotationY(angle)
        rotatedXYZ = rotatedXY.rotationZ(angle)
        
        projected = rotatedXYZ.project(fov, distance, center)

        x_point = int(projected.point[0])
        y_point = int(projected.point[1])
        shown = int(projected.point[2])
        projected_points[i] = (x_point, y_point, shown)

        if(shown == 1):   
            draw_point(surface=screen, center=(x_point, y_point), radius=radius, colour=WHITE)
    
    for i in range(4):
        connect(screen,     projected_points[i],     projected_points[((i+1)%4)], colour=WHITE)
        connect(screen, projected_points[(i+4)], projected_points[(((i+1)%4)+4)], colour=WHITE)
        connect(screen,     projected_points[i],         projected_points[(i+4)], colour=WHITE) 

    pygame.display.flip()

    angle += 0.01
    clock.tick(75)

pygame.quit()
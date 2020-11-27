#--Graphic library for 3D orthogonal representation of objects--#

import pygame
import pygame.gfxdraw
from numpy import pi, cos, sin, array, dot, float16, int
from sys import exit
from random import randint, randrange, seed

#--------------------------- matrices --------------------------#

def matrixX(angle): # for rotation around X axis
    return [[ 1.0,        0.0,         0.0],
            [ 0.0, cos(angle), -sin(angle)],
            [ 0.0, sin(angle),  cos(angle)]]

def matrixY(angle): # for rotation around Y axis
    return [[ cos(angle), 0.0, sin(angle)],
            [        0.0, 1.0,        0.0],
            [-sin(angle), 0.0, cos(angle)]]

def matrixZ(angle): # for rotation around Z axis
    return [[cos(angle), -sin(angle), 0.0],
            [sin(angle),  cos(angle), 0.0],
            [       0.0,         0.0, 1.0]]

#--------------------------global vars--------------------------#

X = 0
Y = 1
Z = 2

screen = 0 # it has to be defined in the program passing the screen object created in it
G = 6.67*10**(-4)

#-----------------------drawing classes-------------------------#

class Point3D:
    def __init__(self, x, y, z):
        self.coordinates = array([x, y, z], dtype=float16)
        self.projected = array([0, 0], dtype=int)

    def rotationX(self, rot_center, angle):
        # X' = AX - AB + B
        self.coordinates = dot(matrixX(angle), self.coordinates) - dot(matrixX(angle), rot_center) + rot_center

    def rotationY(self, rot_center, angle):
        self.coordinates = dot(matrixY(angle), self.coordinates) - dot(matrixY(angle), rot_center) + rot_center

    def rotationZ(self, rot_center, angle):
        self.coordinates = dot(matrixZ(angle), self.coordinates) - dot(matrixZ(angle), rot_center) + rot_center

    def ortho_project(self):
        point = dot(ortho_projection_matrix, self.coordinates)
        self.projected[X] = int(point[X])
        self.projected[Y] = int(point[Y])

class Point2D: # for the 2D representation of the points
    def __init__(self, x, y):
        self.coordinates = array([x,y], dtype=int)

class Shape: # class for initialising all the variable of a shape class
    def __init__(self, center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour): 
        self.center = center
        self.point_radius = point_radius
        self.width = line_width
        self.length = side_length
        self.side_colour = side_colour
        self.point_colour = point_colour
        self.rot_center = rotation_center
        self.index = 0

    def randcolour(self):
        self.point_colour[self.index] = (self.point_colour[self.index] + 1) %255
        times = randint(0, 10)
        for _ in range(times):
            self.index = randint(0, 2)
        self.index = self.index % 3

#-------------------------shape classes-------------------------#

class Cube(Shape):
    def __init__(self, center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour):
        super().__init__(center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour)

        self.points = [
            Point3D(center[X]-self.length, center[Y]-self.length, center[Z]+self.length),
            Point3D(center[X]+self.length, center[Y]-self.length, center[Z]+self.length),
            Point3D(center[X]+self.length, center[Y]+self.length, center[Z]+self.length),
            Point3D(center[X]-self.length, center[Y]+self.length, center[Z]+self.length),
            Point3D(center[X]-self.length, center[Y]-self.length, center[Z]-self.length),
            Point3D(center[X]+self.length, center[Y]-self.length, center[Z]-self.length),
            Point3D(center[X]+self.length, center[Y]+self.length, center[Z]-self.length),
            Point3D(center[X]-self.length, center[Y]+self.length, center[Z]-self.length)
        ]

        self.sides = [
            [0, 1],[1, 2],[2, 3],[3, 0],
            [4, 5],[5, 6],[6, 7],[7, 4],
            [0, 4],[1, 5],[2, 6],[3, 7]
        ]

class Sphere(Shape):
    def __init__(self, center, rotation_center, point_radius, point_colour, radius, line_width, side_colour, resolution):
        super().__init__(center, rotation_center, point_radius, point_colour, radius, line_width, side_colour)

        self.resolution = resolution 

        self.points = []
        self.sides = []

        for i in range(self.resolution):
            # -PI <= phi <= PI
            phi = map_value(i, 0, self.resolution - 1, -pi, pi)
            for j in range(self.resolution):
                # -PI/2 <= theta <= PI/2
                theta = map_value(j, 0,self.resolution - 1, 0, pi)
                x = self.length * sin(theta) * cos(phi) + center[X]
                y = self.length * sin(theta) * sin(phi) + center[Y]
                z = self.length * cos(theta) + center[Z]
                self.points.append(Point3D(x, y, z))

#------------------------drawing functions----------------------#

def draw_solid(solid, rotation="no_rot", colour_mode="normal", angle=0.01):
    rotate_solid(solid, rotation=rotation, angle=angle)
    for point in solid.points:
        point.ortho_project()

    for side in solid.sides:
        connect(screen, solid.points[side[0]].projected, solid.points[side[1]].projected, colour=solid.side_colour, width=solid.width)

    for point in solid.points:
        draw(point=point, surface=screen, radius=solid.point_radius, colour=solid.point_colour)
        if colour_mode == "casual":
            if randint(0, 100)%2 == 0:
                solid.randcolour()

def rotate_solid(solid, rotation="", angle=0.01, rot_center=None):
    if rot_center == None:
        rot_center = solid.rot_center

    if rotation != "no_rot":
        type_rot = rotation.lower().split(",")
        for rot in type_rot:
            if rot.strip() == "x":
                for point in solid.points:
                    point.rotationX(rot_center, angle)
            elif rot.strip() == "y":
                for point in solid.points:
                    point.rotationY(rot_center, angle)
            elif rot.strip() == "z":
                for point in solid.points:
                    point.rotationZ(rot_center, angle)
            else:
                exit('rotation not valid')

def draw(point, surface, radius, colour):
    pygame.gfxdraw.filled_circle(surface, point.projected[X], point.projected[Y], radius, colour)

def connect(surface, a, b, colour, width=1):
    pygame.draw.line(surface, colour, a, b, width)

#---------------------------matrices----------------------------#

ortho_projection_matrix = array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]
)

#---------------------------functions---------------------------#

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
#--Graphic library for 3D orthogonal representation of objects--#

import pyglet
from numpy import pi, cos, sin, array, subtract, sum, dot, float16, int
from sys import exit
from utilities import mapvalue
from random import randint, randrange, seed

#--------------------------global vars--------------------------#

X = 0
Y = 1
Z = 2

#----------------------lambdas for matrices---------------------#

matrixX = lambda angle : [[       1.0,         0.0,        0.0], [        0.0, cos(angle), -sin(angle)], [        0.0, sin(angle), cos(angle)]]
matrixY = lambda angle : [[cos(angle),         0.0, sin(angle)], [        0.0,        1.0,         0.0], [-sin(angle),        0.0, cos(angle)]]
matrixZ = lambda angle : [[cos(angle), -sin(angle),        0.0], [ sin(angle), cos(angle),         0.0], [        0.0,        0.0,        1.0]]

#-----------------------drawing classes-------------------------#

class Point3D:
    def __init__(self, x, y, z):
        self.coordinates = array([x, y, z], dtype=float16)
        self.projected = array([0, 0], dtype=int)

    def rotationX(self, center, angle):
        self.coordinates = sum((dot(matrixX(angle), subtract(self.coordinates, center)), center), axis=0)

    def rotationY(self, center, angle):
        self.coordinates = sum((dot(matrixY(angle), subtract(self.coordinates, center)), center), axis=0)

    def rotationZ(self, center, angle):
        self.coordinates = sum((dot(matrixZ(angle), subtract(self.coordinates, center)), center), axis=0)

    def ortho_project(self):
        points = dot(ortho_projection_matrix, self.coordinates)
        self.projected[X] = int(points[X])
        self.projected[Y] = int(points[Y])

    def perspective_project(self, fov):
        pass


class Point2D:  #for the 2D representation of the points
    def __init__(self, x, y):
        self.point = array([x,y], dtype=int)

class Ennio:#class for initialising all the variable of a shape class
    def __init__(self, center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour, angle = 0.01, isinperspective=False, fov=0):#vert_num, 
        
        # if vert_num > 0:
        #     self.vertex_list = pyglet.graphics.vertex_list(vert_num, 'v3f', 'c3B')
        self.center = center
        self.radius = point_radius
        self.width = line_width
        self.length = side_length
        self.side_colour = side_colour
        self.angle = angle
        self.point_colour = point_colour
        self.isinperspective = isinperspective
        self.rot_center = rotation_center
        self.index = 0
        if self.isinperspective:
            self.fov = fov

    def randcolour(self):
        self.point_colour[self.index] = (self.point_colour[self.index] + 1) %255
        times = randint(0, 10)
        for i in range(times):
            self.index = randint(0, 2)
        self.index = self.index % 3

#-------------------------shape classes-------------------------#
class Cube(Ennio):
    def __init__(self, center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour, angle = 0.01, isinperspective=False, fov=0):
        
        super().__init__(center=center, rotation_center=rotation_center, point_radius=point_radius, point_colour=point_colour, side_length=side_length, line_width=line_width, side_colour=side_colour, angle = 0.01, isinperspective=False, fov=0)

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
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 4],
            [0, 4],
            [1, 5],
            [2, 6],
            [3, 7]
        ]

class AX6(Ennio):#class for a octahedron-shaped molecule
    def __init__(self, center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour, angle = 0.01, isinperspective=False, fov=0):
        
        super().__init__(center=center, rotation_center=rotation_center, point_radius=point_radius, point_colour=point_colour, side_length=side_length, line_width=line_width, side_colour=side_colour, angle = 0.01, isinperspective=False, fov=0)

        # self.points = [
        #     Point3D(            self.center[X],             self.center[Y],             self.center[Z]),
        #     Point3D(            self.center[X], self.center[Y]-self.length,             self.center[Z]),
        #     Point3D(            self.center[X], self.center[Y]+self.length,             self.center[Z]),
        #     Point3D(self.center[X]-self.length,             self.center[Y],             self.center[Z]),
        #     Point3D(self.center[X]+self.length,             self.center[Y],             self.center[Z]),
        #     Point3D(            self.center[X],             self.center[Y], self.center[Z]-self.length),
        #     Point3D(            self.center[X],             self.center[Y], self.center[Z]+self.length)
        # ]
        
        self.points = pyglet.graphics.vertex_list(7, 'v3f', 'c3B')

        self.sides = [
            [2, 1],
            [4, 3],
            [6, 5]
        ]

class Sphere(Ennio):
    def __init__(self, center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour, resolution, angle = 0.01, isinperspective=False, fov=0):
        
        super().__init__(center, rotation_center, point_radius, point_colour, side_length, line_width, side_colour, angle = 0.01, isinperspective=False, fov=0)

        self.resolution = resolution 

        self.points = []

        for i in range(self.resolution):
            phi = mapvalue(i, 0, self.resolution, -pi/2, pi/2)
            for j in range(self.resolution):
                theta = mapvalue(j, 0, self.resolution, -pi, pi)
                x = self.length * sin(theta) * cos(phi) + center[X]
                y = self.length * sin(theta) * sin(phi) + center[Y]
                z = self.length * cos(theta) + center[Z]
                self.points.append(Point3D(x, y, z))
                
        self.sides = []

#------------------------drawing functions----------------------#

def draw_solid(solid, rotation="XYZ", colour_mode="normal"):
	batch = pyglet.graphics.Batch()
	
	if not solid.isinperspective:
		projected_points = ortho_rotate_solid(solid, rotations=rotation) 

	for side in solid.sides:
		connect(projected_points[side[X]], projected_points[side[Y]], colour=solid.side_colour, width=solid.width)

	for point in projected_points:
		draw(point=point, radius=solid.radius, colour=solid.point_colour)

	if colour_mode == "casual":
		solid.randcolour()
	else:
		pass
	return batch

def ortho_rotate_solid(solid, rotations=""):
    projected_points = []
    for point in solid.points:
        type_rot = rot_dict.get(rotations.upper())
        if type_rot != "no_rot":
            if type_rot == "rotationX":
                point = point.rotationX(solid.angle, solid.rot_center)
            elif type_rot == "rotationY":
                point = point.rotationY(solid.angle, solid.rot_center)
            elif type_rot == "rotationZ":
                point = point.rotationZ(solid.angle, solid.rot_center)
            elif type_rot == "rotationXY":
                point = point.rotationX(solid.angle, solid.rot_center)
                point = point.rotationY(solid.angle, solid.rot_center)
            elif type_rot == "rotationYX":
                point = point.rotationY(solid.angle, solid.rot_center)
                point = point.rotationX(solid.angle, solid.rot_center)
            elif type_rot == "rotationXZ":
                point = point.rotationX(solid.angle, solid.rot_center)
                point = point.rotationZ(solid.angle, solid.rot_center)
            elif type_rot == "rotationZX":
                point = point.rotationZ(solid.angle, solid.rot_center)
                point = point.rotationX(solid.angle, solid.rot_center)
            elif type_rot == "rotationYZ":
                point = point.rotationY(solid.angle, solid.rot_center)
                point = point.rotationZ(solid.angle, solid.rot_center)
            elif type_rot == "rotationZY":
                point = point.rotationZ(solid.angle, solid.rot_center)
                point = point.rotationY(solid.angle, solid.rot_center)
            elif type_rot == "rotationXYZ":
                point = point.rotationX(solid.angle, solid.rot_center)
                point = point.rotationY(solid.angle, solid.rot_center)
                point = point.rotationZ(solid.angle, solid.rot_center)
            elif type_rot == "rotationXZY":
                point = point.rotationX(solid.angle, solid.rot_center)
                point = point.rotationZ(solid.angle, solid.rot_center)
                point = point.rotationY(solid.angle, solid.rot_center)
            elif type_rot == "rotationYXZ":
                point = point.rotationY(solid.angle, solid.rot_center)
                point = point.rotationX(solid.angle, solid.rot_center)
                point = point.rotationZ(solid.angle, solid.rot_center)
            elif type_rot == "rotationYZX":
                point = point.rotationY(solid.angle, solid.rot_center)
                point = point.rotationZ(solid.angle, solid.rot_center)
                point = point.rotationX(solid.angle, solid.rot_center)
            elif type_rot == "rotationZXY":
                point = point.rotationZ(solid.angle, solid.rot_center)
                point = point.rotationX(solid.angle, solid.rot_center)
                point = point.rotationY(solid.angle, solid.rot_center)
            elif type_rot == "rotationZYX":
                point = point.rotationZ(solid.angle, solid.rot_center)
                point = point.rotationY(solid.angle, solid.rot_center)
                point = point.rotationX(solid.angle, solid.rot_center)
            else:
                exit('rotation not valid')

        projected = point.ortho_project()
        projected_points.append(projected)

    return projected_points

def draw(point, radius, colour):
    return
#     pygame.draw.circle(surface, colour, (point.point[0], point.point[1]), radius)

def connect(a, b, colour, width=1):
    return
#     pygame.draw.line(surface, colour, a.point, b.point, width)

#---------------------------matrices----------------------------#

ortho_projection_matrix = array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]
)

#--------------------------dictionariY--------------------------#

rot_dict = {
    "NO":"no_rot",
    "X":"rotationX",
    "Y":"rotationY",
    "Z":"rotationZ",
    "XY":"rotationXY",
    "YX":"rotationYX",
    "XZ":"rotationXZ",
    "ZX":"rotationZX",
    "YZ":"rotationYZ", 
    "ZY":"rotationZY",
    "XYZ":"rotationXYZ",
    "XZY":"rotationXZY",
    "YXZ":"rotationYXZ",
    "YZX":"rotationYZX",
    "ZXY":"rotationZXY",
    "ZYX":"rotationZYX"
}




'''
!!!!importante!!!!
'''

'''
cose da fare:
-aggiungere altre forme
-aggiungere la prospettiva(più importante)
'''
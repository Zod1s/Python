#- 2nd version of the graphic engine -#

from math import cos, pi, sin
from sys import exit

import numpy as np
import pygame
import pygame.gfxdraw

#- Global -#

screen = None
ux = (1, 0, 0)
uy = (0, 1, 0)
uz = (0, 0, 1)

#- Wireframe -#

class Wireframe:
    def __init__(self, colour, nodelist=None, edgelist=[]):
        self.colour = colour
        self.nodes = np.zeros((0,4))
        self.edges = edgelist
        self.projected = []
        if nodelist:
            self.addNodes(nodelist)

    def addNodes(self, nodelist):
        ones_col = np.ones((len(nodelist), 1))
        to_add = np.hstack((nodelist, ones_col))
        self.nodes = np.vstack((self.nodes, to_add))

    def addEdges(self, edgelist):
        self.edges += edgelist

    def center(self):
        l = len(self.nodes)
        return [sum([node[0] for node in self.nodes]) / l, sum([node[1] for node in self.nodes]) / l, sum([node[2] for node in self.nodes]) / l]

    def translate(self, dx, dy, dz):
        self.nodes = np.dot(self.nodes, np.array([
            [ 1,  0,  0, 0],
            [ 0,  1,  0, 0],
            [ 0,  0,  1, 0],
            [dx, dy, dz, 1]
        ]))

    def rotate(self, angle, axis, center=None):
        (cx, cy, cz) = center if center else self.center()
        c = cos(angle)
        s = sin(angle)

        self.translate(*[-cx, -cy, -cz])

        if axis == X:
            self.nodes = np.dot(self.nodes, np.array([
                [1, 0,  0, 0],
                [0, c, -s, 0],
                [0, s,  c, 0],
                [0, 0,  0, 1],
            ]))
        elif axis == Y:
            self.nodes = np.dot(self.nodes, np.array([
                [c, 0, -s, 0],
                [0, 1,  0, 0],
                [s, 0,  c, 0],
                [0, 0,  0, 1],
            ]))
        elif axis == Z:
            self.nodes = np.dot(self.nodes, np.array([
                [c, -s, 0, 0],
                [s,  c, 0, 0],
                [0,  0, 1, 0],
                [0,  0, 0, 1],
            ]))
        else:
            exit("Asse non corretto")

        self.translate(*[cx, cy, cz])

    def scale(self, k, center=None):
        (cx, cy, cz) = center if center else self.center()
        self.translate(*[-cx, -cy, -cz])

        self.nodes = np.dot(self.nodes, np.array([
            [k, 0, 0, 0],
            [0, k, 0, 0],
            [0, 0, k, 0],
            [0, 0, 0, 1]
        ]))

        self.translate(*[cx, cy, cz])

    def project(self, pos):
        px = pos[0]
        py = pos[1]
        d = pos[2]
        points = [(((x/w)-px)*(d/(d+(z/w)))+px, ((y/w)-py)*(d/(d+(z/w)))+py) if d != -(z/w) else (-1, -1) for (x, y, z, w) in self.nodes]
        return points

    def show(self, d=500, radius=5):
        w = screen.get_width()
        h = screen.get_height()
        projected = self.project([w/2, h/2, d])
        for (x, y) in projected:
            if (x>=0 and x<=w) and (y>=0 and y<=h):
                pygame.draw.circle(screen, self.colour, (int(np.around(x, decimals=0)), int(np.around(y, decimals=0))), radius)
        for (node1, node2, colour) in self.edges:
            pygame.draw.aaline(screen, colour, projected[node1], projected[node2])

#- Camera -#

class Camera:
    def __init__(self, pos, itemlist=None):
        self.pos = np.array(pos)
        self.dir = np.array([0, 0, 1]) # points towards the z axis
        self.itemlist = itemlist if itemlist else []

    def addItems(items):
        self.itemlist = self.itemlist + items if isinstance(items, list) else self.itemlist + [items]

    def translate(self, dx, dy, dz):
        self.pos += np.array([dx, dy, dz])

    def rotate(self, angle, axis):
        c = cos(angle)
        s = sin(angle)

        if axis == X:
            self.dir = np.dot(self.dir, np.array([
                [1, 0,  0],
                [0, c, -s],
                [0, s,  c]
            ]))
        elif axis == Y:
            self.dir = np.dot(self.dir, np.array([
                [c, 0, -s],
                [0, 1,  0],
                [s, 0,  c]
            ]))
        elif axis == Z:
            self.dir = np.dot(self.dir, np.array([
                [c, -s, 0],
                [s,  c, 0],
                [0,  0, 1]
            ]))
        else:
            exit("Asse non corretto")
#- Shapes -#

def Ellipsoid(center, radii, v_res, h_res, colour=(255, 255, 255)):
    obj = Wireframe(colour)
    (cx, cy, cz) = center
    (r1, r2, r3) = radii
    nodelist = []
    zenit = np.linspace(0, pi, v_res)
    azimuth = np.linspace(0, 2*pi, h_res, endpoint=False)

    for theta in zenit:
        for phi in azimuth:
            x = cx + r1 * sin(theta) * cos(phi)
            y = cy + r2 * sin(theta) * sin(phi)
            z = cz + r3 * cos(theta)
            point = np.array((x, y, z))
            nodelist.append(point)
            if theta == 0 or theta == pi:
                break

    obj.addNodes(nodelist)
    return obj

def Sphere(center, radius, res, colour=(255, 255, 255)):
    obj = Wireframe(colour)
    (cx, cy, cz) = center
    nodelist = []
    zenit = np.linspace(0, pi, res)
    azimuth = np.linspace(0, 2*pi, res, endpoint=False)

    for theta in zenit:
        for phi in azimuth:
            x = cx + radius * sin(theta) * cos(phi)
            y = cy + radius * sin(theta) * sin(phi)
            z = cz + radius * cos(theta)
            point = np.array((x, y, z))
            nodelist.append(point)
            if theta == 0 or theta == pi:
                break

    obj.addNodes(nodelist)
    return obj

def Cylinder(center, radii, height, v_res, h_res, colour=(255, 255, 255)):
    obj = Wireframe(colour)

    (cx, cy, cz) = center
    (r1, r2) = radii
    nodelist = []
    zenit = np.linspace(0, 2*pi, h_res, endpoint=False)
    H = np.linspace(-height/2, height/2, v_res)

    for theta in zenit:
        for h in H:
            x = cx + r1 * cos(theta)
            y = cy + r2 * sin(theta)
            z = cz + h
            point = np.array((x, y, z))
            nodelist.append(point)

    obj.addNodes(nodelist)

    return obj

def Cube(center, sidelen, colour=(255, 255, 255)):
    obj = Wireframe(colour)
    (cx, cy, cz) = center

    nodelist = [(x,y,z) for x in (cx - sidelen, cx + sidelen) for y in (cy - sidelen, cy + sidelen) for z in (cz - sidelen, cz + sidelen)]
    edgelist = [(n,n+4,colour) for n in range(0,4)] + [(n,n+1,colour) for n in range(0,8,2)] + [(n,n+2,colour) for n in (0,1,4,5)]   

    obj.addNodes(nodelist)
    obj.addEdges(edgelist)

    return obj

def Parallelepiped(center, sidelens, colour=(255, 255, 255)):
    obj = Wireframe(colour)
    (cx, cy, cz) = center
    (lx, ly, lz) = sidelens

    nodelist = [(x,y,z) for x in (cx - lx, cx + lx) for y in (cy - ly, cy + ly) for z in (cz - lz, cz + lz)]
    edgelist = [(n,n+4,colour) for n in range(0,4)] + [(n,n+1,colour) for n in range(0,8,2)] + [(n,n+2,colour) for n in (0,1,4,5)]   

    obj.addNodes(nodelist)
    obj.addEdges(edgelist)

    return obj

#- input handling -#

key_to_func = {
    pygame.K_KP4 : (lambda x : x.translate(*(-5, 0, 0))),
    pygame.K_KP6 : (lambda x : x.translate(*(5, 0, 0))),
    pygame.K_KP2 : (lambda x : x.translate(*(0, 5, 0))),
    pygame.K_KP8 : (lambda x : x.translate(*(0, -5, 0))),
    pygame.K_KP9 : (lambda x : x.translate(*(0, 0, 5))),
    pygame.K_KP7 : (lambda x : x.translate(*(0, 0, -5))),
    pygame.K_KP1 : (lambda x, center: x.scale(1.25, center)),
    pygame.K_KP3 : (lambda x, center: x.scale(0.8, center)),
    pygame.K_s : (lambda x, center: x.rotate(-pi/64, ux)),
    pygame.K_w : (lambda x, center: x.rotate( pi/64, ux)),
    pygame.K_d : (lambda x, center: x.rotate(-pi/64, uy)),
    pygame.K_a : (lambda x, center: x.rotate( pi/64, uy)),
    pygame.K_e : (lambda x, center: x.rotate(-pi/64, uz)),
    pygame.K_q : (lambda x, center: x.rotate( pi/64, uz))
}

one_arg = {
    pygame.K_KP4,
    pygame.K_KP6,
    pygame.K_KP2,
    pygame.K_KP8,
    pygame.K_KP7,
    pygame.K_KP9
}

two_arg = {
    pygame.K_KP1,
    pygame.K_KP3,
    pygame.K_w,
    pygame.K_s,
    pygame.K_d,
    pygame.K_a,
    pygame.K_e,
    pygame.K_q
}

def key_input(key, itemlist):
    if key in key_to_func:
        for item in itemlist:
            if key in one_arg:
                key_to_func[key](item)
            else:
                key_to_func[key](item, item.center())
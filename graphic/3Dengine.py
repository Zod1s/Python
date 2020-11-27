#--This program shows a rotating 2D orthogonal projection of a cube--#

import tkinter as tk
import numpy as np
import time

#------------projection and rotation functions-------------#

def project(points):
    projected = np.zeros((8,2))
    for i in range(len(points)):
        projected[i] = np.dot(projection_matrix, points[i].T)
    return projected

def rotate(points, rotation_matrix, center):
    rotated = np.zeros((8,3))
    for i in range(len(points)):
        rotated[i] = np.sum([np.dot(rotation_matrix, (np.subtract(points[i], center)).T), center], axis=0)
    return rotated

def rotationX(angle):
    return np.array(     #rotation around X axis
        [
            [1.0,           0.0,            0.0],
            [0.0, np.cos(angle), -np.sin(angle)],
            [0.0, np.sin(angle),  np.cos(angle)]
        ]
    )

def rotationY(angle):
    return np.array(     #rotation around Y axis
        [
            [np.cos(angle),  0.0,  np.sin(angle)],
            [          0.0,  1.0,            0.0],
            [-np.sin(angle), 0.0,  np.cos(angle)]
        ]
    )

def rotationZ(angle):
    return np.array(     #rotation around Z axis 
        [   
            [np.cos(angle), -np.sin(angle),  0.0],
            [np.sin(angle),  np.cos(angle),  0.0],
            [          0.0,            0.0,  1.0]
        ]
    )

#----------------------other functions---------------------#

def connect(a, b, self, colour=""):
    self.create_line(a[0], a[1], b[0], b[1], fill=colour)

def draw_circle(center, radius, self, colour=""):
    self.create_oval(center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius, fill=colour)

#--------------------costants/variables--------------------#

WIDTH = 800
HEIGHT = 600
WIDTH_FLOAT = 800.0
HEIGHT_FLOAT = 600.0

angle = 0
radius = 10
distance = 2.0

done = False

#-------------------matrices and arrays--------------------#

projection_matrix = np.array( #projects a 3D point 
    [                         #on a 2D plane
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]
)

identity_matrix = np.array( #it's the 3x3 identity matrix
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]
)

points = np.zeros((8,3)) #initilaising the array that contains
                         #all the vertices of the cube

#--------------------------points--------------------------#

points[0] = [WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2-100.0, 100.0]
points[1] = [WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2-100.0, 100.0]
points[2] = [WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2+100.0, 100.0]
points[3] = [WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2+100.0, 100.0]
points[4] = [WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2-100.0,-100.0]
points[5] = [WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2-100.0,-100.0]
points[6] = [WIDTH_FLOAT/2+100.0, HEIGHT_FLOAT/2+100.0,-100.0]
points[7] = [WIDTH_FLOAT/2-100.0, HEIGHT_FLOAT/2+100.0,-100.0]

center = [WIDTH_FLOAT/2, HEIGHT_FLOAT/2, 0.0]

#-------------------tkinter initialisation------------------#

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=HEIGHT, width=WIDTH, bd=0)
canvas.grid()

while not done:

    #update rotation matrices
    rotateX = rotationX(angle)
    rotateY = rotationY(angle)
    rotateZ = rotationZ(angle)

    rotated_points = rotate(rotate(rotate(points, rotateX, center), rotateY, center), rotateZ, center)

    projected_points = project(rotated_points)
    
    canvas.delete("all")

    for i in range(8):
        draw_circle(projected_points[i], radius, canvas, colour="white")

    for i in range(4):
        connect(    projected_points[i],     projected_points[((i+1)%4)], canvas, colour="white")
        connect(projected_points[(i+4)], projected_points[(((i+1)%4)+4)], canvas, colour="white")
        connect(    projected_points[i],         projected_points[(i+4)], canvas, colour="white") 

    root.update()
    angle += 0.03
    time.sleep(1.0/75.0)
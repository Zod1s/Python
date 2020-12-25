import numpy as np
from sys import exit
from typing import List

Point = List[float]

def intersection(a: Point, b: Point, plane: str) -> Point:
    """
    finds the intersection between a plane parallel to XY plane 
    and a line that passes between two points, A and B. 
    A is first point, B is second point.
    """

    z = plane
    A = a
    B = b

    v = np.subtract(B, A) #direction of the line

    coefficient_matrix = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0]
        ]
    )

    known_term = np.array([0.0, 0.0, z])

    if v[0] == 0 and v[1] == 0 and v[2] == 0:
        exit("punti coincidenti")

    # elif v[0] == 0:
    #     if v[1] == 0 and not(v[2] == 0):
    #         coefficient_matrix[0][0] = 1.0
    #         coefficient_matrix[1][1] = 1.0
    #         known_term[0] = A[0]
    #         known_term[1] = A[1]
    #     elif v[2] == 0:
    #         coefficient_matrix[0][0] = 1.0
    #         coefficient_matrix[1][2] = 1.0
    #         known_term[0] = A[0]
    #         known_term[1] = A[2]

    # elif v[1] == 0:
    #     if v[2] == 0:
    #         coefficient_matrix[0][1] = 1.0
    #         coefficient_matrix[1][2] = 1.0
    #         known_term[0] = A[1]
    #         known_term[1] = A[2]
    #     else:
    #         pass

    if v[0] == 0.0 and v[1] == 0.0:
        coefficient_matrix[0][0] = 1.0
        coefficient_matrix[1][1] = 1.0
        known_term[0] = A[0]
        known_term[1] = A[1]

    elif v[0] == 0.0 and v[2] == 0.0:
        coefficient_matrix[0][0] = 1.0
        coefficient_matrix[1][2] = 1.0
        known_term[0] = A[0]
        known_term[2] = A[2]

    elif v[1] == 0.0 and v[2] == 0.0:
        coefficient_matrix[0][1] = 1.0
        coefficient_matrix[1][2] = 1.0
        known_term[1] = A[1]
        known_term[2] = A[2]

    elif v[0] == 0:
        coefficient_matrix[0][1] = v[2]
        coefficient_matrix[0][2] = -v[1]
        coefficient_matrix[1][0] = 1.0
        known_term[0] = v[2]*A[1]-v[1]*A[2]
        known_term[1] = A[0]

    elif v[1] == 0:
        coefficient_matrix[0][0] = v[2]
        coefficient_matrix[0][2] = -v[0]
        coefficient_matrix[1][1] = 1.0
        known_term[0] = v[2]*A[0]-v[0]*A[2]
        known_term[1] = A[1]

    elif v[2] == 0:
        coefficient_matrix[0][0] = v[1]
        coefficient_matrix[0][1] = -v[0]
        coefficient_matrix[1][2] = 1.0
        known_term[0] = v[1]*A[0]-v[0]*A[1]
        known_term[1] = A[2]

    elif v[0] != 0 and v[1] != 0 and v[2] != 0:
        coefficient_matrix[0][0] = v[1]
        coefficient_matrix[0][1] = -v[0]
        coefficient_matrix[1][1] = v[2]
        coefficient_matrix[1][2] = -v[1]
        known_term[0] = v[1]*A[0]-v[0]*A[1]
        known_term[1] = v[2]*A[1]-v[1]*A[2]

    solution = np.linalg.solve(coefficient_matrix, known_term)
    return solution

def solve(a, b):
    """
    a is a square matrix NxN, b is a column matrix Nx1
    """
    if np.linalg.det(a) == 0:
        exit("il sistema non ha soluzioni")
    else:
        A = np.linalg.inv(a)
        X = np.dot(A, b)
        return X

print(intersection([3.0, 2.0, 3.0], [4.0, 3.0, 12.0], 9.0))
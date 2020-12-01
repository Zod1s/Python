import numpy as np

def intersection(a=[], b=[], plane=0.0):
    v = np.subtract(b, a) #direction of the line
    coefficient_matrix = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0]
        ]
    )
    known_term = np.array([0.0, 0.0, plane])

    if v[0] == 0.0 and v[1] == 0.0:
        coefficient_matrix[0][0] = 1.0
        coefficient_matrix[1][1] = 1.0
        known_term[0] = a[0]
        known_term[1] = a[1]

    elif v[0] == 0.0 and v[2] == 0.0:
        coefficient_matrix[0][0] = 1.0
        coefficient_matrix[1][2] = 1.0
        known_term[0] = a[0]
        known_term[2] = a[2]

    elif v[1] == 0.0 and v[2] == 0.0:
        coefficient_matrix[0][1] = 1.0
        coefficient_matrix[1][2] = 1.0
        known_term[1] = a[1]
        known_term[2] = a[2]

    elif v[0] == 0:
        coefficient_matrix[0][1] = v[2]
        coefficient_matrix[0][2] = -v[1]
        coefficient_matrix[1][0] = 1.0
        known_term[0] = v[2]*a[1]-v[1]*a[2]
        known_term[1] = a[0]

    elif v[1] == 0:
        coefficient_matrix[0][0] = v[2]
        coefficient_matrix[0][2] = -v[0]
        coefficient_matrix[1][1] = 1.0
        known_term[0] = v[2]*a[0]-v[0]*a[2]
        known_term[1] = a[1]

    elif v[2] == 0:
        coefficient_matrix[0][0] = v[1]
        coefficient_matrix[0][1] = -v[0]
        coefficient_matrix[1][2] = 1.0
        known_term[0] = v[1]*a[0]-v[0]*a[1]
        known_term[1] = a[2]

    elif v[0] != 0 and v[1] != 0 and v[2] != 0:
        coefficient_matrix[0][0] = v[1]
        coefficient_matrix[0][1] = -v[0]
        coefficient_matrix[1][1] = v[2]
        coefficient_matrix[1][2] = -v[1]
        known_term[0] = v[1]*a[0]-v[0]*a[1]
        known_term[1] = v[2]*a[1]-v[1]*a[2]
    solution = np.linalg.solve(coefficient_matrix, known_term)
    return solution
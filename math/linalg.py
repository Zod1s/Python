import numpy as np

A = np.array(
    [
        [ 0.3,   -0.2,      0,      0],
        [-0.2,  1.325, -0.125,     -1],
        [   0, -0.125,    0.5, -0.125],
        [   0,     -1, -0.125,  1.625]
    ]
)

b = np.array([3, -3, 0, 6])

print(np.linalg.solve(A, b))

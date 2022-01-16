import numpy as np
import scipy.linalg as linalg

vec1 = np.array([2, -2, -1, 1])
vec2 = np.array([3, 0, 2, 1])
vec3 = np.array([3, -2, 2, 2])
vec4 = np.array([3, 2, 2, 0])

mat = np.stack([vec1, vec2, vec3, vec4])

print(linalg.det(mat))

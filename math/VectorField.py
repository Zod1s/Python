from itertools import product

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

E0 = 150
a = 3.5
b = 1.2
l = 1

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = map(lambda x: np.around(x, decimals=2),
              np.meshgrid(np.arange(- 2 * l, 2 * l + 0.01, 0.4), np.arange(- 2 * l, 2 * l + 0.01, 0.4), np.arange(- 2 * l, 2 * l + 0.01, 0.4)))

u = E0 * (a * x**3 + b * x)
v = E0 * (b * y)**2
w = E0 * (b * l)**2

# Color by magnitude
c = np.sqrt(np.square(u) + np.square(v) + np.square(w))
# Flatten and normalize
c = (c.ravel() - c.min()) / c.ptp()
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))
# Colormap
c = plt.cm.hsv(c)

q = ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True, colors=c)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

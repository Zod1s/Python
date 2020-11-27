import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

u_space = np.linspace(0.0, 2*np.pi, 100, endpoint=False)
v_space = np.linspace(-1.0, 1.0, 100)

x = [(1 + v/2.0*np.cos(u/2.0))*np.cos(u) for u in u_space for v in v_space]
y = [(1 + v/2.0*np.cos(u/2.0))*np.sin(u) for u in u_space for v in v_space]
z = [v/2.0*np.sin(u/2.0) for u in u_space for v in v_space]

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
ax.legend()

plt.show()
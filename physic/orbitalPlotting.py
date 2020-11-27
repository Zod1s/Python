import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from sympy.utilities.lambdify import lambdify

import atomicOrbitals as Orb

print('modules loaded')

# print('generating angles')
# P = np.linspace(0, 2 * np.pi, 2000)
# T = np.linspace(0, np.pi, 1000)
# T, P = np.meshgrid(T, P)

# print('generating orbitals')

# l = 2
# # R0 = lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.dOrbital(0).evalf(), 'numpy')(T,P)
# # R1 = lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.dOrbital(-1).evalf(), 'numpy')(T, P)
# # R2 = lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.dOrbital(1).evalf(), 'numpy')(T, P)
# # R3 = lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.dOrbital(-2).evalf(), 'numpy')(T, P)
# # R4 = lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.dOrbital(2).evalf(), 'numpy')(T, P)

# radii = [lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.orbital(l, m).evalf(), 'numpy')(T, P) for m in range(-l, l + 1)]
# # radii = [lambdify((Orb.theta, Orb.phi), Orb.OrbitalHarmonic.orbital(l, 5).evalf(), 'numpy')(T,P)]
# print('orbitals generated')

# print('generating points')
# points = [Orb.SphToCart(abs(radii[i]), T, P) for i in range(len(radii))]
# print('points generated')

# fig = plt.figure()
# ax0 = fig.add_subplot(111, projection='3d')

# print('plotting')
# ax0.plot_surface(*points[1])
# print('plotted')
# # ax0.plot_surface(*points[1])

# # ax0.plot_surface(x0, y0, z0)
# # ax0.plot_surface(x1, y1, z1)
# # ax0.plot_surface(x2, y2, z2)
# # ax0.plot_surface(x3, y3, z3)
# # ax0.plot_surface(x4, y4, z4)

# ax0.xaxis.pane.fill = False
# ax0.xaxis.pane.set_edgecolor('white')
# ax0.yaxis.pane.fill = False
# ax0.yaxis.pane.set_edgecolor('white')
# ax0.zaxis.pane.fill = False
# ax0.zaxis.pane.set_edgecolor('white')
# ax0.grid(False)
# # Remove axis
# ax0.w_xaxis.line.set_lw(0.)
# ax0.set_xticks([])
# ax0.w_yaxis.line.set_lw(0.)
# ax0.set_yticks([])
# ax0.w_zaxis.line.set_lw(0.)
# ax0.set_zticks([])

# scaling = np.array([getattr(ax0, 'get_{}lim'.format(dim))() for dim in 'xyz'])
# ax0.auto_scale_xyz(*([[np.min(scaling), np.max(scaling)]] * 3))

# plt.show()
# print('quitting')


def normalize(v):
    return v / np.linalg.norm(v)


def mapp(x, inmin, inmax, outmin, outmax):
    return (x - inmin) * (outmax - outmin) / (inmax - inmin) + outmin


# l<n, |m|<=l
n = 3
l = 1
m = 0

print('generating triplets')
R = np.linspace(0, 20, 20)
T = np.linspace(0, np.pi, 10)
P = np.linspace(0, 2 * np.pi, 20)
R, T, P = np.meshgrid(R, T, P)

print('generating orbital')

Psi = abs(lambdify(
    (Orb.r, Orb.theta, Orb.phi), Orb.RealOrbital.orbital(n, l, m).evalf(), 'numpy')(R, T, P))

Psi = normalize(Psi)

print('orbital generated')

print('generating points')
x0, y0, z0 = Orb.SphToCart(R, T, P)
print('points generated')

fig = plt.figure()
ax0 = fig.add_subplot(111, projection='3d')

print('plotting')

print('generating colors')
cols = [item for List in [Psi[0][i] for i in range(len(Psi[0]))] for item in List] * len(Psi)
colors = cm.rgba(1, 0, 0, cols / max(cols))
colmap = cm.ScalarMappable(cmap=cm.rgba)
colmap.set_array(cols)
cb = fig.colorbar(colmap)
print('colors generated')

print('generating alphas')

# alpha = list([item for List in [Psi[0][i] for i in range(len(Psi[0]))] for item in List] * len(Psi))
# print(type(alpha))
print('alphas generated')

# print('scattering')
# ax0.scatter(x0, y0, z0, alpha=alpha)  # , c=colors)
# print('scattered')

# ax0.xaxis.pane.fill = False
# ax0.xaxis.pane.set_edgecolor('white')
# ax0.yaxis.pane.fill = False
# ax0.yaxis.pane.set_edgecolor('white')
# ax0.zaxis.pane.fill = False
# ax0.zaxis.pane.set_edgecolor('white')
# ax0.grid(False)
# # Remove axis
# ax0.w_xaxis.line.set_lw(0.)
# ax0.set_xticks([])
# ax0.w_yaxis.line.set_lw(0.)
# ax0.set_yticks([])
# ax0.w_zaxis.line.set_lw(0.)
# ax0.set_zticks([])

# scaling = np.array([getattr(ax0, 'get_{}lim'.format(dim))() for dim in 'xyz'])
# ax0.auto_scale_xyz(*([[np.min(scaling), np.max(scaling)]] * 3))

# plt.show()
# print('quitting')

import numpy as np
from sympy import *
from sympy import im as Im
from sympy import re as Re

init_printing(use_latex=True)

r, theta, phi = symbols('r theta phi', real=True)


class OrbitalHarmonic:
    @staticmethod
    def orbital(l, m):
        if m == 0:
            return sphericalHarmonic(l, 0, theta, phi)
        else:
            M = abs(m)
            O1 = simplify(sphericalHarmonic(l, -M, theta, phi))
            O2 = simplify(sphericalHarmonic(l, M, theta, phi))
            K1 = 1j * sqrt(1 / 2) if m < 0 else sqrt(1 / 2)
            K2 = - (-1) ** m if m < 0 else (-1) ** m
            W = K1 * (O1 + K2 * O2)
            return W

    @staticmethod
    def sOrbital():
        return OrbitalHarmonic.orbital(0, 0)

    @staticmethod
    def pOrbital(m):
        return OrbitalHarmonic.orbital(1, m)

    @staticmethod
    def dOrbital(m):
        return OrbitalHarmonic.orbital(2, m)

    @staticmethod
    def fOrbital(m):
        return OrbitalHarmonic.orbital(3, m)


class RealOrbital:
    @staticmethod
    def orbital(n, l, m):
        if m == 0:
            return ComplexOrbital.orbital(n, l, 0)
        else:
            R = radialComponent(n, l)
            M = abs(m)
            O1 = simplify(R * sphericalHarmonic(l, -M, theta, phi))
            O2 = simplify(R * sphericalHarmonic(l, M, theta, phi))
            K1 = 1j * sqrt(1 / 2) if m < 0 else sqrt(1 / 2)
            K2 = - (-1) ** m if m < 0 else (-1) ** m
            W = K1 * (O1 + K2 * O2)
            return W

    @staticmethod
    def sOrbital(n):
        return RealOrbital.orbital(n, 0, 0)

    @staticmethod
    def pOrbital(n, m):
        return RealOrbital.orbital(n, 1, m)

    @staticmethod
    def dOrbital(n, m):
        return RealOrbital.orbital(n, 2, m)

    @staticmethod
    def fOrbital(n, m):
        return RealOrbital.orbital(n, 3, m)


class ComplexOrbital:
    @staticmethod
    def orbital(n, l, m):
        radius = radialComponent(n, l)
        harmonic = sphericalHarmonic(l, m, theta, phi)
        return radius * harmonic

    @staticmethod
    def sOrbital(n):
        return ComplexOrbital.orbital(n, 0, 0)

    @staticmethod
    def pOrbital(n, m):
        return ComplexOrbital.orbital(n, 1, m)

    @staticmethod
    def dOrbital(n, m):
        return ComplexOrbital.orbital(n, 2, m)

    @staticmethod
    def fOrbital(n, m):
        return ComplexOrbital.orbital(n, 3, m)


def sphericalHarmonic(l, m, theta, phi):
    '''
    Y_l^m(theta, phi)
    l∊N, |m|<=l, theta∊[0, pi], phi∊[0, 2pi]
    '''
    K1 = (-1)**((m + abs(m)) / 2)
    K2 = (2 * l + 1) / (4 * pi)
    K3 = factorial(l - abs(m))
    K4 = factorial(l + abs(m))
    K5 = sqrt(K2 * K3 / K4)
    K = K1 * K5
    P = associatedLegendrePoly(l, abs(m), cos(theta))
    E = exp(I * m * phi)
    return K * P * E


def associatedLegendrePoly(l, m, x):
    '''
    P_l^m(x), l>=0, |m|<=l
    '''
    if m < 0:
        K1 = (-1)**m
        K2 = factorial(l - abs(m))
        K3 = factorial(l + abs(m))
        P = associatedLegendrePoly(l, abs(m), x)
        return K1 * (K2 / K3) * P
    elif m == 0:
        return LegendrePoly(l, x)
    else:
        f = var('f')
        K1 = 1
        K2 = sin(theta)**m
        P1 = LegendrePoly(l, f).diff(f, m)
        P = K1 * K2 * P1.subs(f, cos(theta))
        return P


def LegendrePoly(l, x):
    '''
    P_l(x), l>=0
    '''
    if l == 0:
        return 1
    elif l == 1:
        return x
    elif l == 2:
        return (1 / 2) * (3 * x**2 - 1)
    elif l == 3:
        return (1 / 2) * (5 * x**3 - 3 * x)
    elif l == 4:
        return (1 / 8) * (35 * x**4 - 30 * x**2 + 3)
    elif l == 5:
        return (1 / 8) * (63 * x**5 - 70 * x**3 + 15 * x)
    elif l == 6:
        return (1 / 16) * (231 * x**6 - 315 * x**4 + 105 * x**2 - 5)
    else:
        A = LegendrePoly(l - 1, x)
        B = LegendrePoly(l - 2, x)
        K1 = (2 * l - 1) * x
        K2 = l - 1
        F = K1 * A / l - K2 * B / l
        return F


def radialComponent(n, l):
    '''
    R(r), 0 <= l< n
    '''
    a0 = 1
    rho = 2 * r / (n * a0)
    K1 = (2 / (n * a0)) ** 3
    K2 = factorial(n - l - 1)
    K3 = 2 * n * factorial(n + 1)
    K4 = sqrt(K1 * K2 / K3)
    K5 = exp(-rho / 2)
    K6 = rho ** l
    L = LaguerrePoly(n - l - 1, 2 * l + 1, rho)
    R = K4 * K5 * K6 * L
    return R


def LaguerrePoly(l, a, x):
    '''
    L_l^a(x)
    '''
    if isinstance(l, int) and isinstance(a, int):
        if l == 0:
            return 1
        elif l == 1:
            return 1 + a - x
        else:
            K1 = (2 * l - 1 + a - x)
            K2 = (k + a)
            P1 = LaguerrePoly(l - 1, a, x)
            P2 = LaguerrePoly(l - 2, a, x)
            P = (K1 * P1 - K2 * P2) / (l)
            return P
    else:
        L = symbols('L', cls=Function)
        return L(l, a, x)


def SphToCart(rho, th, ph):
    x = rho * np.sin(th) * np.cos(ph)
    y = rho * np.sin(th) * np.sin(ph)
    z = rho * np.cos(th)
    return [x, y, z]


def CartToSph(x, y, z):
    rho = np.sqrt(x**2 + y**2 + z**2)
    th = np.arctan2(np.sqrt(x**2 + y**2), z)
    ph = np.arctan2(y, x)
    return [rho, th, ph]


# F = ComplexOrbital.orbital(2, 1, -1)
# f = RealOrbital.orbital(2, 1, -1)

# pprint(simplify(f))
# pprint(simplify(Re(f)))
# pprint(simplify(Im(f)))

# sph = sphericalHarmonic(3, -2, theta, phi)

# pprint(sph)
# Int = Integral(Integral(abs(sph)**2*sin(theta), (theta, 0, pi)), (phi, 0, 2*pi))
# pprint(Int)
# pprint(Int.doit())

# Integral on unit sphere = Integral(Integral(f(theta, phi)*sin(theta),
# (theta, 0, pi)), (phi, 0, 2*pi))

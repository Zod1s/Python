import numpy as np


def derivata(func, x, dx, decimal=5):
    dydx = (func(x + dx / 2) - func(x - dx / 2)) / dx
    return np.around((dydx), decimal)


def integrale(func, a, b, res=100, decimal=5):
    n = 2 * res

    h = (b - a) / n
    s = func(a) + func(b)

    for i in range(1, n, 2):
        s += 4 * func(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * func(a + i * h)

    return np.around((s * h / 3), decimal)


def proto_sin(A, w, t):
    def temp(x):
        return A * np.around((np.sin(w * x + t)), 5)
    return temp


def proto_cos(A, w, t):
    def temp(x):
        return A * np.around((np.cos(w * x + t)), 5)
    return temp


def proto_line(m, q):
    def temp(x):
        return np.around((m * x + q), 5)
    return temp


def proto_parabola(a, b, c):
    def temp(x):
        return np.around((a * x**2 + b * x + c), 5)
    return temp


def proto_exp(a):
    def temp(x):
        return np.around((a**x), 5)
    return temp


def proto_log(a):
    def temp(x):
        return np.around((np.log(x) / np.log(a)), 5)
    return temp

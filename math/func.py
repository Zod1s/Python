import numpy as np

def derivata(func, x, dx, decimal=5):
    dy = (func(x + dx/2) - func(x - dx/2)) / dx
    return np.around((dy), decimal)

def integrale(func, a, b, res=100, decimal=5):
    n = 2 * res

    h = (b - a) / n
    s = func(a) + func(b)

    for i in range(1, n, 2):
        s += 4 * func(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * func(a + i * h)

    return np.around((s * h / 3), decimal)

def proto_sin(A, w, t):
    return lambda x : A * np.around((np.sin(w * x + t)), 5)

def proto_cos(A, w, t):
    return lambda x : A * np.around((np.cos(w * x + t)), 5)

def proto_line(m, q):
    return lambda x : np.around((m * x + q), 5)

def proto_parabola(a, b, c):
    return lambda x : np.around((a * x**2 + b * x + c), 5)

def proto_exp(a):
    return lambda x : np.around((a**x), 5)

def proto_log(a):
    return lambda x : np.around((np.log(x) / np.log(a)), 5)
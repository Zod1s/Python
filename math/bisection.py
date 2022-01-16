import math


def f(x):
    return x - 5


def bisection(f, a, b, prec):  # , iter=0):
    m = 0
    while ((b - a) / 2 > prec):
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(m) * f(a) < 0:
            b = m
        else:
            a = m
    return m


print(bisection(f, 1, 6, 0.000000001))

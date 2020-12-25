import numpy as np

def fft(xs):
    N = len(xs)
    coeffs = [np.exp(-1j * 2 * np.pi * n / N) for n in range(N)]
    Xk = [xs[i] * coeffs[k]**k for k in range(N) for i in range(N)]
    return Xk

def func(x):
    return np.sin(2 * np.pi * x)

xs = np.linspace(0, 1, 50)
ys = list(map(func, xs))
ffts = fft(ys)

print(list(map(abs, ffts)))
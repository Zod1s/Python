import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.sin(2*np.pi*t)

N = 700
T = 1 / 250
F = 1 / T

xs = np.linspace(0.0, N*T, N)
ys = f(xs)
noise = np.random.normal(0, 1, ys.shape)
dist = ys + noise

fft = scipy.fftpack.fft(dist)
xf = np.linspace(0.0, F/2, N/2)

plt.plot(xf, 2.0/N * np.abs(fft[:N//2]))
plt.show()
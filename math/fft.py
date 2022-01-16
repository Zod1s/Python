import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


def fft(xs):
    N = len(xs)
    coeffs = [np.exp(-1j * 2 * np.pi * n / N) for n in range(N)]
    Xk = [sum((xs[n] * coeffs[(k * n) % N] for n in range(N)))
          for k in range(N)]
    return Xk


def func(x):
    return np.sin(2 * np.pi * x) + np.sin(2 * np.pi * 5 * x)


number_of_samples = 500
samples_freq = 1 / 80

xs = np.linspace(0.0, samples_freq * number_of_samples, number_of_samples)
ys = func(xs)
ffts = np.abs(fft(ys))
xffts = np.linspace(0, 1 / (2 * samples_freq), number_of_samples // 2)

m = max(ffts)
i = [x for (x, y) in enumerate(ffts) if y == m]

# ffts = np.abs(scipy.fftpack.fft(ys))
plt.plot(xs, ys)
plt.plot(xffts, ffts[:number_of_samples // 2])

plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-500, 501, 1)
X, Y = np.meshgrid(x, x)
wavelength = 0.1
angle = 0
gratingX1 = np.logical_and(-20 <= X, X <= -16)
gratingX2 = np.logical_and(16 <= X, X <= 20)
gratingX = np.logical_or(gratingX1, gratingX2)
gratingY = np.logical_and(-100 <= Y, Y <= 100)
grating = np.logical_and(gratingX, gratingY)


plt.set_cmap("gray")
plt.subplot(121)
plt.imshow(grating)
# Calculate Fourier transform of grating
ft = np.fft.ifftshift(grating)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)

plt.subplot(122)
plt.imshow(abs(ft))
plt.xlim([480, 520])
plt.ylim([520, 480])  # Note, order is reversed for y
plt.show()



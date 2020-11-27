import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def wave_func(a, x, t, lenght, freq):
    return a * np.cos(2 * np.pi * (x / lenght - t / freq))

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
x = np.arange(0.0, 5.0, 0.001)
t0 = 0
a0 = 5
f0 = 2
delta_f = 0.01
l0 = 5
s = wave_func(a0, x, t0, l0, f0)
l, = plt.plot(x, s, lw=2, color='red')
plt.axis([0, 5.0, -10, 10])

axcolor = 'lightgoldenrodyellow'
axtime = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

stime = Slider(axtime, 'T', 0, 10.0, valinit=t0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

def update(val):
    amp = samp.val
    time = stime.val
    l.set_ydata(wave_func(amp, x, time, l0, f0))
    fig.canvas.draw_idle()

stime.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    stime.reset()
    samp.reset()

button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()

radio.on_clicked(colorfunc)

plt.show()
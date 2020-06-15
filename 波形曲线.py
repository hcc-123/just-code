import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as FA
import numpy as np

xdata = np.linspace(0, 2 * np.pi, 50)
fig, ax = plt.subplots(1, 1, figsize = (8, 5))
b_cir = ax.plot(5 * np.cos(xdata), 5 * np.sin(xdata))
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(bottom = 'off', left = 'off', labelbottom = 'off', labelleft = 'off')
def update(frame):
    movX1 = 5 * np.cos(frame * 1)
    movY1 = 5 * np.sin(frame * 1)
    a = movp1.set_data(movX1, movY1)
    return movp1
ani = FA(fig, update, frames = xdata, blit = True)
"""
WarriorsSuraj
Simple physics projectile motion simulator
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
g = -9.81
t = np.linspace(0, 3, 40)

print("Welcome to a simple projectile motion simulator!")
print("What would you like your initial velocity to be (+ve only) in m/s: ")
u = float(input())

#ADJUST AXES LIMITS ACCORDING TO MAX DISPLACEMENTS (energy methods or more suvat?)

s = u * t + 0.5 * g * t ** 2
scat = ax.scatter(t[0], s[0], c="b", s=5, label=f'u = {u} m/s')
ax.set(xlim=[0, 3], ylim=[0, 10], xlabel='Time [s]', ylabel='Displacement [m]')
ax.legend()

def update(frame):
    x = t[:frame]
    y = s[:frame]
    if y.size != 0 and y[-1] <= 0:
        return
    data = np.stack([x,y]).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval = 30)
plt.show()

#!/usr/bin/python

import sys
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib import animation

SOL_MASS = 1.989e30
EAR_MASS = 5.972e24
AU       = 1.396e11
PARSEC   = 3.0857e16

timeline=[]
with open(sys.argv[1]) as f:
    niter = f.readline()
    nb = f.readline()
    mass_low = f.readline()
    mass_up = f.readline()
    vel_low = f.readline()
    vel_up = f.readline()
    cubelen = f.readline()

    niter = int(niter)
    nb = int(nb)
    mass_low = float(mass_low)
    mass_up = float(mass_up)
    cubelen = float(cubelen)

    for _ in range(niter):
        X=[]
        Y=[]
        Z=[]

        for _ in range(nb):
            x,y,z=f.readline().split()
            X.append(x)
            Y.append(y)
            Z.append(z)

        timeline.append((X,Y,Z))


fig = plt.figure()
ax = plt.axes(xlim=(-cubelen/2.0, cubelen/2.0), ylim=(-cubelen/2.0, cubelen/2.0))
plt.xlabel("x-coordinate [m]")
plt.ylabel("y-coordinate [m]")
line, = ax.plot([], [],marker='o',linestyle='none')
def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(timeline[i][0], timeline[i][1])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=niter, interval=20, blit=True)

#plt.plot(X,Y, marker="o", linestyle="none")
plt.show()

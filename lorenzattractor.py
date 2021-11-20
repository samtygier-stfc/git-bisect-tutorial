#!/usr/bin/env python3
import matplotlib.pyplot as plt

# Initial values
xs = [0]
ys = [1]
zs = [1.05]

nsteps = 10000
for i in range(nsteps):
    # get current
    x, y, z = xs[i], ys[i], zs[i]

    # caclulate new
    dt = 0.01
    xs.append(x + ((10*(y - x)) * dt))
    ys.append(y + ((28*x - y - x*z) * dt))
    zs.append(z + ((x*y - 2.667*z) * dt))

ax = plt.figure().add_subplot(projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()

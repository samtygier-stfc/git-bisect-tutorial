#!/usr/bin/env python3


# Initial values
xs = [0]
ys = [1]
zs = [1.05]

for i in range(10000):
    # get current
    x, y, z = xs[i], ys[i], zs[i]

    # caclulate new
    xs.append(x + (10*(y - x) * 0.01))
    ys.append(y + (28*x - y - x*z * 0.01))
    zs.append(z + (x*y - 2.667*z * 0.01))
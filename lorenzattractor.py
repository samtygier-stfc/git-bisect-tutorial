#!/usr/bin/env python3
import matplotlib.pyplot as plt


def lorenzattractor(nsteps = 10000, dt = 0.01):
    # Initial values
    xs = [0]
    ys = [1]
    zs = [1.05]

    for i in range(nsteps):
        # get current
        x, y, z = xs[i], ys[i], zs[i]

        # calculate new
        xs.append(x + ((10*(y - x)) * dt))
        ys.append(y + ((28*x - y - x*z) * dt))
        zs.append(z + ((x*y - 2.667*z) * dt))

    return xs, ys, zs


def plot(xs, ys, zs):
    xs, ys, zs = lorenzattractor()
    # Plot on 3D projection
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.tight_layout()

    # Show plot to user
    plt.show()


def main():
    la_data = lorenzattractor()
    plot(*la_data)


if __name__ == "__main__":
    main()

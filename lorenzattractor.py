#!/usr/bin/env python3
import matplotlib.pyplot as plt


def calculate_velocity(x, y, z, a=10, b=28, c=2.667):
    xp = a * (y - x)
    yp = (b * x - y - x * z)
    zp = (x * y * c * z)

    return xp, yp, zp

def lorenzattractor(n_steps=10000, dt=0.01):
    # Initial values
    xs = [0]
    ys = [1]
    zs = [1.05]

    for i in range(n_steps):
        # get current
        x, y, z = xs[i], ys[i], zs[i]

        xp, yp, zp = calculate_velocity(x, y, z)

        # calculate new
        xs.append(x + (xp * dt))
        ys.append(y + (yp * dt))
        zs.append(z + (zp * dt))

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
    la_data = lorenzattractor(10000, 0.01)
    plot(*la_data)


if __name__ == "__main__":
    main()

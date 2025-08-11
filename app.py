import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Particle import Particle

PARTICLE_COUNT = 10
fig, ax = plt.subplots(1, 1, figsize=(7.5, 7.5), subplot_kw={"projection": "3d"})

particles = []


def init():
    init_ax()
    init_particles()

    return ax.collections


def init_ax():
    ax.set_title("3D Brownian motion simulation")
    ax.set(xlim3d=[-10, 10], xlabel="X-axis")
    ax.set(ylim3d=[-10, 10], ylabel="Y-axis")
    ax.set(zlim3d=[-10, 10], zlabel="Z-axis")


def init_particles():
    for _ in range(PARTICLE_COUNT):
        position = np.array([0.0, 0.0, 0.0])
        velocity = np.array([0.0, 0.0, 0.0])
        particle = Particle(position, velocity)
        ax.scatter(particle.position[0], particle.position[1], particle.position[2])

        particles.append(particle)


def update(frame):
    plt.cla()
    init_ax()

    for particle in particles:
        particle.move()
        ax.scatter(particle.position[0], particle.position[1], particle.position[2])

    return ax.collections


anim = FuncAnimation(fig, update, frames=200, init_func=init, interval=50, blit=False)
# plt.show()

anim.save("animation.gif")

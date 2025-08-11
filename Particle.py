import numpy as np


class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        self.velocity = np.random.uniform(-1, 1, 3)

        next_position = self.position + self.velocity

        if next_position[0] < -10:
            next_position[0] = -10
        elif next_position[0] > 10:
            next_position[0] = 10

        if next_position[1] < -10:
            next_position[1] = -10
        elif next_position[1] > 10:
            next_position[1] = 10

        if next_position[2] < -10:
            next_position[2] = -10
        elif next_position[2] > 10:
            next_position[2] = 10

        self.position = next_position

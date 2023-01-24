import numpy as np


class Star:
    def __init__(
        self, name: str, mass: int, radius: int, distance: int = 0, velocity: int = 0
    ):
        self.mass = mass
        self.radius = radius


class Planet:
    def __init__(self, name: str, distance: int, mass: int, period: int, radius: int):
        self.period = period
        self.mass = mass
        self.radius = radius
        self.distance = distance
        self.velocity = np.sqrt(((6.67408 * 10 ^ (-11)) * mass) / (2 * self.radius))


class Asteroid:
    def __init__(self, name: str, density: int, distance: int, radius: int):
        self.density = density
        self.radius = radius
        self.distance = distance
        self.volume = (4 / 3) * np.pi * (self.radius**3)
        self.mass = self.density * self.volume
        self.velocity = np.sqrt(
            ((6.67408 * 10 ^ (-11)) * self.mass) / (2 * self.radius)
        )

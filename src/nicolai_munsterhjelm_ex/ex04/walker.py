# -*- coding: utf-8 -*-

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicolai.munsterhjelm@nmbu.no'

import random


class Walker:
    def __init__(self, x0, h):
        self.position = x0
        self.home = h
        self.steps = 0

    def move(self):
        self.position += random.choice((-1, 1))
        self.steps += 1

    def is_at_home(self):
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps


def walker_simulation(distances, n):
    """Simlutates a walker n times for each distance
     in the 'distances' list."""
    for distance in distances:
        number_of_steps = []
        for i in range(n):
            walker = Walker(0, distance)
            while not walker.is_at_home():
                walker.move()
            number_of_steps.append(walker.get_steps())
        print(f"Distance: {distance} -> Path lengths: "
              f"{sorted(number_of_steps)}")


if __name__ == "__main__":
    distances = [1, 2, 5, 10, 20, 50, 100]
    walker_simulation(distances, 5)
